import streamlit as st
import pandas as pd
import time
from logic.automatas import afd_termina_01, afd_divisible_3, decimal_a_binario_info

st.set_page_config(
    page_title="Módulo C: Simulador de Autómatas | StringLab",
    page_icon="⚙️",
    layout="wide"
)

# Cargar estilos si existen
try:
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except Exception:
    pass

st.title("⚙️ Módulo C: Simulador de Autómatas Finitos (AFD)")
st.markdown("**Responsable del Módulo:** Vini (`rama: vini`)")
st.caption("Visualización interactiva, seguimiento paso a paso y análisis formal de Autómatas Finitos Deterministas.")
st.markdown("---")

# 1. Selector de Autómata
col_sel, col_desc = st.columns([1, 2])

with col_sel:
    opcion = st.selectbox(
        "Elige un Autómata para experimentar:",
        [
            "1. Cadenas binarias terminadas en '01'",
            "2. Números binarios divisibles por 3"
        ],
        key="selector_afd"
    )

afd = afd_termina_01 if "01" in opcion else afd_divisible_3

with col_desc:
    st.info(f"**{afd.nombre}**\n\n{afd.descripcion}")

# 2. Especificación Teórica y Tabla de Transiciones (Expandible)
with st.expander("📐 Definición Formal del Autómata: M = (Q, Σ, δ, q₀, F)", expanded=False):
    t1, t2, t3 = st.columns([1, 1, 1])
    with t1:
        st.markdown(f"""
        * **Estados ($Q$):** `{{{', '.join(afd.estados)}}}`
        * **Alfabeto ($\Sigma$):** `{{{', '.join(sorted(list(afd.alfabeto)))}}}`
        * **Estado Inicial ($q_0$):** `{afd.estado_inicial}`
        * **Estados de Aceptación ($F$):** `{{{', '.join(sorted(list(afd.estados_aceptacion)))}}}`
        """)
    with t2:
        st.markdown("**Tabla de Transiciones $\delta(q, \sigma)$:**")
        df_trans = pd.DataFrame(afd.obtener_tabla_transiciones_data())
        st.dataframe(df_trans.drop(columns=["Identificador"]), hide_index=True)
        st.caption("➔ : Estado inicial | ★ : Estado de aceptación")
    with t3:
        st.markdown("**Fundamento Teórico:**")
        st.markdown(afd.explicacion_teorica)
        if afd.notas_casos_limite:
            st.markdown(afd.notas_casos_limite)

st.markdown("---")

# 3. Entrada de la Cadena y Ejemplos Rápidos
st.subheader("📥 Entrada de Cadena")

# Inicialización de estado en session_state para este módulo
if "cadena_actual" not in st.session_state:
    st.session_state.cadena_actual = "1101" if afd.id_automata == "termina_01" else "110"
if "paso_index" not in st.session_state:
    st.session_state.paso_index = 0
if "ultimo_afd" not in st.session_state:
    st.session_state.ultimo_afd = afd.id_automata

# Si el usuario cambió de autómata, reiniciamos la cadena por defecto sugerida
if st.session_state.ultimo_afd != afd.id_automata:
    st.session_state.cadena_actual = "1101" if afd.id_automata == "termina_01" else "110"
    st.session_state.paso_index = 0
    st.session_state.ultimo_afd = afd.id_automata

# Botones de ejemplos sugeridos
st.write("**Ejemplos predefinidos para probar:**")
cols_ejemplos = st.columns(len(afd.ejemplos_sugeridos))
for idx, ej in enumerate(afd.ejemplos_sugeridos):
    etiqueta = f"'{ej['cadena']}'" if ej['cadena'] else "λ (vacía)"
    icono = "✅" if ej['esperado'] else "❌"
    if cols_ejemplos[idx].button(f"{icono} {etiqueta}", key=f"btn_ej_{idx}", help=ej["tipo"]):
        st.session_state.cadena_actual = ej["cadena"]
        st.session_state.paso_index = 0
        st.rerun()

