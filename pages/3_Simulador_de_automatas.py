import streamlit as st
import pandas as pd
from logic.automatas import afd_termina_01, afd_divisible_3

st.set_page_config(page_title="Módulo C: Simulador de Autómatas | StringLab", page_icon="⚙️", layout="wide")

st.title("⚙️ Módulo C: Simulador de Autómatas Finitos Deterministas (AFD)")
st.markdown("**Responsable:** Vini (`rama: vini`)")
st.caption("Simulación visual interactiva, seguimiento paso a paso y verificación formal de lenguajes regulares.")
st.markdown("---")

opcion_afd = st.selectbox(
    "Selecciona un Autómata Finito Determinista:",
    ["1. Cadenas binarias terminadas en '01'", "2. Números binarios divisibles por 3"]
)

afd_seleccionado = afd_termina_01 if "01" in opcion_afd else afd_divisible_3

st.subheader(f"📌 {afd_seleccionado.nombre}")
st.write(afd_seleccionado.descripcion)

# Definición formal 5-tupla
with st.expander("📐 Definición formal del Autómata M = (Q, Σ, δ, q₀, F)", expanded=False):
    st.markdown(f"""
    * **Estados ($Q$):** `{{{', '.join(afd_seleccionado.estados)}}}`
    * **Alfabeto ($\Sigma$):** `{{{', '.join(sorted(list(afd_seleccionado.alfabeto)))}}}`
    * **Estado inicial ($q_0$):** `{afd_seleccionado.estado_inicial}`
    * **Estados de aceptación ($F$):** `{{{', '.join(afd_seleccionado.estados_aceptacion)}}}`
    
    **Significado de los estados:**
    {afd_seleccionado.explicacion_teorica}
    """)

# Mostrar grafo inicial del autómata
st.subheader("🕸️ Grafo del Autómata")
st.graphviz_chart(afd_seleccionado.generar_dot())

st.markdown("---")
st.subheader("🧪 Simulación de Cadena")

col_cadena, col_btn = st.columns([3, 1])
cadena_input = col_cadena.text_input("Ingresa una cadena binaria para evaluar:", value="1101" if "01" in opcion_afd else "110")
evaluar = col_btn.button("Evaluar Cadena", use_container_width=True)

if "sim_estado" not in st.session_state:
    st.session_state.sim_estado = {"cadena": "", "resultado": None, "paso_actual": 0}

if evaluar:
    resultado = afd_seleccionado.simular(cadena_input)
    st.session_state.sim_estado = {
        "cadena": cadena_input,
        "resultado": resultado,
        "paso_actual": len(resultado["pasos"]) if resultado["exito"] else 0
    }

sim = st.session_state.sim_estado
res = sim["resultado"]

if res:
    if not res["exito"]:
        st.error(f"❌ {res['error']}")
    else:
        st.markdown(f"### Resultado Final: {'✅ ACEPTADA' if res['aceptada'] else '❌ RECHAZADA'}")
        st.info(res["mensaje"])
        
        if res["pasos"]:
            st.subheader("🐾 Seguimiento Paso a Paso")
            
            # Slider o control de paso
            paso_seleccionado = st.slider(
                "Moverse entre los pasos de la simulación:",
                min_value=0,
                max_value=len(res["pasos"]),
                value=len(res["pasos"])
            )
            
            if paso_seleccionado == 0:
                estado_en_paso = afd_seleccionado.estado_inicial
                st.caption(f"Inicio antes de leer símbolos. Estado: **{estado_en_paso}**")
            else:
                paso_info = res["pasos"][paso_seleccionado - 1]
                estado_en_paso = paso_info["estado_siguiente"]
                st.caption(f"Paso {paso_seleccionado}: Leyendo símbolo '**{paso_info['simbolo']}**' desde **{paso_info['estado_anterior']}** ➔ Pasa a **{estado_en_paso}**")
                
            # Grafo con estado activo resaltado
            st.graphviz_chart(afd_seleccionado.generar_dot(estado_activo=estado_en_paso))
            
            # Tabla de ejecución completa
            st.write("Tabla de transiciones ejecutadas:")
            df_pasos = pd.DataFrame(res["pasos"])
            st.dataframe(df_pasos, hide_index=True, use_container_width=True)

st.markdown("---")
with st.expander("🎓 ¿Qué conceptos estoy aprendiendo en este módulo?"):
    st.markdown("""
    * **Lenguajes Regulares (Chomsky Tipo 3):** Son aquellos que pueden ser reconocidos por un autómata finito con memoria finita (sus estados).
    * **Relación con Teoría de Números:** Un AFD con $k$ estados puede computar congruencias módulo $k$. Cada nuevo bit $b$ en binario desplaza el número hacia la izquierda ($2v + b$), lo que genera transiciones cíclicas exactas entre los residuos.
    * **Determinismo:** Para cada par $(q, \sigma) \in Q \times \Sigma$, existe una y solo una transición $\delta(q, \sigma)$, lo que permite ejecuciones computacionales predecibles y de tiempo lineal $O(|w|)$.
    """)
