import streamlit as st
import pandas as pd
from logic.cifrado import cifrar_cesar_paso_a_paso, descifrar_cesar_paso_a_paso, obtener_alfabeto_desplazado

st.set_page_config(page_title="Cifrado Educativo | StringLab", layout="wide")

# Cargar estilos visuales
try:
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except Exception:
    pass

st.title("Cifrado Educativo (César Modular)")
st.caption("Aprende cómo la aritmética modular transforma caracteres en el cifrado clásico de sustitución.")
st.markdown("---")

st.warning("Nota didáctica: Este módulo utiliza el alfabeto estándar de 26 letras en inglés (A-Z, sin letra Ñ) para ejemplificar la aritmética módulo 26. Los signos y espacios se conservan intactos. Este método es estrictamente educativo y no debe usarse para proteger información sensible.")

# 1. Preservar el mensaje en session_state para que no se reinicie a 'HOLA MUNDO'
if "mensaje_cifrado" not in st.session_state:
    st.session_state.mensaje_cifrado = "HOLA MUNDO"

modo = st.radio(
    "Selecciona la operación:",
    ["Cifrar Mensaje", "Descifrar Mensaje"],
    horizontal=True,
    key="radio_modo_cifrado"
)

col_txt, col_k = st.columns([3, 1])

def on_texto_change():
    st.session_state.mensaje_cifrado = st.session_state.input_texto_cifrado

mensaje_input = col_txt.text_input(
    "Mensaje a procesar:",
    value=st.session_state.mensaje_cifrado,
    key="input_texto_cifrado",
    on_change=on_texto_change
)

# Mantener sincronizado el texto actual
st.session_state.mensaje_cifrado = mensaje_input

clave_k = col_k.slider("Clave de desplazamiento (K):", min_value=1, max_value=25, value=3, key="slider_clave_k")

# Visualización comparativa de alfabetos
st.subheader("Mapeo de Alfabetos")
orig, desp = obtener_alfabeto_desplazado(clave_k)

df_alf = pd.DataFrame({
    "Original": list(orig),
    "Posición (P)": list(range(26)),
    "Desplazado (+K)": list(desp)
})
st.dataframe(df_alf.T, use_container_width=True)

st.markdown("---")
st.subheader("Procesamiento y Procedimiento Paso a Paso")

if modo == "Cifrar Mensaje":
    resultado, pasos = cifrar_cesar_paso_a_paso(mensaje_input, clave_k)
    st.success(f"**Texto Cifrado:** `{resultado}`")
    st.markdown(f"**Fórmula aplicada:** $C = (P + {clave_k}) \\pmod{{26}}$")
else:
    resultado, pasos = descifrar_cesar_paso_a_paso(mensaje_input, clave_k)
    st.success(f"**Texto Descifrado:** `{resultado}`")
    st.markdown(f"**Fórmula aplicada:** $P = (C - {clave_k}) \\pmod{{26}}$")

# Botón utilitario para transferir el resultado de nuevo al campo de texto
col_copiar, _ = st.columns([1, 3])
def transferir_resultado():
    st.session_state.mensaje_cifrado = resultado
    st.session_state.input_texto_cifrado = resultado

col_copiar.button("Copiar resultado al campo de entrada", on_click=transferir_resultado)

if pasos:
    st.write("Tabla de transformaciones carácter por carácter:")
    df_pasos = pd.DataFrame(pasos)
    st.dataframe(df_pasos, hide_index=True, use_container_width=True)

st.markdown("---")
with st.expander("¿Qué conceptos estoy aprendiendo en este módulo?"):
    st.markdown("""
    * **Transductores Finitos:** Un cifrado de sustitución puede verse formalmente como una Máquina de Mealy o transductor finito que lee un símbolo de entrada $P$ y emite un símbolo $C$ según una función de salida.
    * **Aritmética en Anillos Finitos ($\mathbb{Z}_{26}$):** Las letras se mapean biyectivamente a números entre $0$ y $25$. La suma y resta modular garantizan que el resultado siempre vuelva a caer dentro del alfabeto (operación cerrada).
    * **Inversibilidad:** El descifrado funciona porque la suma modular tiene un inverso aditivo: $(P + K - K) \equiv P \pmod{26}$.
    """)
