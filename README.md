
# 🏀 Proyecto Grupal NBA Analytics

Este repositorio corresponde a un **fork** del proyecto grupal de análisis de datos de la NBA.  
Mi participación estuvo enfocada en la **gestión de bases de datos, limpieza y análisis de datos**, y desarrollo de dashboards en Power BI.

## ⚡ Mi rol en el proyecto

1. **Creación, seguridad y automatización de la base de datos en BigQuery**  
   - BigQuery fue una herramienta **nueva para mí**, por lo que adaptarme y configurar la base de datos de manera eficiente fue un desafío importante.  
   - Configuré permisos, creé tablas y automatizaciones para la carga de datos crudos al entorno de análisis.  

2. **Limpieza y análisis de archivos crudos**  
   - Trabajé con los datasets originales, limpiando inconsistencias y normalizando columnas para su posterior análisis.  
   - Preparé tablas listas para generar métricas y visualizaciones.  

3. **Análisis final en Power BI**  
   - Participé en la creación de **una página del dashboard**, integrando visualizaciones y métricas relevantes para mostrar insights sobre jugadores, equipos y desempeño por temporada.  

## 🛠️ Tecnologías utilizadas
- **BigQuery** → gestión y automatización de bases de datos.  
- **Python (pandas, numpy)** → limpieza y análisis de archivos crudos.  
- **Power BI** → desarrollo de dashboards y visualizaciones interactivas.  
- **SQL** → consultas avanzadas para extracción y transformación de datos.  
# 🏀 Análisis de Datos NBA – Proyecto Final | Equipo 1

Este repositorio contiene el desarrollo de nuestro proyecto grupal, centrado en el análisis y visualización de datos de la NBA. El objetivo principal fue extraer valor de distintas fuentes de datos relacionadas al rendimiento de equipos y jugadores para construir visualizaciones interactivas que faciliten la toma de decisiones.

---


## 📥 Descarga de Datos Crudos

Debido a limitaciones de tamaño, los datos originales no están almacenados directamente en este repositorio. En su lugar, podés descargar los datos crudos desde la carpeta compartida en Google Drive:

**Nota:** Es importante colocar los datos descargados dentro de la carpeta `Data/Data Cruda` para que los notebooks funcionen correctamente con las rutas relativas configuradas.

