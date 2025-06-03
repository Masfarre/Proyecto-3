# Guía de Instalación para Proyecto-3: TaskFlow

## Requisitos Previos
- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar el repositorio)

## Pasos de Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/Proyecto-3.git
cd Proyecto-3
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install --upgrade pip setuptools wheel

# Instalar dependencias con soluciones para evitar errores comunes
pip install --no-build-isolation --use-pep517 spacy
pip install Flask==2.3.2 gunicorn==20.1.0
```


### 4. Descargar modelo de lenguaje

```bash
python -m spacy download en_core_web_sm
```

### 5. Ejecutar la aplicación

```bash
python app.py
```

### 6. Ejecutar la aplicación

Acceder a la aplicación
Abre tu navegador en: http://localhost:5000

##Credenciales de prueba
-Manager:

--Email: manager@company.com

--Contraseña: securepass123

-Desarrollador:

--Email: dev1@company.com

--Contraseña: developerpass
