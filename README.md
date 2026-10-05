# Task Manager

Aplicación web para gestionar tareas personales. Permite crear, visualizar y completar tareas, filtrarlas por estado y ver estadísticas de progreso.

## Funcionalidades

- Ver el listado de tareas existentes.
- Crear nuevas tareas con título y descripción opcional.
- Marcar tareas como completadas.
- Filtrar tareas por estado: todas, pendientes, completadas.
- Consultar estadísticas: total de tareas, completadas, pendientes y porcentaje de avance.

## Requisitos

- Python 3.11 o superior.
- Git.

## Configuración del entorno

### macOS / Linux

```bash
# 1. Clonar el repositorio
git clone <url-del-repositorio>
cd task-manager

# 2. Crear el entorno virtual
python3 -m venv .venv

# 3. Activar el entorno virtual
source .venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Iniciar la aplicación
uvicorn app.main:app --reload
```

### Windows (PowerShell)

```powershell
# 1. Clonar el repositorio
git clone <url-del-repositorio>
cd task-manager

# 2. Crear el entorno virtual
python -m venv .venv

# 3. Activar el entorno virtual
.venv\Scripts\Activate.ps1

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Iniciar la aplicación
uvicorn app.main:app --reload
```

> **Nota para Windows:** si PowerShell bloquea la ejecución de scripts, ejecuta primero:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## Acceso

Una vez iniciada, la aplicación estará disponible en: [http://localhost:8000](http://localhost:8000)

## Estructura del proyecto

```
app/
├── main.py          # Aplicación FastAPI y definición de rutas
├── models.py        # Modelos de datos (Pydantic)
├── services.py      # Lógica de negocio
├── database.py      # Persistencia en archivo JSON
├── templates/
│   └── index.html   # Interfaz de usuario (Jinja2)
└── static/
    ├── styles.css   # Estilos
    └── app.js       # Comportamiento del cliente

data/
└── tasks.json       # Almacenamiento persistente de tareas
```

## Tecnologías utilizadas

| Componente   | Tecnología              |
|--------------|-------------------------|
| Backend      | Python 3.11 + FastAPI   |
| Servidor     | Uvicorn                 |
| Templates    | Jinja2                  |
| Frontend     | HTML + CSS + JS vanilla |
| Persistencia | JSON (archivo local)    |
