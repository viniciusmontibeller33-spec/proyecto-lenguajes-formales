import streamlit as st
import pandas as pd
from logic.cadenas import analizar_cadena, verificar_palindromo, buscar_subcadena

st.set_page_config(page_title="Analizador de Cadenas | StringLab", layout="wide")

# Cargar estilos visuales
try:
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except Exception:
    pass

st.title("Analizador de Cadenas")
st.caption("Herramienta interactiva para inspección de texto, conteo sintáctico, detección paso a paso de palíndromos y localización de patrones.")
st.markdown("---")

texto_ejemplo = "La ruta natural nos dio otro camino"
entrada = st.text_area("Escribe o pega una cadena de texto para analizar:", value=texto_ejemplo, height=100)

if entrada:
    datos = analizar_cadena(entrada)
    
    st.subheader("Métricas de la Cadena")
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
        st.subheader("Verificación de Palíndromo Paso a Paso")
        res_pal = verificar_palindromo(entrada)
        
        if not res_pal["evaluable"]:
            st.info("La cadena no contiene letras ni dígitos evaluables para determinar si es palíndromo.")
        elif res_pal["es_palindromo"]:
            st.success("La cadena es un palíndromo.")
        else:
            st.warning("La cadena NO es un palíndromo.")
            
        st.markdown(f"""
        * **Texto normalizado:** `{res_pal['normalizado']}`
        * **Texto invertido:** `{res_pal['invertido']}`
        * *Nota pedagógica:* Se ignoran mayúsculas, espacios y signos de puntuación según la definición formal.
        """)
        
        if res_pal["pasos"]:
            st.write("**Procedimiento de comparación paso a paso (dos punteros):**")
            df_pasos_pal = pd.DataFrame(res_pal["pasos"])
            st.dataframe(df_pasos_pal, hide_index=True, use_container_width=True)
        
    with col_der:
        st.subheader("Búsqueda de Subcadenas")
        subcadena = st.text_input("Ingresa una subcadena a buscar:", value="ruta")
        if subcadena:
            res_busqueda = buscar_subcadena(entrada, subcadena)
            posiciones = res_busqueda.get("posiciones", [])
            ocurrencias = res_busqueda.get("ocurrencias", len(posiciones))
            comparaciones = res_busqueda.get("comparaciones", 0)
            
            if ocurrencias > 0:
                st.success(f"Se encontraron {ocurrencias} coincidencia(s) en las posiciones (índice 0): {posiciones}")
                st.caption(f"Comparaciones de caracteres realizadas: {comparaciones}")
                
                texto_resaltado = entrada.replace(subcadena, f"**:blue-background[{subcadena}]**")
                st.markdown(f"**Vista con coincidencias:**\n\n{texto_resaltado}")
            else:
                st.info(f"No se encontró la subcadena '{subcadena}' en el texto. (Se realizaron {comparaciones} comparaciones).")

    st.markdown("---")
    st.subheader("Frecuencia de Caracteres")
    df_freq = pd.DataFrame(list(datos["frecuencias"].items()), columns=["Carácter", "Frecuencia"]).sort_values(by="Frecuencia", ascending=False)
    st.dataframe(df_freq, hide_index=True, use_container_width=True)

st.markdown("---")
with st.expander("¿Qué conceptos estoy aprendiendo en este módulo?"):
    st.markdown("""
    * **Alfabetos ($\Sigma$) y Cadenas ($w$):** En ciencias de la computación, un texto es una palabra formal compuesta por una secuencia finita de símbolos tomados de un alfabeto.
    * **Longitud de una cadena ($|w|$):** Representa el número de símbolos. Aquí exploramos la diferencia entre considerar o no el símbolo blanco/espacio.
    * **Búsqueda de Patrones y Complejidad:** La búsqueda directa recorre la cadena comprobando coincidencias carácter a carácter, con una cota de comparaciones de $O(|w| \\cdot |v|)$.
    * **Simetría e Inversión ($w^R$):** Un palíndromo formal cumple que $w = w^R$, base fundamental de los lenguajes libres de contexto (Chomsky Tipo 2) no reconocibles por autómatas finitos debido a que requieren memoria infinita tipo pila.
    """)
