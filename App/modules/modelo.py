import streamlit as st
import pandas as pd
import joblib

@st.cache_resource
def cargar_modelo():
    return joblib.load('App/modelo_entrenado_xgb.pkl')

modelo = cargar_modelo()

def predecir_rendimiento(df):
    columnas_entrada = [
        'Hours_Studied', 'Attendance', 'Parental_Involvement',
        'Access_to_Resources', 'Extracurricular_Activities', 'Sleep_Hours',
        'Motivation_Level', 'Internet_Access', 'Tutoring_Sessions',
        'Family_Income', 'Teacher_Quality', 'School_Type',
        'Learning_Disabilities', 'Parental_Education_Level', 'Distance_from_Home'
    ]

    mapeo_columnas = {
        'Horas de estudio': 'Hours_Studied',
        'Porcentaje Asistencias': 'Attendance',
        'Participación de los padres': 'Parental_Involvement',
        'Acceso a recursos': 'Access_to_Resources',
        'Actividades Extracurriculares': 'Extracurricular_Activities',
        'Horas de sueño': 'Sleep_Hours',
        'Nivel de motivación': 'Motivation_Level',
        'Acceso a internet': 'Internet_Access',
        'Sesiones de tutoria': 'Tutoring_Sessions',
        'Ingresos familiares': 'Family_Income',
        'Calidad docente': 'Teacher_Quality',
        'Tipo escuela origen': 'School_Type',
        'Discapacidad Cognitiva': 'Learning_Disabilities',
        'Educación parental': 'Parental_Education_Level',
        'Distancia de casa': 'Distance_from_Home'
    }

    ordinal_maps = {
        'Parental_Involvement': {'Bajo': 0, 'Medio': 50, 'Alto': 100},
        'Access_to_Resources': {'Bajo': 0, 'Medio': 50, 'Alto': 100},
        'Motivation_Level': {'Bajo': 0, 'Medio': 50, 'Alto': 100},
        'Extracurricular_Activities': {'No': 0, 'Si': 100},
        'Internet_Access': {'No': 0, 'Si': 100},
        'Family_Income': {'Bajo': 0, 'Medio': 50, 'Alto': 100},
        'Teacher_Quality': {'Bajo': 0, 'Medio': 50, 'Alto': 100},
        'School_Type': {'Publica': 25, 'Privada': 75},
        'Learning_Disabilities': {'No': 100, 'Si': 0},
        'Parental_Education_Level': {'Secundaria completa': 25, 'Bachiller': 50, 'Titulado': 100},
        'Distance_from_Home': {'Lejos': 0, 'Moderado': 50, 'Cerca': 100}
    }

    df = df.rename(columns=mapeo_columnas)
    df = df.drop(columns=[col for col in ['Id Estudiante', 'Nombres', 'Apellidos'] if col in df.columns], errors='ignore')

    for col, mapping in ordinal_maps.items():
        if col in df.columns:
            df[col] = df[col].map(mapping)

    predicciones = modelo.predict(df[columnas_entrada])
    df['Rendimiento_Predicho'] = predicciones


    # Categorizar el nivel de riesgo
    def categorizar(valor):
        if valor < 33:
            return "🔴 Alto"
        elif valor < 66.6:
            return "🟡 Medio"
        else:
            return "🟢 Bajo"
    
    df['Nivel de Riesgo'] = df['Rendimiento_Predicho'].apply(categorizar)
    return df
