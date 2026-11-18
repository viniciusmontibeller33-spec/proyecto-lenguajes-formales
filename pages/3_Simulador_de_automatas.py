import streamlit as st
import pandas as pd
import time
from logic.automatas import afd_termina_01, afd_divisible_3, decimal_a_binario_info

st.set_page_config(
    page_title="Simulador de Autómatas | StringLab",
    layout="wide"
)

# Cargar estilos visuales
try:
    with open("assets/styles.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except Exception:
    pass

st.title("Simulador de Autómatas Finitos (AFD)")
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

# 2. Definición Formal y Tabla de Transiciones
with st.expander("Definición Formal del Autómata: M = (Q, Σ, δ, q0, F)", expanded=False):
    t1, t2, t3 = st.columns([1, 1, 1])
    with t1:
        st.markdown(f"""
        * **Estados (Q):** `{{{', '.join(afd.estados)}}}`
        * **Alfabeto (Σ):** `{{{', '.join(sorted(list(afd.alfabeto)))}}}`
        * **Estado Inicial (q0):** `{afd.estado_inicial}`
        * **Estados de Aceptación (F):** `{{{', '.join(sorted(list(afd.estados_aceptacion)))}}}`
        """)
    with t2:
        st.markdown("**Tabla de Transiciones δ(q, σ):**")
        df_trans = pd.DataFrame(afd.obtener_tabla_transiciones_data())
        st.dataframe(df_trans.drop(columns=["Identificador"]), hide_index=True)
        st.caption("-> : Estado inicial | * : Estado de aceptación")
    with t3:
        st.markdown("**Fundamento Teórico:**")
        st.markdown(afd.explicacion_teorica)
        if afd.notas_casos_limite:
            st.markdown(afd.notas_casos_limite)

st.markdown("---")

# 3. Gestión de Estado y Entrada de Cadena
st.subheader("Entrada de Cadena")

# Inicialización segura de estado
if "cadena_actual" not in st.session_state:
    st.session_state.cadena_actual = "1101" if afd.id_automata == "termina_01" else "110"
if "paso_actual" not in st.session_state:
    st.session_state.paso_actual = 0
if "ultimo_afd" not in st.session_state:
    st.session_state.ultimo_afd = afd.id_automata

# Reinicio si cambia de autómata
if st.session_state.ultimo_afd != afd.id_automata:
    st.session_state.cadena_actual = "1101" if afd.id_automata == "termina_01" else "110"
    st.session_state.paso_actual = 0
    st.session_state.ultimo_afd = afd.id_automata

def aplicar_ejemplo(cad):
    st.session_state.cadena_actual = cad
    st.session_state.paso_actual = 0
    if "slider_pasos_sync" in st.session_state:
        st.session_state.slider_pasos_sync = 0

# Botones de ejemplos predefinidos
st.write("**Ejemplos sugeridos para evaluar con un clic:**")
cols_ejemplos = st.columns(len(afd.ejemplos_sugeridos))
for idx, ej in enumerate(afd.ejemplos_sugeridos):
    etiqueta = f"'{ej['cadena']}'" if ej['cadena'] else "λ (vacía)"
    estado_tipo = "[Aceptada]" if ej['esperado'] else "[Rechazada]"
    cols_ejemplos[idx].button(
        f"{etiqueta} {estado_tipo}",
        key=f"btn_ej_{afd.id_automata}_{idx}",
        on_click=aplicar_ejemplo,
        args=(ej["cadena"],),
        help=ej["tipo"]
    )

def on_texto_change():
    st.session_state.cadena_actual = st.session_state.txt_input_widget
    st.session_state.paso_actual = 0
    if "slider_pasos_sync" in st.session_state:
        st.session_state.slider_pasos_sync = 0

st.text_input(
    "Escribe una cadena binaria (solo dígitos 0 y 1, o deja vacío para λ):",
    value=st.session_state.cadena_actual,
    key="txt_input_widget",
    on_change=on_texto_change
)

# 4. Evaluación de la Cadena
res_sim = afd.simular(st.session_state.cadena_actual)

st.markdown("---")

if not res_sim["exito"]:
    st.error(f"Error Sintáctico de Entrada: {res_sim['error']}")
    st.warning("El autómata finito determinista está definido estrictamente sobre el alfabeto Σ = {0, 1}. Por favor, corrige la entrada.")
    st.subheader("Grafo del Autómata (Estado de Reposo)")
    st.graphviz_chart(afd.generar_dot(estado_activo=afd.estado_inicial))
else:
    total_pasos = len(res_sim["pasos"])
    
    # Asegurar que paso_actual esté dentro del rango válido
    if st.session_state.paso_actual > total_pasos:
        st.session_state.paso_actual = total_pasos
    if st.session_state.paso_actual < 0:
        st.session_state.paso_actual = 0
        
    paso_actual = st.session_state.paso_actual

    # Callbacks para los botones de control (100% confiables)
    def ir_inicio():
        st.session_state.paso_actual = 0
        st.session_state.slider_pasos_sync = 0

    def ir_anterior():
        if st.session_state.paso_actual > 0:
            st.session_state.paso_actual -= 1
            st.session_state.slider_pasos_sync = st.session_state.paso_actual

    def ir_siguiente():
        if st.session_state.paso_actual < total_pasos:
            st.session_state.paso_actual += 1
            st.session_state.slider_pasos_sync = st.session_state.paso_actual

    def ir_final():
        st.session_state.paso_actual = total_pasos
        st.session_state.slider_pasos_sync = total_pasos

    def on_slider_move():
        st.session_state.paso_actual = st.session_state.slider_pasos_sync

    # 5. Controles de navegación de la simulación
    st.subheader("Control de Simulación Paso a Paso")
    
    b1, b2, b3, b4, b5 = st.columns(5)
    b1.button("Inicio", on_click=ir_inicio, disabled=(paso_actual == 0), use_container_width=True)
    b2.button("Anterior", on_click=ir_anterior, disabled=(paso_actual == 0), use_container_width=True)
    b3.button("Siguiente", on_click=ir_siguiente, disabled=(paso_actual >= total_pasos), use_container_width=True)
    b4.button("Final", on_click=ir_final, disabled=(paso_actual >= total_pasos), use_container_width=True)
    b5.button("Reiniciar", on_click=ir_inicio, use_container_width=True)

    if total_pasos > 0:
        if "slider_pasos_sync" not in st.session_state:
            st.session_state.slider_pasos_sync = paso_actual
        st.slider(
            "Progreso de lectura de la cinta:",
            min_value=0,
            max_value=total_pasos,
            value=paso_actual,
            key="slider_pasos_sync",
            on_change=on_slider_move
        )

    # 6. Determinar estado activo y transición activa para el grafo interactivo
    if paso_actual == 0:
        estado_activo = afd.estado_inicial
        trans_activa = None
        info_paso_texto = f"Estado Inicial: {estado_activo} (Listo para leer la cadena)"
    else:
        info_p = res_sim["pasos"][paso_actual - 1]
        estado_activo = info_p["estado_siguiente"]
        trans_activa = (info_p["estado_anterior"], info_p["simbolo"], info_p["estado_siguiente"])
        es_acc = " [Estado de Aceptación]" if info_p["es_aceptacion"] else ""
        info_paso_texto = (
            f"Paso {paso_actual} de {total_pasos}: "
            f"Leyendo símbolo '{info_p['simbolo']}' desde {info_p['estado_anterior']} "
            f"-> Pasa a {info_p['estado_siguiente']}{es_acc} | Transición: {info_p['transicion_str']}"
        )

    # 7. Visualización de la Cinta de Entrada
    st.write("**Cinta de Entrada:**")
    if not st.session_state.cadena_actual:
        st.code("[ λ (Cadena Vacía) ] -> Evaluada directamente en el estado inicial q0")
    else:
        cinta_html = ["<div style='display: flex; gap: 8px; padding: 12px; background: #0f172a; border-radius: 8px; border: 1.5px solid #334155; font-family: monospace; font-size: 1.3rem; margin-bottom: 8px;'>"]
        for i, char in enumerate(st.session_state.cadena_actual):
            if i < paso_actual - 1:
                cinta_html.append(f"<span style='padding: 4px 14px; background: #1e293b; color: #38bdf8; border-radius: 6px; border: 1px solid #0284c7; font-weight: bold;'>{char}</span>")
            elif i == paso_actual - 1:
                cinta_html.append(f"<span style='padding: 4px 14px; background: #0284c7; color: #ffffff; border-radius: 6px; border: 2px solid #38bdf8; font-weight: bold; box-shadow: 0 0 10px #38bdf8;'>{char}</span>")
            else:
                cinta_html.append(f"<span style='padding: 4px 14px; background: #1e293b; color: #64748b; border-radius: 6px; border: 1px solid #334155;'>{char}</span>")
        cinta_html.append("</div>")
        st.markdown("".join(cinta_html), unsafe_allow_html=True)

    st.caption(f"**Estado de ejecución:** {info_paso_texto}")

    # Trayectoria de estados (Breadcrumb interactivo)
    if total_pasos > 0:
        trayectoria = [afd.estado_inicial]
        for p in res_sim["pasos"][:paso_actual]:
            trayectoria.append(p["estado_siguiente"])
        st.markdown(f"**Trayectoria recorrida:** `{' -> '.join(trayectoria)}`")

    # 8. Grafo Interactivo Sincronizado y Registro de Transiciones
    col_grafo, col_tabla = st.columns([3, 2])

    with col_grafo:
        st.markdown(f"#### Grafo del Autómata (Estado Activo: `{estado_activo}`)")
        codigo_dot = afd.generar_dot(estado_activo=estado_activo, transicion_activa=trans_activa)
        st.graphviz_chart(codigo_dot, use_container_width=True)

    with col_tabla:
        st.markdown("#### Registro de Transiciones")
        if res_sim["pasos"]:
            df_pasos = pd.DataFrame(res_sim["pasos"])
            df_pasos["Estado"] = df_pasos["paso"].apply(
                lambda p: "ACTUAL" if p == paso_actual else ("Pasado" if p < paso_actual else "Pendiente")
            )
            st.dataframe(
                df_pasos[["paso", "simbolo", "estado_anterior", "estado_siguiente", "Estado"]],
                hide_index=True,
                use_container_width=True
            )
        else:
            st.info("Cadena vacía evaluada. No hay transiciones intermedias.")

    # 9. Veredicto Final de Aceptación
    st.markdown("---")
    st.subheader("Veredicto de la Evaluación")

    if res_sim["aceptada"]:
        st.success(f"### CADENA ACEPTADA (Pertenece al Lenguaje L)\n\n{res_sim['mensaje']}")
    else:
        st.error(f"### CADENA RECHAZADA (No Pertenece al Lenguaje L)\n\n{res_sim['mensaje']}")

    if afd.id_automata == "divisible_3":
        info_dec = decimal_a_binario_info(st.session_state.cadena_actual)
        if info_dec:
            st.info(f"Comprobación Aritmética (Teoría de Números): {info_dec['explicacion']}")

# 10. Sección Didáctica Pedagógica
st.markdown("---")
with st.expander("¿Qué conceptos estoy aprendiendo en este módulo?"):
    st.markdown("""
    * **Lenguajes Regulares (Jerarquía de Chomsky - Tipo 3):** Los lenguajes aceptados por Autómatas Finitos Deterministas son exactamente la clase de lenguajes regulares, definibles también mediante expresiones regulares.
    * **Determinismo y Memoria Finita:** Un AFD no dispone de memoria infinita ni pila; su memoria reside exclusivamente en su conjunto finito de estados Q. Para cada estado y símbolo, existe exactamente una transición determinista:
      $$\\delta: Q \\times \\Sigma \\to Q$$
    * **Aritmética Modular en Autómatas:** Un autómata finito puede computar congruencias numéricas si los números se transmiten dígito por dígito. Para divisibilidad por 3 en binario, el estado almacena el residuo actual (0, 1, 2), demostrando que la aritmética en anillos Zk es computable con k estados.
    * **Cadena Vacía (λ) y Ceros Invariantes:** En la teoría de autómatas, el reconocimiento de la cadena vacía depende estrictamente de si q0 pertenece a F. En bases numéricas, los ceros iniciales corresponden a la invariancia del valor 0, modelados por el bucle δ(q0, 0) = q0.
    """)
