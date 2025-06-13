import streamlit as st

# Configuración inicial (debe ser lo primero)
st.set_page_config(page_title="AcademicProfessor", layout="wide")

# Importar vistas
from modules.ui import (
    mostrar_sidebar,
    vista_inicio,
    vista_estudiantes,
    vista_predicciones,
    vista_analisis,
    vista_detalle_estudiante,
    vista_estudiante_manual
)

# Inicializar estado al inicio
if "pagina" not in st.session_state:
    st.session_state.pagina = "Inicio"

# Mostrar menú lateral
menu_seleccionado = mostrar_sidebar()

# Si se elige algo del menú, actualizar el estado de navegación
if st.session_state.pagina != "Detalle":  # Evita que el menú sobrescriba la redirección interna
    st.session_state.pagina = menu_seleccionado

# Leer página actual desde session_state
pagina_actual = st.session_state.get("pagina", "Inicio")

# Navegar a la vista correspondiente
if pagina_actual == "Inicio":
    vista_inicio()
elif pagina_actual == "Estudiantes":
    vista_estudiantes()
elif pagina_actual == "Predicciones":
    vista_predicciones()
elif pagina_actual == "Análisis":
    vista_analisis()
elif pagina_actual == "Detalle":
    vista_detalle_estudiante()
elif pagina_actual == "Estudiante Manual":
    vista_estudiante_manual()
