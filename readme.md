# Dashboard de Insights — Backend + Frontend

### Integrantes

* **SERGIO ANDRÉS BEJARANO RODRÍGUEZ**
* **GERONIMO MARTINEZ NUÑEZ**
* **LAURA DANIELA RODRÍGUEZ SÁNCHEZ**
* **JESUS ALFONSO PINZON VEGA**

---

## Descripción General

Esta aplicación muestra un **dashboard** con estadísticas extraídas desde:

* **PostgreSQL (Supabase)**
* **Pinecone**

El backend está construido con **FastAPI** bajo una arquitectura sencilla tipo **MVC**, con:

* Capa de configuración (`core/config.py`)
* Capa de conexión a base de datos (`core/database.py`)
* Capa de repositorios (`repositories/postgres.py`)
* Capa de servicios (`services/analyticsService.py`)
* Capa de rutas (`routers/analyticsRouter.py`)

El frontend es completamente estático (`/static`) y utiliza **Chart.js** para graficar:

* Distribución de tipos de caso
* Tasa de éxito
* Tendencia temporal por fecha
* Indicadores KPI globales

Se consulta la API con `/api/insightsPostgres`.

---

## 🗂️ Estructura del Proyecto

```
.
│   .env
├───app
│   │   main.py
│   ├───core
│   │   ├── config.py
│   │   └── database.py
│   ├───repositories
│   │   └── postgres.py
│   ├───routers
│   │   └── analyticsRouter.py
│   └───services
│       └── analyticsService.py
└───static
        index.html
        script.js
        styles.css
```

---

## Configuración del entorno

El archivo `.env` almacena las credenciales necesarias para conectarse a:

* **Supabase / PostgreSQL**
* **Pinecone**
* **Google API (si se necesita en el futuro)**

Formato esperado:

```
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_URI=

PINECONE_API_KEY=

GOOGLE_API_KEY=
```

El backend lee `POSTGRES_URI` mediante `core/config.py`.

---

## 🚀 Cómo ejecutar el backend

### 1. Instalar dependencias

```
pip install -r requirements.txt
```

### 2. Activar entorno virtual

```
source .venv/bin/activate
```

### 3. Ejecutar el servidor FastAPI

```
uvicorn app.main:app --reload
```

El backend correrá en:

```
http://127.0.0.1:8000
```

Ruta principal del API:

```
GET /api/insightsPostgres
```

---

##  Frontend

El frontend vive en `/static` y se sirve automáticamente por FastAPI:

```
http://127.0.0.1:8000/static/index.html
```

Incluye:

* **KPI Cards**
* **Filtros dinámicos (todos, éxitos, fallos)**
* **Charts: Doughnut, Pie, Line**
* **Botón flotante para refrescar datos**
* **Animaciones y efectos con CSS puro**

---

## Tecnologías usadas

* **Python 3.13**
* **FastAPI**
* **psycopg**
* **Chart.js**
* **HTML, CSS, JS vanila**