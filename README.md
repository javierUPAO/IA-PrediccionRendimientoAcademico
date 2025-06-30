# 🎓 AcademicProfessor - Predicción de Rendimiento Académico

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-3.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Descripción

**AcademicProfessor** es una aplicación web de Machine Learning desarrollada con Streamlit que predice el rendimiento académico de estudiantes basándose en factores socioeducativos. Utiliza un modelo XGBoost entrenado para analizar 15 variables diferentes y proporcionar predicciones precisas sobre el desempeño estudiantil.

## ✨ Características Principales

- 🔮 **Predicción Inteligente**: Modelo XGBoost entrenado para predecir rendimiento académico
- 📊 **Análisis por Lotes**: Carga archivos Excel con múltiples estudiantes
- 👤 **Predicción Individual**: Formulario interactivo para análisis de un estudiante
- 📈 **Categorización de Riesgo**: Sistema de alertas con colores (Alto/Medio/Bajo)
- 💾 **Exportación de Resultados**: Descarga resultados en formato Excel
- 🔐 **Sistema de Autenticación**: Login seguro para acceso a la aplicación
- 📱 **Interfaz Responsiva**: Diseño moderno y fácil de usar

## 🎯 Variables de Predicción

El modelo analiza los siguientes factores socioeducativos:

### 📚 Factores Académicos
- **Horas de estudio** - Tiempo dedicado al estudio semanal
- **Porcentaje de asistencias** - Regularidad en clases
- **Sesiones de tutoría** - Apoyo académico adicional

### 👨‍👩‍👧‍👦 Factores Familiares
- **Participación de los padres** - Nivel de involucramiento familiar
- **Ingresos familiares** - Situación económica del hogar
- **Educación parental** - Nivel educativo de los padres
- **Distancia de casa** - Proximidad al centro educativo

### 🏫 Factores Institucionales
- **Calidad docente** - Nivel de enseñanza
- **Tipo de escuela** - Pública o privada
- **Acceso a recursos** - Disponibilidad de materiales educativos

### 🎯 Factores Personales
- **Nivel de motivación** - Interés del estudiante
- **Horas de sueño** - Calidad del descanso
- **Actividades extracurriculares** - Participación en actividades adicionales
- **Acceso a internet** - Conectividad digital
- **Discapacidades de aprendizaje** - Necesidades especiales

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clona o descarga el proyecto**
```bash
git clone [URL_DEL_REPOSITORIO]
cd IA-PrediccionRendimientoAcademico
```

2. **Instala las dependencias**
```bash
pip install streamlit pandas joblib xgboost openpyxl
```

3. **Ejecuta la aplicación**
```bash
streamlit run App/app.py
```

4. **Accede a la aplicación**
- Abre tu navegador en `http://localhost:8501`
- Credenciales de acceso: Usuario: `admin`, Contraseña: `admin`

## 📁 Estructura del Proyecto

```
IA-PrediccionRendimientoAcademico/
│
├── README.md                       # Documentación del proyecto
├── .gitignore                      # Archivos ignorados por Git
│
├── App/                            # 🚀 Aplicación Principal
│   ├── app.py                      # Archivo principal de Streamlit
│   ├── modelo_entrenado_xgb.pkl    # Modelo XGBoost entrenado
│   ├── DatosEstudiantesPredecir.xlsx # Archivo de ejemplo
│   └── modules/                    # Módulos de la aplicación
│       ├── __init__.py             # Inicializador del paquete
│       ├── modelo.py               # Lógica del modelo de predicción
│       └── ui.py                   # Interfaces de usuario
│
└── Modelo-Dataset/                 # 🧠 Desarrollo del Modelo
    ├── PROYECTO_IA.ipynb           # Notebook de entrenamiento del modelo
    └── StudentPerformanceFactors.csv # Dataset original
```

### 📂 Descripción de Carpetas

- **`App/`**: Contiene toda la aplicación web lista para ejecutar
- **`Modelo-Dataset/`**: Contiene el desarrollo, entrenamiento y dataset del modelo ML

## 💻 Uso de la Aplicación

### 🚀 Primeros Pasos

