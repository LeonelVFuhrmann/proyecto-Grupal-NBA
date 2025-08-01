# 🏀 Análisis de Datos NBA – Proyecto Final | Equipo 1

Este repositorio contiene el desarrollo de nuestro proyecto grupal, centrado en el análisis y visualización de datos de la NBA. El objetivo principal fue extraer valor de distintas fuentes de datos relacionadas al rendimiento de equipos y jugadores para construir visualizaciones interactivas que faciliten la toma de decisiones.

---

## 📁 Estructura del Repositorio

```
PF_NBA_EQUIPO1/
├── Data/
│   ├── Data Cruda/       # Contiene un link a Drive para descargar los datos originales
│   └── limpia/           # Datos limpios y transformados listos para análisis
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

1. **Obtención de Datos:**  
   Los datasets fueron descargados desde distintas fuentes y almacenados en una carpeta compartida de Google Drive.

2. **Limpieza y Transformación:**  
   Cada integrante trabajó en distintos datasets utilizando Jupyter Notebooks.

3. **Consolidación:**  
   Los archivos limpios se centralizaron y subieron a Google Cloud Platform.

4. **Visualización:**  
   Se conectaron los datos desde GCP a Power BI para construir dashboards interactivos.

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


