import streamlit as st

st.set_page_config(
    page_title="StringLab | Lenguajes Formales y Autómatas",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar estilos visuales
try:
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except Exception:
    pass

st.title("StringLab — Plataforma Educativa")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card-box">
        <h3>Analizador de Cadenas</h3>
        <p>Inspección de secuencias de texto: conteo de símbolos, frecuencias de caracteres, verificación paso a paso de palíndromos y localización de subcadenas.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-box">
        <h3>Laboratorio de Teoría de Números</h3>
        <p>Exploración algorítmica: test de primalidad con divisores probados, Algoritmo de Euclides para MCD, cálculo de MCM y propiedades de congruencia modular.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-box">
        <h3>Simulador de Autómatas Finitos</h3>
        <p>Simulación interactiva paso a paso de Autómatas Finitos Deterministas (AFD) con grafos dinámicos en Graphviz, resaltado de transiciones, cinta de lectura y tablas formales de estados.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-box">
        <h3>Cifrado Educativo</h3>
        <p>Aplicación de la aritmética modular en el cifrado y descifrado César, con demostración de transformaciones carácter por carácter en el anillo Z26.</p>
    </div>
    """, unsafe_allow_html=True)
