import streamlit as st

st.set_page_config(
    page_title="StringLab | Lenguajes Formales y Autómatas",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar estilos personalizados
with open("assets/styles.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🔬 StringLab")
st.subheader("Laboratorio Educativo de Cadenas, Teoría de Números y Autómatas Finitos")
st.markdown("---")

st.markdown("""
Bienvenido a **StringLab**, una herramienta diseñada para estudiantes de **Lenguajes Formales y Autómatas**.
Aquí podrás experimentar de forma interactiva y visual con conceptos clave de la computación teórica:
análisis de secuencias, operaciones aritmético-modulares y simulación formal de autómatas paso a paso.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card-box">
        <h3>🔤 Módulo A: Analizador de Cadenas</h3>
        <p>Examina cadenas de texto: conteo de símbolos, frecuencias, detección de palíndromos y búsqueda de subcadenas con resaltado visual.</p>
        <span class="badge-edu">Responsable: Sergio</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-box">
        <h3>⚙️ Módulo C: Simulador de Autómatas</h3>
        <p>Simulación interactiva paso a paso de Autómatas Finitos Deterministas (AFD) con grafos de estados y tablas de transición.</p>
        <span class="badge-edu">Responsable: Vini</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-box">
        <h3>🔢 Módulo B: Teoría de Números</h3>
        <p>Aprende paso a paso: números primos, Algoritmo de Euclides (MCD), MCM y el funcionamiento de la aritmética modular.</p>
        <span class="badge-edu">Responsable: José</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-box">
        <h3>🔐 Módulo D: Cifrado Educativo</h3>
        <p>Descubre cómo la aritmética modular se aplica en el cifrado clásico de César mediante transformaciones carácter por carácter.</p>
        <span class="badge-edu">Responsable: José</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.info("💡 **Cómo empezar:** Selecciona uno de los módulos en la barra lateral izquierda para comenzar tu experimentación.")
