import streamlit as st
import datetime
import random

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

# Clase Task
class Task:
    def __init__(self, title, description, deadline):
        self.id = random.randint(1000, 9999)
        self.title = title
        self.description = description
        self.deadline = deadline
        self.created_at = datetime.datetime.now()
        self.status = "open"
        self.priority = None
        self.category = None
        self.auto_assign_priority()
        self.categorize_task()
        
    def auto_assign_priority(self):
        content = (self.title + " " + self.description).lower()
        analysis = nlp.analyze_text(content)
        self.priority = analysis["priority"]
    
    def categorize_task(self):
        content = (self.title + " " + self.description).lower()
        analysis = nlp.analyze_text(content)
        self.category = analysis["category"]

# Datos de ejemplo
sample_users = {
    "manager@company.com": {"name": "John Manager", "role": "manager"},
    "dev@company.com": {"name": "Alice Developer", "role": "developer"},
    "marketing@company.com": {"name": "Carol Marketer", "role": "marketing"}
}

sample_tasks = [
    Task("Fix login bug", "Critical bug preventing users from logging in", "2023-12-15"),
    Task("Create holiday campaign", "Design Christmas marketing campaign", "2023-11-30"),
    Task("Update API documentation", "Document new endpoints for v2 API", "2023-12-10")
]

# Configuración de Streamlit
st.set_page_config(
    page_title="TaskFlow Demo",
    page_icon="✅",
    layout="wide"
)

# Diseño de la aplicación
def main():
    st.title("TaskFlow - Sistema de Gestión de Tareas Inteligente")
    st.caption("Demo online del sistema de gestión de tareas con priorización automática")
    
    # Sección de autenticación
    with st.sidebar:
        st.header("Inicio de Sesión")
        email = st.text_input("Email", value="manager@company.com")
        password = st.text_input("Contraseña", type="password", value="securepass123")
        
        if st.button("Ingresar"):
            if email in sample_users:
                st.session_state.user = email
                st.success(f"Bienvenido, {sample_users[email]['name']}!")
            else:
                st.error("Credenciales inválidas")
    
    # Si el usuario está autenticado
    if 'user' in st.session_state:
        user = st.session_state.user
        user_data = sample_users[user]
        
        # Dashboard principal
        st.subheader(f"Panel de Control - {user_data['name']}")
        
        # Métricas
        col1, col2, col3 = st.columns(3)
        col1.metric("Tareas Totales", len(sample_tasks))
        col2.metric("Tareas Abiertas", sum(1 for t in sample_tasks if t.status == "open"))
        col3.metric("Tareas Completadas", sum(1 for t in sample_tasks if t.status == "completed"))
        
        # Crear nueva tarea
        with st.expander("➕ Crear Nueva Tarea"):
            with st.form("new_task_form"):
                title = st.text_input("Título de la tarea")
                description = st.text_area("Descripción")
                deadline = st.date_input("Fecha límite")
                
                if st.form_submit_button("Crear Tarea"):
                    if title and description:
                        new_task = Task(title, description, deadline.strftime("%Y-%m-%d"))
                        sample_tasks.append(new_task)
                        st.success("Tarea creada exitosamente!")
                    else:
                        st.error("Título y descripción son requeridos")
        
        # Lista de tareas
        st.subheader("Tus Tareas")
        
        for task in sample_tasks:
            with st.container():
                priority_color = {
                    "high": "#ff4b4b",
                    "medium": "#ffa700",
                    "low": "#0f9d58"
                }.get(task.priority, "#9e9e9e")
                
                col1, col2 = st.columns([0.8, 0.2])
                with col1:
                    st.markdown(f"**{task.title}**")
                    st.caption(f"🔖 Categoría: {task.category.capitalize()}")
                    st.caption(f"📅 Fecha límite: {task.deadline}")
                    st.write(task.description)
                
                with col2:
                    st.markdown(
                        f'<span style="color:{priority_color}; font-weight:bold">'
                        f'⬤ {task.priority.capitalize()}</span>', 
                        unsafe_allow_html=True
                    )
                    status = st.selectbox(
                        "Estado",
                        ["open", "in_progress", "completed"],
                        index=["open", "in_progress", "completed"].index(task.status),
                        key=f"status_{task.id}",
                        label_visibility="collapsed"
                    )
                    task.status = status
                
                st.divider()
    
    # Información para usuarios no autenticados
    else:
        st.info("Por favor inicia sesión para acceder al sistema")
        st.image("https://images.unsplash.com/photo-1506784983877-45594efa4cbe?auto=format&fit=crop&q=80", 
                caption="Sistema de gestión de tareas inteligente")
        
        st.subheader("Características Principales")
        col1, col2, col3 = st.columns(3)
        col1.markdown("""
        **📊 Priorización Automática**  
        Clasifica tareas por urgencia usando NLP
        """)
        col2.markdown("""
        **👥 Asignación Inteligente**  
        Distribuye tareas según habilidades del equipo
        """)
        col3.markdown("""
        **📈 Dashboard Interactivo**  
        Visualiza el progreso en tiempo real
        """)
        
        st.subheader("Credenciales de Prueba")
        st.table({
            "Rol": ["Gerente", "Desarrollador", "Marketing"],
            "Email": ["manager@company.com", "dev@company.com", "marketing@company.com"],
            "Contraseña": ["securepass123", "developerpass", "marketingpass"]
        })

if __name__ == "__main__":
    main()