[📂 Data Cruda][![Google Drive](https://img.shields.io/badge/Google%20Drive-Download-blue?logo=google-drive&style=flat-square)](https://drive.google.com/drive/folders/1cpyqh4gJj8WTLE0hibV6B5b3XWL0TMEG)


También podés descargar los archivos ya limpios y colocarlos en su carpeta correspondiente (Data Limpia), en caso de no querer hacer el proceso.

[📂 Data Limpia][![Google Drive](https://img.shields.io/badge/Google%20Drive-Download-blue?logo=google-drive&style=flat-square)](https://drive.google.com/drive/folders/19Ap8VtPO3Ph3U8Cnk0MvJFhxqOdBxvkl)      

## 📁 Estructura del Repositorio

```
PF_NBA_EQUIPO1/
├── Data/
│   ├── Data Cruda/       # Contiene un link a Drive para descargar los datos originales
│   └── Data Limpia/           # Datos limpios y transformados listos para análisis
│
├── Notebooks/            # Notebooks individuales de cada integrante (limpieza y transformación)
│
├── cloud_functions/        # Funciones para automatizar procesos en la nube
│ 
│ 
├── Documentación/
│   ├── Identidad/        # Elementos visuales del proyecto
│   ├── diccionario_datos.pdf
│   └── informe_proyecto.pdf
│   └── Presentación Sprint 1
│
├── requirements.txt      # Dependencias del entorno
└── README.md             # Documentación principal del proyecto
└── Dashboard             # Dashboard
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
   Se descargan los datasets originales desde la carpeta de Google Drive y colocá los archivos dentro de `Data/Data Cruda` (carpetas creadas localmente al clonar el repositorio).

2. **Preparar el entorno de trabajo**  
   Se abre Visual Studio Code y se carga la carpeta del proyecto para trabajar con los notebooks.  
   Instalar las dependencias listadas en `requirements.txt`.

3. **Limpieza y transformación de datos**  
   Ejecutamos y modificamos los notebooks en la carpeta `Notebooks` para procesar los datos crudos y obtener datasets limpios.  
   Los archivos transformados deben guardarse en la carpeta `Data/Data limpia`.

4. **Subida a Google Cloud Platform**  
   Los datasets limpios se cargan a Google Cloud Storage o BigQuery para centralizar la información y facilitar la integración con herramientas de visualización.

5. **Visualización en Power BI**  
   Conectamos Power BI a las fuentes de datos en la nube para crear dashboards dinámicos e interactivos que permitan analizar la información de manera efectiva.

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
- **Trello** 

---

## 🤖 Automatización del Pipeline

Automatización de Ingesta y Limpieza con Cloud Functions
Este proyecto utiliza una función en Google Cloud para automatizar la ingesta y limpieza de datos:

Cuando se sube un archivo .csv a la carpeta prueba/ del bucket pf-nba-csv,
la función ingest_clean.py se dispara automáticamente.

El archivo se descarga, se limpia y se comparan los datos con BigQuery para insertar sólo los nuevos registros.

Esto garantiza que la base de datos se mantenga actualizada sin duplicados ni datos sucios.

### 🎥 Video de la Automatización

[Ver video de demostración](https://drive.google.com/file/d/1qmPmSfjTDkAnyyMHrdup64EZsplPh62l/view?usp=sharing)  


---

## 📊 Dashboard en Power BI

[Link al Dashboard](https://drive.google.com/drive/folders/13ZotAZ88YXn-ilOpU4XvyrulicVRVNPu)

El **dashboard interactivo** desarrollado en **Power BI** es el producto final del análisis, diseñado para **facilitar la exploración y comparación** de jugadores y equipos de la NBA.  
Está conectado a datos alojados en **Google BigQuery** y cuenta con **tres vistas principales**:

---

### 1️⃣ Performance Equipo
**🎯 Objetivo:** Analizar métricas globales y comparativas entre equipos.

**🔹 Elementos clave:**
- 📌 **Tarjetas con KPIs:** puntos, victorias, derrotas, faltas.
- 🗂 **Filtros** por ubicación, tipo de lanzamiento y temporada.
- 📈 **Gráfico de precisión ofensiva**.
- 🛡 **Treemap de solidez defensiva**.
- 📊 **Línea de tendencia** sobre puntos generados por errores forzados.

---

### 2️⃣ Perfil Jugador
**🎯 Objetivo:** Explorar las características físicas y demográficas de cada jugador.

**🔹 Elementos clave:**
- 📌 Tarjetas con **edad, altura, peso, equipo actual, posición y año de draft**.
- 📅 **Clasificación etaria:**  
  *Joven Talento*, *En Crecimiento*, *Pico de Rendimiento*, *Veterano*, *Veterano Senior*.
- 🏁 **Indicador tipo gauge** que ubica al jugador en su segmento de edad.
- 🕸 **Radar chart** con métricas físicas: alcance de brazos, agilidad en pista, salto vertical, ancho de mano y alcance parado (normalizadas).
- 🌍 **Mapa de nacionalidad** para identificar jugadores internacionales y mercados potenciales.

---

### 3️⃣ Performance Jugador
**🎯 Objetivo:** Evaluar el rendimiento individual y relacionarlo con factores como salario y grupo etario.

**🔹 Elementos clave:**
- 📌 KPIs de **partidos jugados, tiros intentados, victorias y aciertos**.
- 📊 **Tabs de estadísticas:** asistencias, pérdidas, bloqueos, puntos y robos.
- 🏆 **Gráfico Top 5** por estadística seleccionada.
- ⚖ **Scatter plot “Eficiencia vs Salario”** segmentado por grupo etario.

---

💡 **Nota:** El dashboard fue diseñado con un enfoque en **interactividad y segmentación dinámica**, permitiendo explorar información **por jugador, equipo, temporada y grupo etario en tiempo real**.

---



## 👥 Integrantes del Equipo

- Sofía Echeverria  
- Leonel Fuhrmann  
- Maria Paz Camino  
- Agustín Brandt