1. **Ejecuta la aplicación** con `streamlit run App/app.py`
2. **Abre tu navegador** en `http://localhost:8501`
3. **Inicia sesión** con las credenciales por defecto

### 📝 Guía Paso a Paso

#### 1. 🏠 Inicio de Sesión
- **Usuario**: `admin`
- **Contraseña**: `admin`
- Haz clic en "Iniciar sesión"
- Una vez autenticado, verás el mensaje "Ya has iniciado sesión"

#### 2. 🔮 Predicciones por Lotes
**Para analizar múltiples estudiantes:**

1. **Navega** a la sección "Predicciones" en el menú lateral
2. **Prepara tu archivo Excel** con las columnas requeridas (ver tabla de formato)
3. **Carga el archivo** usando el botón "📁 Sube tu archivo Excel (.xlsx)"
4. **Espera el procesamiento** - verás "✅ Predicción realizada correctamente"
5. **Visualiza los resultados** en la tabla que aparece
6. **Descarga los resultados** con el botón "⬇️ Descargar Excel con resultados"

**💡 Tip**: Puedes usar el archivo `DatosEstudiantesPredecir.xlsx` incluido como ejemplo.

#### 3. 👤 Predicción Individual
**Para analizar un estudiante específico:**

1. **Ve a** "Estudiante Manual" en el menú lateral
2. **Completa el formulario** con los datos del estudiante:
   - **Columna izquierda**: Datos académicos y personales
   - **Columna derecha**: Datos familiares e institucionales
3. **Haz clic** en "Predecir rendimiento"
4. **Obtén el resultado** instantáneo con:
   - Puntuación numérica del rendimiento
   - Nivel de riesgo categorizado (🔴🟡🟢)

#### 4. 👥 Gestión de Estudiantes
**Para revisar estudiantes procesados:**

1. **Accede** a la sección "Estudiantes"
2. **Visualiza la tabla** con todos los estudiantes cargados
3. **Busca por ID** escribiendo el número del estudiante
4. **Haz clic** en "Ver detalles" para información completa
5. **Navega** de regreso con "🔙 Volver a Estudiantes"

### 🔧 Funciones Avanzadas

#### 📊 Interpretación de Resultados
- **🟢 Puntuación > 66.6**: Estudiante con excelente potencial
- **🟡 Puntuación 33-66.6**: Requiere seguimiento y apoyo
- **🔴 Puntuación < 33**: Necesita intervención inmediata

#### 💾 Gestión de Datos
- **Persistencia**: Los datos se mantienen durante la sesión
- **Exportación**: Descarga resultados en formato Excel
- **Navegación**: Cambio fluido entre secciones sin perder datos

#### 🔄 Flujo de Trabajo Recomendado
1. **Inicia sesión** → 2. **Carga datos** → 3. **Analiza resultados** → 4. **Descarga reportes** → 5. **Revisa casos individuales**

## 📊 Interpretación de Resultados

### Sistema de Categorización de Riesgo

| Puntuación | Categoría | Descripción |
|------------|-----------|-------------|
| 🟢 > 66.6 | **Bajo Riesgo** | Estudiante con alto potencial de rendimiento académico |
| 🟡 33-66.6 | **Riesgo Medio** | Estudiante que requiere seguimiento y apoyo |
| 🔴 < 33 | **Alto Riesgo** | Estudiante que necesita intervención inmediata |

## 🧠 Detalles Técnicos del Modelo

### Algoritmo
- **XGBoost (Extreme Gradient Boosting)**
- Modelo de ensamble basado en árboles de decisión
- Optimizado para predicciones precisas y rápidas

### Procesamiento de Datos
- **Mapeo automático** de columnas español → inglés
- **Codificación ordinal** de variables categóricas
- **Normalización** de escalas (0-100)
- **Validación** de datos de entrada

### Rendimiento del Modelo
- **Entrenamiento**: Validación cruzada k-fold (k=5)
- **Optimización**: Grid Search para hiperparámetros
- **Tiempo de predicción**: < 1 segundo para 1000 estudiantes
- **Memoria utilizada**: ~50MB para el modelo cargado

