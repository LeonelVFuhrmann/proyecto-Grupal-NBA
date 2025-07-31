# PF_NBA_EQUIPO1
Proyecto Final DA Soy Henry
## 📁 Datasets

Los archivos utilizados en este proyecto están disponibles en la siguiente carpeta de Google Drive:

🔗 [Acceder a los datasets](https://drive.google.com/drive/folders/1U8SGNrBMAOR53BKV6Py5srgMV2s_o-rC?usp=drive_link)

# 📊 Proyecto de Ingesta de Datos para Análisis en Power BI

Este repositorio contiene el código y estructura para la limpieza y carga de datasets que serán utilizados en Power BI. El flujo actual incluye limpieza con Python y sus librerías, subida a Google Cloud Platform (GCP), y conexión desde herramientas de visualización.

---

## 🔁 Flujo de trabajo actual

1. 📥 **Obtención de datos**: los archivos `.csv` fueron descargados desde una carpeta compartida de Google Drive.
2. 🧹 **Limpieza**: los datos fueron procesados con Python en Visual Studio Code (`scripts/clean_data.py`).
3. 📤 **Subida de datos limpios**: los archivos procesados fueron subidos nuevamente a Drive.
4. ☁️ **Carga a la nube**: un miembro del equipo los importó a Google Cloud.
5. 📈 **Visualización**: los datos serán utilizados en Power BI para generar reportes.

---


## 🗃️ Datos

Los archivos están disponibles temporalmente en esta carpeta de Google Drive:  
👉 [Carpeta de datasets y notebooks]](https://drive.google.com/drive/folders/1U8SGNrBMAOR53BKV6Py5srgMV2s_o-rC?usp=drive_link

> *Nota: el objetivo es reemplazar este enlace por un flujo automatizado en el futuro.*

---

## 🛠️ Requisitos (para ejecutar scripts)

- Python 3.10+
- Pandas
- Jupyter
- Numpy
- seaborn
- matplotlib
- re
Instalar dependencias:
(apartado a cambiar hoy)

```bash
pip install -r requirements.txt
🚧 Próximos pasos (pendientes)
Automatizar la carga directa desde Python a GCP usando load_data.py

Implementar control de versiones para datasets

Documentar credenciales y variables de entorno con .env.example

Conectar directamente Power BI con Google Cloud (en proceso)

👨‍💻 Equipo
Agustín
Sofia
Paz
Leonel
