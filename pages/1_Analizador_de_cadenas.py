import streamlit as st
import pandas as pd
from logic.cadenas import analizar_cadena, es_palindromo, buscar_subcadena

st.set_page_config(page_title="Módulo A: Analizador de Cadenas | StringLab", page_icon="🔤", layout="wide")

st.title("🔤 Módulo A: Analizador de Cadenas")
st.markdown("**Responsable:** Sergio (`rama: sergio`)")
st.caption("Herramienta interactiva para inspección de texto, conteo sintáctico, detección de palíndromos y localización de patrones.")
st.markdown("---")

texto_ejemplo = "La ruta natural nos dio otro camino"
entrada = st.text_area("Escribe o pega una cadena de texto para analizar:", value=texto_ejemplo, height=100)

if entrada:
    datos = analizar_cadena(entrada)
    
    st.subheader("📊 Métricas de la Cadena")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Caracteres (con espacios)", datos["total_con_espacios"])
    c2.metric("Total sin Espacios", datos["total_sin_espacios"])
    c3.metric("Letras", datos["letras"])
    c4.metric("Dígitos", datos["digitos"])
    
    c5, c6, c7, c8 = st.columns(4)
    c5.metric("Vocales", datos["vocales"])
    c6.metric("Consonantes", datos["consonantes"])
    c7.metric("Espacios", datos["espacios"])
    c8.metric("Símbolos", datos["simbolos"])
    
    st.markdown("---")
    col_izq, col_der = st.columns(2)
    
    with col_izq:
        st.subheader("🔄 Verificación de Palíndromo")
        es_pal, limpio, invertido = es_palindromo(entrada)
        if es_pal:
            st.success("✅ ¡La cadena es un palíndromo!")
        else:
            st.warning("❌ La cadena NO es un palíndromo.")
            
        st.markdown(f"""
        * **Texto normalizado:** `{limpio}`
        * **Texto invertido:** `{invertido}`
        * *Nota:* Para la comprobación de palíndromos se ignoran mayúsculas, espacios, signos de puntuación y tildes.
        """)
        
    with col_der:
        st.subheader("🔍 Búsqueda de Subcadenas")
        subcadena = st.text_input("Ingresa una subcadena a buscar:", value="ruta")
        if subcadena:
            coincidencias = buscar_subcadena(entrada, subcadena)
            if coincidencias:
                st.success(f"Se encontraron **{len(coincidencias)}** coincidencia(s) en las posiciones (índice 0): `{coincidencias}`")
                
                # Resaltado visual básico
                texto_resaltado = entrada.replace(subcadena, f"**:blue-background[{subcadena}]**")
                st.markdown(f"**Vista con coincidencias:**\n\n{texto_resaltado}")
            else:
                st.info(f"No se encontró la subcadena '{subcadena}' en el texto.")

    st.markdown("---")
    st.subheader("📈 Frecuencia de Caracteres")
    df_freq = pd.DataFrame(list(datos["frecuencias"].items()), columns=["Carácter", "Frecuencia"]).sort_values(by="Frecuencia", ascending=False)
    st.dataframe(df_freq, hide_index=True, use_container_width=True)

st.markdown("---")
with st.expander("🎓 ¿Qué conceptos estoy aprendiendo en este módulo?"):
    st.markdown("""
    * **Alfabetos ($\Sigma$) y Cadenas ($w$):** En ciencias de la computación, un texto es una palabra formal compuesta por una secuencia finita de símbolos tomados de un alfabeto.
    * **Longitud de una cadena ($|w|$):** Representa el número de símbolos. Aquí exploramos la diferencia entre considerar o no el símbolo blanco/espacio.
    * **Prefijos, Sufijos y Subcadenas:** La búsqueda de patrones busca localizar si una subcadena $v$ existe tal que $w = xvy$.
    * **Simetría e Inversión ($w^R$):** Un palíndromo formal cumple que $w = w^R$, base de lenguajes libres de contexto generados por gramáticas con reglas como $S \to aSa \mid bSb \mid \epsilon$.
    """)
