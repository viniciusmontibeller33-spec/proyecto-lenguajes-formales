import streamlit as st
import pandas as pd
from logic.teoria_numeros import es_primo_paso_a_paso, mcd_euclides_paso_a_paso, mcm_con_explicacion, operacion_modulo_explicada, verificar_congruencia

st.set_page_config(page_title="Módulo B: Teoría de Números | StringLab", layout="wide")

# Cargar estilos visuales
try:
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except Exception:
    pass

st.title("Módulo B: Laboratorio de Teoría de Números")
st.caption("Operaciones fundamentales paso a paso: números primos, Algoritmo de Euclides, MCM y aritmética modular.")
st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["Números Primos", "MCD (Algoritmo de Euclides)", "MCM", "Aritmética Modular"])

with tab1:
    st.subheader("Test de Primalidad Paso a Paso")
    num_primo = st.number_input("Ingresa un número entero positivo:", min_value=1, max_value=1000000, value=29)
    if st.button("Evaluar Primalidad"):
        es_p, divisores, msj = es_primo_paso_a_paso(num_primo)
        if es_p:
            st.success(f"{msj}")
        else:
            st.warning(f"{msj}")
            
        if divisores:
            st.write("Divisores evaluados hasta $\\lfloor\\sqrt{n}\\rfloor$:")
            df_div = pd.DataFrame(divisores, columns=["Divisor probado (d)", "Residuo (n % d)"])
            st.dataframe(df_div, hide_index=True)

with tab2:
    st.subheader("Máximo Común Divisor (MCD) por Algoritmo de Euclides")
    col_a, col_b = st.columns(2)
    a_mcd = col_a.number_input("Número A:", min_value=1, value=252)
    b_mcd = col_b.number_input("Número B:", min_value=1, value=105)
    
    if st.button("Calcular MCD"):
        mcd_res, pasos = mcd_euclides_paso_a_paso(a_mcd, b_mcd)
        st.success(f"**Resultado:** $\\text{{MCD}}({a_mcd}, {b_mcd}) = {mcd_res}$")
        st.write("Tabla de divisiones sucesivas:")
        df_pasos = pd.DataFrame(pasos)
        st.dataframe(df_pasos[["dividendo", "divisor", "cociente", "residuo", "ecuacion"]], hide_index=True)

with tab3:
    st.subheader("Mínimo Común Múltiplo (MCM)")
    col_x, col_y = st.columns(2)
    x_mcm = col_x.number_input("Primer número:", min_value=1, value=12)
    y_mcm = col_y.number_input("Segundo número:", min_value=1, value=18)
    
    if st.button("Calcular MCM"):
        mcm_val, mcd_val, expl = mcm_con_explicacion(x_mcm, y_mcm)
        st.success(f"**Resultado:** $\\text{{MCM}}({x_mcm}, {y_mcm}) = {mcm_val}$")
        st.info(f"**Fórmula aplicada:** {expl}")

with tab4:
    st.subheader("Operación Residuo / Módulo y Congruencias")
    
    st.markdown("#### 1. Operación Módulo ($a \\pmod m$)")
    col_d, col_m = st.columns(2)
    dividendo = col_d.number_input("Dividendo (a):", value=17)
    divisor = col_m.number_input("Módulo / Divisor (m):", min_value=1, value=5)
    
    if st.button("Calcular Módulo"):
        res, coc, explic = operacion_modulo_explicada(dividendo, divisor)
        st.success(f"**Resultado:** {dividendo} mod {divisor} = {res}")
        st.markdown(f"""
        * **Desglose del Teorema del Resto:** $a = q \\cdot m + r$
        * En este caso: **{dividendo} = {divisor} × {coc} + {res}**
        * **Congruencia:** Decimos que dos números son congruentes módulo $m$ ($a \\equiv b \\pmod m$) si dejan el mismo residuo al dividirse por $m$. Por ejemplo: ${dividendo} \\equiv {res} \\pmod{{{divisor}}}$.
        """)

    st.markdown("---")
    st.markdown("#### 2. Verificador Interactivo de Congruencias ($a \\equiv b \\pmod m$)")
    st.caption("Verifica si dos números pertenecen a la misma clase de equivalencia módulo $m$.")
    
    col_ca, col_cb, col_cm = st.columns(3)
    cong_a = col_ca.number_input("Valor a:", value=38, key="cong_a")
    cong_b = col_cb.number_input("Valor b:", value=14, key="cong_b")
    cong_m = col_cm.number_input("Módulo m:", min_value=1, value=12, key="cong_m")
    
    if st.button("Evaluar Congruencia"):
        res_cong = verificar_congruencia(cong_a, cong_b, cong_m)
        if res_cong["es_congruente"]:
            st.success(f"**Verdadero:** ${cong_a} \\equiv {cong_b} \\pmod{{{cong_m}}}$")
        else:
            st.error(f"**Falso:** ${cong_a} \\not\\equiv {cong_b} \\pmod{{{cong_m}}}$")
            
        st.markdown(f"""
        **Demostración paso a paso:**
        1. Residuo de $a$: ${cong_a} \\pmod{{{cong_m}}} = {res_cong['res_a']}$
        2. Residuo de $b$: ${cong_b} \\pmod{{{cong_m}}} = {res_cong['res_b']}$
        3. Criterio de la diferencia: $a - b = {cong_a} - ({cong_b}) = {res_cong['diferencia']}$
        4. Divisibilidad: ${cong_m}$ {'divide exactamente a ' if res_cong['es_congruente'] else 'NO divide exactamente a '} ${res_cong['diferencia']}$ (${res_cong['diferencia']} = {cong_m} \\times {res_cong['cociente_dif']} + {res_cong['diferencia'] % cong_m}$).
        """)

st.markdown("---")
with st.expander("¿Qué conceptos estoy aprendiendo en este módulo?"):
    st.markdown("""
    * **Divisibilidad y Estructuras Discretas:** La divisibilidad establece relaciones de equivalencia en el conjunto de los enteros $\\mathbb{Z}$.
    * **Algoritmo de Euclides:** Es uno de los algoritmos formales más antiguos de la humanidad ($O(\\log(\\min(a, b)))$).
    * **Aritmética Modular ($\\mathbb{Z}_m$):** El concepto de residuo cíclico es la base de los autómatas finitos que reconocen propiedades numéricas y de toda la criptografía clásica y moderna.
    """)
