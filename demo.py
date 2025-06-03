import gradio as gr
import datetime
import random
import pandas as pd

# Clase SimpleNLP (alternativa a spaCy)
class SimpleNLP:
    def __init__(self):
        pass
    
    def analyze_text(self, text):
        text_lower = text.lower()
        return {
            "priority": self._detect_priority(text_lower),
            "category": self._detect_category(text_lower)
        }
    
    def _detect_priority(self, text):
        high_terms = ["urgent", "critical", "important", "asap", "blocker"]
        medium_terms = ["medium", "moderate", "soon", "normal"]
        
        if any(term in text for term in high_terms):
            return "high"
        elif any(term in text for term in medium_terms):
            return "medium"
        return "low"
    
    def _detect_category(self, text):
        categories = {
            "development": ["bug", "feature", "code", "api", "database"],
            "marketing": ["campaign", "seo", "content", "social media"],
            "design": ["design", "ui", "ux", "mockup"]
        }
        
        for category, terms in categories.items():
            if any(term in text for term in terms):
                return category
        return "general"

nlp = SimpleNLP()

# Base de datos en memoria para la demo
tasks = []
task_id_counter = 1

# Crear algunas tareas de ejemplo
def create_sample_tasks():
    global tasks, task_id_counter
    sample_tasks = [
        ("Fix login bug", "Critical bug preventing users from logging in", "2023-12-15"),
        ("Create holiday campaign", "Design Christmas marketing campaign", "2023-11-30"),
        ("Update API documentation", "Document new endpoints for v2 API", "2023-12-10")
    ]
    
    for title, desc, deadline in sample_tasks:
        tasks.append({
            "id": task_id_counter,
            "title": title,
            "description": desc,
            "deadline": deadline,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "priority": "",
            "category": "",
            "status": "open"
        })
        task_id_counter += 1
        analyze_task(task_id_counter - 1)

# Analizar una tarea para asignar prioridad y categoría
def analyze_task(task_id):
    global tasks
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        content = task["title"] + " " + task["description"]
        analysis = nlp.analyze_text(content)
        task["priority"] = analysis["priority"]
        task["category"] = analysis["category"]
    return task

# Crear una nueva tarea
def create_task(title, description, deadline):
    global tasks, task_id_counter
    if not title or not description:
        return "Error: Título y descripción son requeridos", None
    
    new_task = {
        "id": task_id_counter,
        "title": title,
        "description": description,
        "deadline": deadline,
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "priority": "",
        "category": "",
        "status": "open"
    }
    
    tasks.append(new_task)
    task_id_counter += 1
    
    # Analizar la nueva tarea
    analyze_task(new_task["id"])
    
    return "✅ Tarea creada exitosamente!", get_task_table()

# Obtener tabla de tareas para mostrar
def get_task_table():
    if not tasks:
        return pd.DataFrame(columns=["ID", "Título", "Prioridad", "Categoría", "Fecha Límite", "Estado"])
    
    data = []
    for task in tasks:
        data.append([
            task["id"],
            task["title"],
            task["priority"].capitalize() if task["priority"] else "Pendiente",
            task["category"].capitalize() if task["category"] else "Pendiente",
            task["deadline"],
            task["status"].replace("_", " ").capitalize()
        ])
    
    return pd.DataFrame(data, columns=["ID", "Título", "Prioridad", "Categoría", "Fecha Límite", "Estado"])

# Actualizar estado de una tarea
def update_task_status(task_id, new_status):
    global tasks
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        task["status"] = new_status
        return "✅ Estado actualizado", get_task_table()
    return "❌ Tarea no encontrada", get_task_table()

# Interfaz de Gradio
with gr.Blocks(title="TaskFlow Demo", theme="soft") as demo:
    gr.Markdown("# 🚀 TaskFlow - Sistema de Gestión de Tareas")
    gr.Markdown("**Priorización automática de tareas usando procesamiento de lenguaje natural**")
    
    # Crear tareas de ejemplo al inicio
    create_sample_tasks()
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("## 📝 Crear Nueva Tarea")
            title = gr.Textbox(label="Título", placeholder="Título de la tarea")
            description = gr.Textbox(label="Descripción", placeholder="Describe la tarea...", lines=3)
            deadline = gr.Textbox(label="Fecha Límite (YYYY-MM-DD)", value=datetime.date.today().strftime("%Y-%m-%d"))
            submit_btn = gr.Button("Crear Tarea", variant="primary")
            result_msg = gr.Label()
        
        with gr.Column(scale=2):
            gr.Markdown("## 📋 Lista de Tareas")
            task_table = gr.Dataframe(
                value=get_task_table(),
                headers=["ID", "Título", "Prioridad", "Categoría", "Fecha Límite", "Estado"],
                datatype=["number", "str", "str", "str", "str", "str"],
                interactive=False
            )
            
            with gr.Row():
                task_id = gr.Number(label="ID de Tarea", precision=0)
                status_dropdown = gr.Dropdown(
                    ["open", "in_progress", "completed"],
                    label="Nuevo Estado",
                    value="open"
                )
                update_btn = gr.Button("Actualizar Estado")
                update_result = gr.Label()
            
            refresh_btn = gr.Button("Actualizar Lista")
    
    # Event handlers
    submit_btn.click(
        create_task, 
        inputs=[title, description, deadline],
        outputs=[result_msg, task_table]
    )
    
    update_btn.click(
        update_task_status,
        inputs=[task_id, status_dropdown],
        outputs=[update_result, task_table]
    )
    
    refresh_btn.click(
        lambda: get_task_table(),
        outputs=task_table
    )
    
    # Ejemplos de uso
    gr.Markdown("## 💡 Ejemplos de Tareas")
    gr.Examples(
        examples=[
            ["Resolver error crítico en producción", "Hay un error que impide el acceso a los usuarios. ¡Urgente!", "2023-11-20"],
            ["Planificar reunión de equipo", "Organizar reunión para revisar progreso del trimestre", "2023-11-25"],
            ["Mejorar diseño de la interfaz", "Rediseñar la página principal para mejor experiencia de usuario", "2023-12-05"]
        ],
        inputs=[title, description, deadline],
        outputs=[result_msg, task_table],
        fn=create_task,
        cache_examples=True
    )
    
    # Explicación del sistema
    with gr.Accordion("ℹ️ Sobre TaskFlow", open=False):
        gr.Markdown("""
        **TaskFlow** es un sistema inteligente de gestión de tareas que utiliza procesamiento de lenguaje natural para:
        - Clasificar automáticamente tareas por prioridad (alta, media, baja)
        - Asignar categorías según el contenido de la tarea
        - Optimizar el flujo de trabajo en equipos
        
        ### Cómo funciona
        1. **Ingresa una tarea** con título y descripción
        2. El sistema **analiza el texto** para determinar prioridad y categoría
        3. **Visualiza y gestiona** tus tareas en el panel
        
        ### Prioridades
        - 🔴 **Alta**: Contiene palabras como 'urgente', 'crítico', 'importante'
        - 🟠 **Media**: Contiene palabras como 'medio', 'moderado', 'pronto'
        - 🟢 **Baja**: Sin palabras clave de prioridad
        
        ### Categorías comunes
        - 💻 Desarrollo: 'bug', 'feature', 'código', 'api'
        - 📣 Marketing: 'campaña', 'seo', 'contenido'
        - 🎨 Diseño: 'diseño', 'ui', 'ux', 'mockup'
        """)

if __name__ == "__main__":
    demo.launch()
