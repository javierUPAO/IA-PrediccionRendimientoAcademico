import streamlit as st
import pandas as pd
from io import BytesIO
from .modelo import predecir_rendimiento

# Estado global para guardar datos entre páginas
def init_session_state():
    for key in ["df_original", "df_predicho", "df_completo", "logged_in", "pagina", "id_detalle"]:
        if key not in st.session_state:
            st.session_state[key] = None
init_session_state()

def mostrar_sidebar():
    return st.sidebar.radio("Menú", ["Inicio", "Estudiantes", "Predicciones", "Análisis"])

def vista_inicio():
    st.title("🏠 Bienvenido a AcademicProfessor")
    st.write("Esta herramienta predice el rendimiento académico de estudiantes a partir de datos socioeducativos.\n\nPara comenzar, inicia sesión y sube un archivo Excel desde la pestaña 'Predicciones'.")

    if not st.session_state.logged_in:
        with st.form("login"):
            usuario = st.text_input("Usuario")
            password = st.text_input("Contraseña", type="password")
            iniciar = st.form_submit_button("Iniciar sesión")
        if iniciar:
            if usuario == "admin" and password == "admin":
                st.session_state.logged_in = True
                st.success("Inicio de sesión exitoso.")
            else:
                st.error("Credenciales incorrectas.")
    else:
        st.success("Ya has iniciado sesión.")

def vista_estudiantes():
    st.title("👥 Estudiantes")

    if 'df_completo' in st.session_state and st.session_state.df_completo is not None:
        df = st.session_state.df_completo.copy()
        df['Predicción'] = df['Nivel de Riesgo']

        columnas = [
            'Id Estudiante', 'Nombres', 'Apellidos',
            'Nivel de motivación', 'Porcentaje Asistencias', 'Predicción'
        ]
        columnas_disponibles = [col for col in columnas if col in df.columns]
        df_vista = df[columnas_disponibles]

        st.dataframe(df_vista, use_container_width=True)

        st.markdown("### 🔍 Escribe el ID de un estudiante para ver más detalles:")
        opciones = df['Id Estudiante'].astype(str).unique().tolist()

        seleccion = st.text_input("ID del estudiante:", value=st.session_state.id_detalle if st.session_state.id_detalle else "", key="entrada_estudiante")

        if st.button("Ver detalles"):
            if seleccion in opciones:
                st.session_state.pagina = "Detalle"
                st.session_state.id_detalle = seleccion
                st.rerun()
            else:
                st.warning("ID no encontrado en los datos.")
    else:
        st.warning("No hay datos procesados. Ve a 'Predicciones' y carga un archivo.")

def vista_predicciones():
    st.title("🔮 Predicción de Rendimiento Académico")
    archivo = st.file_uploader("📁 Sube tu archivo Excel (.xlsx)", type=["xlsx"])

    if archivo:
        try:
            df = pd.read_excel(archivo)
            st.session_state.df_original = df
            df_predicho = predecir_rendimiento(df.copy())
            st.session_state.df_predicho = df_predicho

            # 🔁 Fusión de datos
            df_completo = df.copy()
            df_completo['Rendimiento_Predicho'] = df_predicho['Rendimiento_Predicho']
            df_completo['Nivel de Riesgo'] = df_predicho['Nivel de Riesgo']
            st.session_state.df_completo = df_completo

            st.success("✅ Predicción realizada correctamente.")
        except Exception as e:
            st.error(f"❌ Error: {e}")

    if st.session_state.df_predicho is not None:
        st.subheader("📊 Resultados")
        st.dataframe(st.session_state.df_predicho.head(15))

        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            st.session_state.df_predicho.to_excel(writer, index=False)
        output.seek(0)

        st.download_button(
            label="⬇️ Descargar Excel con resultados",
            data=output,
            file_name="resultados_prediccion.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.info("Carga un archivo para ver los resultados aquí.")

def vista_analisis():
    st.title("📈 Análisis de Datos")
    st.info("Aquí podrás visualizar análisis descriptivos y gráficos. (Próximamente)")

def vista_detalle_estudiante():
    st.title("📄 Detalle del Estudiante")

    id_buscar = st.session_state.get("id_detalle")

    if id_buscar and 'df_completo' in st.session_state and st.session_state.df_completo is not None:
        df = st.session_state.df_completo
        estudiante = df[df["Id Estudiante"].astype(str) == str(id_buscar)]

        if not estudiante.empty:
            st.write("Información del estudiante:")
            st.dataframe(estudiante.T, use_container_width=True)
        else:
            st.warning("Estudiante no encontrado.")

        if st.button("🔙 Volver a Estudiantes"):
            st.session_state.pagina = "Estudiantes"
            st.rerun()
    else:
        st.warning("ID no especificado o datos no disponibles.")