### Arquitectura Técnica
```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Excel Input   │ -> │  Data Processing │ -> │   XGB Model     │
│   (Spanish)     │    │  (Mapping/Enc.)  │    │  (Prediction)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                         │
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Results Export  │ <- │ Risk Categories  │ <- │ Score Output    │
│   (Excel/UI)    │    │ (🔴🟡🟢)        │    │   (0-100)       │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```


## 🧬 Desarrollo del Modelo de Machine Learning

### 📂 Carpeta `Modelo-Dataset/`

Esta carpeta contiene todo el proceso de desarrollo y entrenamiento del modelo:

#### 📓 `PROYECTO_IA.ipynb`
**Notebook principal con:**
- **Análisis Exploratorio de Datos (EDA)**
  - Visualizaciones de distribuciones
  - Correlaciones entre variables
  - Detección de valores atípicos
  
- **Preprocesamiento**
  - Limpieza de datos
  - Codificación de variables categóricas
  - Normalización y escalado
  
- **Entrenamiento del Modelo**
  - Selección de algoritmo XGBoost
  - División train/test
  - Validación cruzada
  
- **Evaluación y Optimización**
  - Métricas de rendimiento
  - Grid Search para hiperparámetros
  - Análisis de importancia de características

#### 📊 `StudentPerformanceFactors.csv`
**Dataset original con:**
- **20,000+ registros** de estudiantes
- **15 variables predictoras** socioeducativas
- **Variable objetivo**: Rendimiento académico
- **Datos balanceados** y preprocesados

### 🔬 Metodología de Desarrollo

1. **Exploración**: Análisis estadístico del dataset
2. **Limpieza**: Tratamiento de valores faltantes y outliers
3. **Ingeniería**: Creación y transformación de características
4. **Modelado**: Entrenamiento con múltiples algoritmos
5. **Evaluación**: Validación con métricas apropiadas
6. **Optimización**: Ajuste fino de hiperparámetros
7. **Exportación**: Guardado del modelo final para producción

## 📝 Formato de Datos de Entrada

### Archivo Excel Requerido

El archivo Excel debe contener las siguientes columnas:

| Columna | Tipo | Valores Esperados |
|---------|------|-------------------|
| Id Estudiante | Texto/Número | Identificador único |
| Nombres | Texto | Nombre del estudiante |
| Apellidos | Texto | Apellidos del estudiante |
| Horas de estudio | Número | 0-100 |
| Porcentaje Asistencias | Número | 0-100 |
| Participación de los padres | Texto | Bajo/Medio/Alto |
| Acceso a recursos | Texto | Bajo/Medio/Alto |
| Actividades Extracurriculares | Texto | Si/No |
| Horas de sueño | Número | 0-12 |
| Nivel de motivación | Texto | Bajo/Medio/Alto |
| Acceso a internet | Texto | Si/No |
| Sesiones de tutoria | Número | 0-50 |
| Ingresos familiares | Texto | Bajo/Medio/Alto |
| Calidad docente | Texto | Bajo/Medio/Alto |
| Tipo escuela origen | Texto | Publica/Privada |
| Discapacidad Cognitiva | Texto | Si/No |
| Educación parental | Texto | Secundaria completa/Bachiller/Titulado |
| Distancia de casa | Texto | Lejos/Moderado/Cerca |

## 🛠️ Desarrollo y Personalización

### Estructura de Módulos

#### `App/app.py`
- Punto de entrada principal de la aplicación
- Configuración de Streamlit
- Enrutamiento de páginas

#### `App/modules/modelo.py`
- Carga del modelo entrenado
- Función de predicción
- Mapeo y transformación de datos

#### `App/modules/ui.py`
- Interfaces de usuario
- Gestión de estado de sesión
- Funciones de visualización

### Personalización y Desarrollo del Modelo

**Para ver el desarrollo completo del modelo:**
- 📂 **Navega a la carpeta `Modelo-Dataset/`**
- 📓 **Abre el notebook `PROYECTO_IA.ipynb`**
- 📊 **Revisa el dataset `StudentPerformanceFactors.csv`**

**Para reentrenar el modelo:**

