import streamlit as st
import pandas as pd
from logic.cifrado import cifrar_cesar_paso_a_paso, descifrar_cesar_paso_a_paso, obtener_alfabeto_desplazado, ALFABETO

st.set_page_config(page_title="Módulo D: Cifrado Educativo | StringLab", page_icon="🔐", layout="wide")

st.title("🔐 Módulo D: Cifrado Educativo (César Modular)")
st.markdown("**Responsable:** José (`rama: jose`)")
st.caption("Aprende cómo la aritmética modular transforma caracteres en el cifrado clásico de sustitución.")
st.markdown("---")

st.warning("⚠️ **Nota didáctica:** Este módulo utiliza el alfabeto estándar de 26 letras en inglés ($A-Z$, sin letra Ñ) para ejemplificar la aritmética módulo 26. Los signos y espacios se conservan intactos. Este método es estrictamente educativo y no debe usarse para proteger información sensible.")

modo = st.radio("Selecciona la operación:", ["Cifrar Mensaje", "Descifrar Mensaje"], horizontal=True)

col_txt, col_k = st.columns([3, 1])
mensaje_input = col_txt.text_input("Mensaje a procesar:", value="HOLA MUNDO" if modo == "Cifrar Mensaje" else "KROD PXQGR")
clave_k = col_k.slider("Clave de desplazamiento (K):", min_value=1, max_value=25, value=3)

# Visualización comparativa de alfabetos
st.subheader("🔤 Mapeo de Alfabetos")
orig, desp = obtener_alfabeto_desplazado(clave_k)

df_alf = pd.DataFrame({
    "Original": list(orig),
    "Posición (P)": list(range(26)),
    "Desplazado (+K)": list(desp)
})
st.dataframe(df_alf.T, use_container_width=True)

st.markdown("---")
st.subheader("⚙️ Procesamiento y Procedimiento Paso a Paso")

if modo == "Cifrar Mensaje":
    resultado, pasos = cifrar_cesar_paso_a_paso(mensaje_input, clave_k)
    st.success(f"**Texto Cifrado:** `{resultado}`")
    st.markdown(f"**Fórmula aplicada:** $C = (P + {clave_k}) \\pmod{{26}}$")
else:
    resultado, pasos = descifrar_cesar_paso_a_paso(mensaje_input, clave_k)
    st.success(f"**Texto Descifrado:** `{resultado}`")
    st.markdown(f"**Fórmula aplicada:** $P = (C - {clave_k}) \\pmod{{26}}$")

if pasos:
    st.write("Tabla de transformaciones carácter por carácter:")
    df_pasos = pd.DataFrame(pasos)
    st.dataframe(df_pasos, hide_index=True, use_container_width=True)

st.markdown("---")
with st.expander("🎓 ¿Qué conceptos estoy aprendiendo en este módulo?"):
    st.markdown("""
    * **Transductores Finitos:** Un cifrado de sustitución puede verse formalmente como una Máquina de Mealy o transductor finito que lee un símbolo de entrada $P$ y emite un símbolo $C$ según una función de salida.
    * **Aritmética en Anillos Finitos ($\mathbb{Z}_{26}$):** Las letras se mapean biyectivamente a números entre $0$ y $25$. La suma y resta modular garantizan que el resultado siempre vuelva a caer dentro del alfabeto (operación cerrada).
    * **Inversibilidad:** El descifrado funciona porque la suma modular tiene un inverso aditivo: $(P + K - K) \equiv P \pmod{26}$.
    """)
