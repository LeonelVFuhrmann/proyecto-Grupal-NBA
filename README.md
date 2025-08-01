# 🏀 Análisis de Datos NBA – Proyecto Final | Equipo 1

Este repositorio contiene el desarrollo de nuestro proyecto grupal, centrado en el análisis y visualización de datos de la NBA. El objetivo principal fue extraer valor de distintas fuentes de datos relacionadas al rendimiento de equipos y jugadores para construir visualizaciones interactivas que faciliten la toma de decisiones.

---

## 📁 Estructura del Repositorio

PF_NBA_EQUIPO1/
│
├── Data/
│ ├── Data Cruda/ # Contiene un link de una carpeta de drive donde se descargan los archivos crudos
│ └── limpia/ # Datos limpios y transformados listos para análisis
│
├── Notebooks/ # Notebooks que contienen las transformaciones hechas por cada uno de los integrantes, en carpetas separadas 
│
│
├── Documentación/
│ ├── Identidad/ # Elementos visuales e identidad del proyecto
│ ├── diccionario_datos.pdf
│ └── informe_proyecto.pdf
│
├── requirements.txt # Lista de dependencias del entorno
└── README.md # Documentación principal del proyecto

---

## 🎯 Objetivos del Proyecto

- Recolectar, limpiar y transformar datasets relacionados a la NBA.
- Desarrollar un modelo de procesamiento de datos reproducible.
- Subir los datos procesados a la nube mediante Google Cloud Platform.
- Crear dashboards interactivos en Power BI para facilitar el análisis exploratorio y descriptivo.
- Documentar el flujo completo de trabajo para futuras implementaciones.

---

## ⚙️ Instalación del Entorno de Trabajo

1. Clonar el repositorio:

   git clone https://github.com/pazcaminoDA/PF_NBA_EQUIPO1.git
   cd PF_NBA_EQUIPO1

Crear entorno virtual (opcional):

python -m venv env
source env/bin/activate   # Linux/MacOS
.\env\Scripts\activate    # Windows

Instalar las dependencias:
pip install -r requirements.txt


🔄 Flujo de Trabajo
Obtención de datos: los datasets fueron descargados desde distintas fuentes y almacenados en Drive.

División de tareas: cada integrante trabajó en la limpieza y transformación de datasets específicos utilizando Jupyter Notebooks.

Consolidación: los archivos limpios fueron centralizados y subidos a una instancia de almacenamiento en Google Cloud Platform (GCP).

Visualización: conexión de los datos en GCP con Power BI para desarrollar visualizaciones interactivas.

📈 Herramientas y Tecnologías Utilizadas
Python (pandas, numpy, seaborn, matplotlib)

Jupyter Notebooks

Google Cloud Platform (Cloud Storage, BigQuery)

Power BI

Git & GitHub para control de versiones

Visual Studio Code

🤖 Automatización de Ingesta de Datos (En Desarrollo)
Actualmente se encuentra en desarrollo una solución de automatización del pipeline de ingesta y procesamiento de datos. El objetivo es:

Implementar scripts programados para extraer y transformar los datasets originales.

Automatizar la carga de datos limpios a Google Cloud Storage o BigQuery.

Utilizar herramientas como cron, Airflow o Cloud Functions para ejecutar procesos en intervalos definidos.

Garantizar la trazabilidad y repetibilidad del proceso de ETL.

📊 Visualizaciones en Power BI

El producto final incluye dashboards conectados directamente a los datos en la nube, permitiendo una visualización dinámica, actualizada y centrada en KPIs relevantes.



👥 Integrantes del Equipo
Sofía Echeverria 

Leonel Fuhrmann

Maria Paz Camino

Agustín Brandt

