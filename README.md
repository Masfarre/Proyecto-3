# TaskFlow: Intelligent Task Management System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

TaskFlow es un sistema de gestión de tareas inteligente que utiliza procesamiento de lenguaje natural (NLP) para optimizar la asignación y priorización de actividades en equipos empresariales. Este proyecto fue desarrollado como parte de la transformación digital de nuestra organización.

## 🚀 Motivación

En entornos empresariales dinámicos, equipos distribuidos enfrentan desafíos constantes en:
- Priorización manual de tareas
- Asignación subóptima de recursos
- Pérdida de tiempo en coordinación
- Falta de visibilidad del progreso

TaskFlow automatiza estos procesos usando inteligencia artificial para:
1. **Clasificar automáticamente** tareas por urgencia e impacto
2. **Asignar inteligentemente** recursos basado en habilidades y carga de trabajo
3. **Generar reportes predictivos** de cumplimiento
4. **Integrar sin problemas** con herramientas empresariales existentes

## 💻 Instalación y Despliegue

### Requisitos Previos
- Python 3.9+
- PostgreSQL 12+
- Redis (para colas de tareas)

### Opción 1: Despliegue Local
```bash
# Clonar repositorio
git clone https://github.com/tu-org/taskflow.git
cd taskflow

# Configurar entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno (crear .env)
cp .env.example .env
# Editar .env con tus credenciales

# Ejecutar migraciones
python manage.py migrate

# Iniciar servidor
python manage.py runserver
