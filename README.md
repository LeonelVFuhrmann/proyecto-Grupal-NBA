# 🏀 Análisis de Datos NBA – Proyecto Final | Equipo 1

Este repositorio contiene el desarrollo de nuestro proyecto grupal, centrado en el análisis y visualización de datos de la NBA. El objetivo principal fue extraer valor de distintas fuentes de datos relacionadas al rendimiento de equipos y jugadores para construir visualizaciones interactivas que faciliten la toma de decisiones.

---


## 📥 Descarga de Datos Crudos

Debido a limitaciones de tamaño, los datos originales no están almacenados directamente en este repositorio. En su lugar, podés descargar los datos crudos desde la carpeta compartida en Google Drive:

**Nota:** Es importante colocar los datos descargados dentro de la carpeta `Data/Data Cruda` para que los notebooks funcionen correctamente con las rutas relativas configuradas.

[📂 Carpeta de Google Drive][![Google Drive](https://img.shields.io/badge/Google%20Drive-Download-blue?logo=google-drive&style=flat-square)](https://drive.google.com/drive/folders/1cpyqh4gJj8WTLE0hibV6B5b3XWL0TMEG)

## 📁 Estructura del Repositorio

```
PF_NBA_EQUIPO1/
├── Data/
│   ├── Data Cruda/       # Contiene un link a Drive para descargar los datos originales
│   └── Data Limpia/           # Datos limpios y transformados listos para análisis
│
├── Notebooks/            # Notebooks individuales de cada integrante (limpieza y transformación)
│
├── Documentación/
│   ├── Identidad/        # Elementos visuales del proyecto
│   ├── diccionario_datos.pdf
│   └── informe_proyecto.pdf
│
├── requirements.txt      # Dependencias del entorno
└── README.md             # Documentación principal del proyecto
```

---

## 🎯 Objetivos del Proyecto

- Recolectar, limpiar y transformar datasets relacionados a la NBA.
- Desarrollar un modelo de procesamiento de datos reproducible.
- Subir los datos procesados a Google Cloud Platform.
- Crear dashboards interactivos en Power BI.
- Documentar el flujo completo de trabajo para futuras implementaciones.

---

## ⚙️ Instalación del Entorno de Trabajo

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/pazcaminoDA/PF_NBA_EQUIPO1.git
   cd PF_NBA_EQUIPO1
   ```

2. (Opcional) Crear un entorno virtual:

   ```bash
   python -m venv env
   source env/bin/activate   # Linux/MacOS
   .\env\Scripts\activate    # Windows
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🔄 Flujo de Trabajo

## 🚀 Instructivo para encarar el proyecto

A continuación se detallan los pasos recomendados para trabajar con este proyecto de forma ordenada y eficiente:

1. **Descargar los datos crudos**  
   Descargá los datasets originales desde la carpeta de Google Drive y colocá los archivos dentro de `Data/Data Cruda` (carpetas creadas localmente al clonar el repositorio).

2. **Preparar el entorno de trabajo**  
   Abrí Visual Studio Code y cargá la carpeta del proyecto para trabajar con los notebooks.  
   Instalar las dependencias listadas en `requirements.txt`.

3. **Limpieza y transformación de datos**  
   Ejecutá y modificá los notebooks en la carpeta `Notebooks` para procesar los datos crudos y obtener datasets limpios.  
   Los archivos transformados deben guardarse en la carpeta `Data/Data limpia`.

4. **Subida a Google Cloud Platform**  
   Los datasets limpios se cargan a Google Cloud Storage o BigQuery para centralizar la información y facilitar la integración con herramientas de visualización.

5. **Visualización en Power BI**  
   Conectá Power BI a las fuentes de datos en la nube para crear dashboards dinámicos e interactivos que permitan analizar la información de manera efectiva.

6. **Automatización del pipeline**  
   Actualmente se está trabajando en la automatización de los procesos de extracción, transformación y carga (ETL) para optimizar y agilizar las actualizaciones periódicas de datos.  
   Esto incluye la programación de scripts y la integración con herramientas como cron, Airflow o Cloud Functions.


---

## 📈 Herramientas y Tecnologías Utilizadas

- **Python**: pandas, numpy, seaborn, matplotlib  
- **Jupyter Notebooks**  
- **Google Cloud Platform**: Cloud Storage, BigQuery  
- **Power BI**  
- **Visual Studio Code**  
- **Git & GitHub** para control de versiones

---

## 🤖 Automatización del Pipeline (En Desarrollo)

Estamos trabajando en la implementación de un pipeline automático para:

- Extraer, transformar y cargar los datos con scripts programados.
- Automatizar la carga de datos limpios a GCP (Storage o BigQuery).
- Ejecutar procesos mediante `cron`, Airflow o Cloud Functions.
- Garantizar trazabilidad y repetibilidad del proceso de ETL.

---

## 📊 Visualizaciones en Power BI

El producto final incluye dashboards conectados directamente a la nube. Estas visualizaciones permiten:

- Monitorear KPIs relevantes
- Acceso dinámico a la información
- Toma de decisiones basada en datos

---

## 👥 Integrantes del Equipo

- Sofía Echeverria  
- Leonel Fuhrmann  
- Maria Paz Camino  
- Agustín Brandt


