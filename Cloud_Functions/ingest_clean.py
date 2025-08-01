import pandas as pd
import hashlib
from io import StringIO
from google.cloud import bigquery, storage
from google.cloud.exceptions import NotFound
import functions_framework

# Configuración
project_id = 'pf-nba-e1'
dataset_id = 'pf_nba_e1'
bucket_name = 'pf-nba-csv'

client_bq = bigquery.Client(project=project_id)
client_storage = storage.Client(project=project_id)

# Funciones de limpieza
def hash_filas(df):
    return df.apply(lambda row: hashlib.md5(str(tuple(row)).encode()).hexdigest(), axis=1)

def limpiar_columnas_numericas(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                muestra = df[col].dropna().astype(str).str.replace(',', '.', regex=False)
                if muestra.str.replace('.', '', regex=False).str.isnumeric().mean() > 0.9:
                    df[col] = pd.to_numeric(muestra, errors='coerce')
            except:
                continue
    return df 

def manejar_columnas_especiales(df):
    if 'jersey' in df.columns:
        df['jersey'] = df['jersey'].astype(str).replace('nan', None).str.replace(r'\.0$', '', regex=True)
    return df

def limpiar_fechas(df):
    for col in df.columns:
        if 'date' in col.lower() or 'fecha' in col.lower():
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce').dt.date
            except:
                continue
    return df

def limpiar_enteros(df):
    for col in df.columns:
        if pd.api.types.is_float_dtype(df[col]):
            if (df[col].dropna() % 1 == 0).all():
                df[col] = df[col].astype('Int64')
    return df

def procesar_archivo(nombre_archivo):
    try:
        print(f"📁 Procesando {nombre_archivo}...")

        # Leer CSV desde Cloud Storage
        bucket = client_storage.bucket(bucket_name)
        blob = bucket.blob(f'prueba/{nombre_archivo}')
        data = blob.download_as_text(encoding='utf-8')
        df = pd.read_csv(StringIO(data))

        # Limpieza
        df = limpiar_columnas_numericas(df)
        df = manejar_columnas_especiales(df)
        df = limpiar_fechas(df)
        df = limpiar_enteros(df)
        df["fila_hash"] = hash_filas(df)

        tabla_destino = nombre_archivo.replace('.csv', '')
        table_ref = f"{project_id}.{dataset_id}.{tabla_destino}"

        try:
            tabla = client_bq.get_table(table_ref)
            df_bq = client_bq.list_rows(tabla).to_dataframe()

            # Limpieza para hash consistente
            df_bq = limpiar_columnas_numericas(df_bq)
            df_bq = manejar_columnas_especiales(df_bq)
            df_bq = limpiar_fechas(df_bq)
            df_bq = limpiar_enteros(df_bq)
            df_bq["fila_hash"] = hash_filas(df_bq)

            nuevos = df[~df["fila_hash"].isin(df_bq["fila_hash"])]

        except NotFound:
            print(f"ℹ️ Tabla nueva: {tabla_destino}")
            nuevos = df.copy()

        if nuevos.empty:
            print(f"🔁 {tabla_destino} ya está actualizada.")
        else:
            nuevos = nuevos.drop(columns=["fila_hash"])
            job_config = bigquery.LoadJobConfig(write_disposition='WRITE_APPEND', autodetect=True)
            job = client_bq.load_table_from_dataframe(nuevos, table_ref, job_config=job_config)
            job.result()
            print(f"✅ Filas nuevas insertadas: {len(nuevos)}")

    except Exception as e:
        print(f"❌ Error al procesar {nombre_archivo}: {e}")

# 🎯 Trigger de Cloud Storage (GEN2 - background function)
@functions_framework.cloud_event
def main(cloud_event):
    data = cloud_event.data
    archivo_subido = data['name']
    if archivo_subido.endswith('.csv') and 'prueba/' in archivo_subido:
        nombre_archivo = archivo_subido.split('/')[-1]
        procesar_archivo(nombre_archivo)
    else:
        print("⚠️ Archivo ignorado:", archivo_subido)


