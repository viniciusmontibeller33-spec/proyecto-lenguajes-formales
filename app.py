import streamlit as st

st.set_page_config(
    page_title="StringLab | Lenguajes Formales y Autómatas",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar estilos visuales
try:
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except Exception:
    pass

st.title("🔬 StringLab — Plataforma Educativa")
st.subheader("Lenguajes Formales y Autómatas • Tema 4: Análisis de Cadenas y Teoría de Números")
st.markdown("---")

st.markdown("""
**StringLab** es una aplicación interactiva diseñada para explorar la relación matemática y computacional entre 
el **análisis de secuencias**, la **teoría elemental de números** y los **autómatas finitos deterministas (AFD)**.
""")

# Tarjetas principales de los módulos
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card-box" style="border-left: 5px solid #0284c7;">
        <h3>⚙️ Módulo C: Simulador de Autómatas Finitos</h3>
        <p><strong>Módulo Desarrollado por Vini:</strong> Simulación interactiva paso a paso de Autómatas Finitos Deterministas (AFD) con grafos dinámicos en Graphviz, resaltado de transiciones, cinta de lectura y tablas formales de estados.</p>
        <span class="badge-edu" style="background-color: #0284c7; color: white;">🌟 Módulo Principal de Vini</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-box">
        <h3>🔤 Módulo A: Analizador de Cadenas</h3>
        <p>Inspección de secuencias de texto: conteo léxico, histogramas de frecuencia, verificación de palíndromos y localización de subcadenas.</p>
        <span class="badge-edu">Asignado a: Sergio</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-box">
        <h3>🔢 Módulo B: Laboratorio de Teoría de Números</h3>
        <p>Exploración algorítmica: test de primalidad, Algoritmo de Euclides (MCD), cálculo de MCM y aritmética modular.</p>
        <span class="badge-edu">Asignado a: José</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-box">
        <h3>🔐 Módulo D: Cifrado Educativo</h3>
        <p>Aplicación de la aritmética modular en el cifrado y descifrado César, con demostración del anillo cíclico ℤ₂₆.</p>
        <span class="badge-edu">Asignado a: José</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Guía para Visual Studio Code
with st.expander("💻 ¿Cómo ejecutar este proyecto en Visual Studio Code?", expanded=True):
    st.markdown("""
    1. Abre la carpeta del proyecto en **Visual Studio Code**.
    2. Asegúrate de tener seleccionada la rama `vini` en la barra inferior de Git.
    3. Presiona **`F5`** o ve al panel de **Ejecutar y depurar** y selecciona **"Ejecutar StringLab (Streamlit)"**.
    4. O desde la terminal integrada de VS Code (PowerShell / Bash), ejecuta:
       ```bash
       streamlit run app.py
       ```
    5. La aplicación abrirá automáticamente tu navegador en `http://localhost:8501`.
    """)

st.info("👈 **Para comenzar a probar el simulador de autómatas:** Abre el menú de la barra lateral izquierda y haz clic en **'3 Simulador de automatas'**.")