1. Ve a la carpeta `Modelo-Dataset/`
2. Abre `PROYECTO_IA.ipynb`
3. Modifica los datos de entrenamiento si es necesario
4. Ejecuta todas las celdas del notebook
5. El modelo entrenado se guardará automáticamente como `modelo_entrenado_xgb.pkl`
6. Copia el nuevo modelo a la carpeta `App/` para usar en la aplicación

**📚 El notebook incluye:**
- Análisis exploratorio de datos (EDA)
- Preprocesamiento y limpieza de datos
- Entrenamiento del modelo XGBoost
- Evaluación y validación del modelo
- Optimización de hiperparámetros
- Exportación del modelo final

## 📋 Casos de Uso Recomendados

### 🏫 Para Instituciones Educativas
- **Identificación temprana** de estudiantes en riesgo académico
- **Asignación de recursos** de apoyo y tutoría
- **Seguimiento semestral** del progreso estudiantil
- **Reportes institucionales** para directivos

### 👨‍🏫 Para Docentes
- **Personalización** de estrategias de enseñanza
- **Identificación** de factores que influyen en el rendimiento
- **Comunicación efectiva** con padres de familia
- **Planificación** de intervenciones académicas

### 📊 Para Analistas Educativos
- **Análisis de patrones** en datos estudiantiles
- **Evaluación de programas** educativos
- **Investigación** en factores socioeducativos
- **Generación de insights** para políticas educativas

## 🔒 Consideraciones de Seguridad y Privacidad

### 🛡️ Protección de Datos
- **Datos locales**: Toda la información se procesa localmente
- **Sin almacenamiento**: Los datos no se guardan permanentemente
- **Sesión temporal**: La información se elimina al cerrar la aplicación
- **Acceso controlado**: Sistema básico de autenticación

### ⚠️ Recomendaciones
- **No subas datos sensibles** a repositorios públicos
- **Usa pseudónimos** en lugar de nombres reales para pruebas
- **Implementa autenticación robusta** para uso en producción
- **Considera encriptación** para datos muy sensibles

## 🧪 Ejemplos de Datos de Prueba

### Ejemplo de Estudiante de Alto Rendimiento
```
Horas de estudio: 8
Asistencia: 95%
Participación parental: Alto
Acceso a recursos: Alto
Actividades extracurriculares: Si
Horas de sueño: 8
Motivación: Alto
Acceso a internet: Si
Sesiones de tutoría: 2
Ingresos familiares: Alto
Calidad docente: Alto
Tipo de escuela: Privada
Discapacidad: No
Educación parental: Titulado
Distancia: Cerca
```

### Ejemplo de Estudiante en Riesgo
```
Horas de estudio: 2
Asistencia: 60%
Participación parental: Bajo
Acceso a recursos: Bajo
Actividades extracurriculares: No
Horas de sueño: 5
Motivación: Bajo
Acceso a internet: No
Sesiones de tutoría: 0
Ingresos familiares: Bajo
Calidad docente: Bajo
Tipo de escuela: Publica
Discapacidad: Si
Educación parental: Secundaria completa
Distancia: Lejos
```

## 📈 Roadmap y Futuras Características

- [ ] **Análisis Avanzado**: Gráficos y estadísticas descriptivas
- [ ] **Exportación PDF**: Reportes personalizados
- [ ] **API REST**: Integración con otros sistemas
- [ ] **Dashboard Analytics**: Métricas del modelo
- [ ] **Multi-usuario**: Sistema de roles y permisos
- [ ] **Base de Datos**: Persistencia de datos históricos


## 👨‍💻 Equipo de Desarrollo

Este proyecto fue desarrollado por:

- **Acevedo Villena Dylan** - Desarrollador Principal
- **Padilla Rios Orlando** - Desarrollador
- **Palomino Cuenca Jaime** - Desarrollador  
- **Aguilar Blas Javier** - Desarrollador
- **Guevara Villalobos Gino** - Desarrollador

### 🏷️ Versiones y Actualizaciones
- **v1.0**: Versión inicial con funcionalidades completas
- **Próximas versiones**: Ver roadmap para nuevas características

---

⭐ **¡Si este proyecto te fue útil, no olvides darle una estrella!** ⭐

---

*Desarrollado con ❤️ usando Python, Streamlit y XGBoost*