# Campo de texto interactivo
col_in, col_btn_eval = st.columns([3, 1])
cadena_usuario = col_in.text_input(
    "Escribe una cadena binaria (solo dígitos 0 y 1, o deja vacío para λ):",
    value=st.session_state.cadena_actual,
    key="input_cadena"
)

# Sincronizar si el usuario escribe en el input
if cadena_usuario != st.session_state.cadena_actual:
    st.session_state.cadena_actual = cadena_usuario
    st.session_state.paso_index = 0

# Ejecución de la simulación
res_sim = afd.simular(st.session_state.cadena_actual)

st.markdown("---")

# 4. Manejo de Errores Sintácticos
if not res_sim["exito"]:
    st.error(f"🚫 **Error Sintáctico de Entrada:** {res_sim['error']}")
    st.warning("El autómata finito determinista está definido estrictamente sobre el alfabeto $\Sigma = \\{0, 1\\}$. Por favor, corrige la cadena.")
    # Mostrar el grafo en reposo
    st.subheader("🕸️ Grafo del Autómata (Estado de Reposo)")
    st.graphviz_chart(afd.generar_dot(estado_activo=afd.estado_inicial))

# 5. Visualización de Simulación Válida (Paso a Paso y Grafo)
else:
    total_pasos = len(res_sim["pasos"])
    paso_actual = min(st.session_state.paso_index, total_pasos)

    # Determinar estado activo y transición activa
    if paso_actual == 0:
        estado_activo = afd.estado_inicial
        trans_activa = None
        info_paso_texto = f"Estado Inicial: **{estado_activo}** (Listo para leer la cadena)"
    else:
        info_p = res_sim["pasos"][paso_actual - 1]
        estado_activo = info_p["estado_siguiente"]
        trans_activa = (info_p["estado_anterior"], info_p["simbolo"], info_p["estado_siguiente"])
        info_paso_texto = (
            f"Paso {paso_actual} de {total_pasos}: "
            f"Leyendo símbolo '**{info_p['simbolo']}**' en posición {info_p['paso']} | "
            f"Transición: `{info_p['transicion_str']}`"
        )

    # Controles de navegación paso a paso
    st.subheader("🎮 Control de Simulación Paso a Paso")
    
    c_btn1, c_btn2, c_btn3, c_btn4, c_btn5 = st.columns([1, 1, 1, 1, 1])
    
    if c_btn1.button("⏮️ Inicio", use_container_width=True, disabled=(paso_actual == 0)):
        st.session_state.paso_index = 0
        st.rerun()

    if c_btn2.button("◀ Anterior", use_container_width=True, disabled=(paso_actual == 0)):
        st.session_state.paso_index = max(0, paso_actual - 1)
        st.rerun()

    if c_btn3.button("Siguiente ▶", use_container_width=True, disabled=(paso_actual >= total_pasos)):
        st.session_state.paso_index = min(total_pasos, paso_actual + 1)
        st.rerun()

    if c_btn4.button("⏭️ Final", use_container_width=True, disabled=(paso_actual >= total_pasos)):
        st.session_state.paso_index = total_pasos
        st.rerun()

    if c_btn5.button("🔄 Reiniciar", use_container_width=True):
        st.session_state.paso_index = 0
        st.rerun()

    # Barra deslizante (slider)
    if total_pasos > 0:
        nuevo_paso = st.slider(
            "Progreso de lectura de la cinta:",
            min_value=0,
            max_value=total_pasos,
            value=paso_actual,
            key="slider_pasos"
        )
        if nuevo_paso != paso_actual:
            st.session_state.paso_index = nuevo_paso
            st.rerun()

    # Visualización de la Cinta de Entrada
    st.write("**Cinta de Entrada:**")
    if not st.session_state.cadena_actual:
        st.code("[ λ (Cadena Vacía) ] ➔ Evaluada directamente en el estado inicial q₀")
    else:
        cinta_html = ["<div style='font-family: monospace; font-size: 1.25rem; letter-spacing: 4px; padding: 10px; background: #f8fafc; border-radius: 8px; border: 1px solid #cbd5e1;'>"]
        for i, char in enumerate(st.session_state.cadena_actual):
            if i < paso_actual - 1:
                # Ya leído
                cinta_html.append(f"<span style='color: #0284c7; font-weight: bold;'>{char}</span>")
            elif i == paso_actual - 1:
                # Símbolo actualmente activo
                cinta_html.append(f"<span style='background: #38bdf8; color: #ffffff; padding: 2px 6px; border-radius: 4px; font-weight: bold;'>{char}</span>")
            else:
                # Aún no leído
                cinta_html.append(f"<span style='color: #94a3b8;'>{char}</span>")
        cinta_html.append("</div>")
        st.markdown("".join(cinta_html), unsafe_allow_html=True)

    st.caption(info_paso_texto)

    # 6. Grafo Visual Sincronizado
    col_grafo, col_tabla = st.columns([3, 2])

    with col_grafo:
        st.markdown(f"#### 🕸️ Grafo del Autómata (Estado Activo: `{estado_activo}`)")
        codigo_dot = afd.generar_dot(estado_activo=estado_activo, transicion_activa=trans_activa)
        st.graphviz_chart(codigo_dot, use_container_width=True)

    with col_tabla:
        st.markdown("#### 📋 Registro de Transiciones")
        if res_sim["pasos"]:
            df_pasos = pd.DataFrame(res_sim["pasos"])
            # Añadir indicador visual de paso actual
            df_pasos["Estado"] = df_pasos["paso"].apply(
                lambda p: "👉 ACTUAL" if p == paso_actual else ("✓ Pasado" if p < paso_actual else "⏳ Pendiente")
            )
            st.dataframe(
                df_pasos[["paso", "simbolo", "estado_anterior", "estado_siguiente", "Estado"]],
                hide_index=True,
                use_container_width=True
            )
        else:
            st.info("Cadena vacía evaluada. No hay transiciones intermedias.")

    # 7. Veredicto Final de Aceptación
    st.markdown("---")
    st.subheader("🏁 Veredicto de la Evaluación")

    if res_sim["aceptada"]:
        st.success(f"### ✅ CADENA ACEPTADA (Pertenece al Lenguaje L)\n\n{res_sim['mensaje']}")
    else:
        st.error(f"### ❌ CADENA RECHAZADA (No Pertenece al Lenguaje L)\n\n{res_sim['mensaje']}")

    # Información complementaria para el autómata de divisibilidad por 3
    if afd.id_automata == "divisible_3":
        info_dec = decimal_a_binario_info(st.session_state.cadena_actual)
        if info_dec:
            st.info(f"🔢 **Comprobación Aritmética (Teoría de Números):** {info_dec['explicacion']}")

