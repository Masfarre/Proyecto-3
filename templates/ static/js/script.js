document.addEventListener('DOMContentLoaded', () => {
    // Funcionalidad para cambiar tema oscuro/claro
    const themeToggle = document.createElement('button');
    themeToggle.textContent = '🌓 Toggle Theme';
    themeToggle.style.position = 'fixed';
    themeToggle.style.bottom = '20px';
    themeToggle.style.right = '20px';
    themeToggle.style.zIndex = '1000';
    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
    });
    document.body.appendChild(themeToggle);
    
    // Añadir clase dark-mode al body si el usuario prefiere modo oscuro
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.body.classList.add('dark-mode');
    }
});