# 8. Sección Didáctica Pedagógica
st.markdown("---")
with st.expander("🎓 ¿Qué conceptos estoy aprendiendo en este módulo?"):
    st.markdown("""
    * **Lenguajes Regulares (Jerarquía de Chomsky - Tipo 3):** Los lenguajes aceptados por Autómatas Finitos Deterministas son exactamente la clase de lenguajes regulares, definibles también mediante expresiones regulares.
    * **Determinismo y Memoria Finita:** Un AFD no dispone de memoria infinita ni pila; su "memoria" reside exclusivamente en su conjunto finito de estados $Q$. Para cada estado y símbolo, existe exactamente una transición determinista:
      $$\\delta: Q \\times \\Sigma \\to Q$$
    * **Aritmética Modular en Autómatas:** Un autómata finito puede computar congruencias numéricas si los números se transmiten dígito por dígito. Para divisibilidad por 3 en binario, el estado almacena el residuo actual ($0, 1, 2$), demostrando que la aritmética en anillos $\\mathbb{Z}_k$ es computable con $k$ estados.
    * **Cadena Vacía ($\lambda$) y Ceros Invariantes:** En la teoría de autómatas, el reconocimiento de la cadena vacía depende estrictamente de si $q_0 \\in F$. En bases numéricas, los ceros iniciales corresponden a la invariancia del valor $0$, modelados por el bucle $\\delta(q_0, 0) = q_0$.
    """)
