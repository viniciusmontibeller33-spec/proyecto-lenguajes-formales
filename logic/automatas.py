"""
Módulo C: Lógica de Autómatas Finitos Deterministas (AFD)

Este módulo implementa la definición formal de Autómatas Finitos Deterministas
según la teoría de Lenguajes Formales:
    M = (Q, Σ, δ, q₀, F)
donde:
    - Q: Conjunto finito de estados
    - Σ: Alfabeto finito de entrada
    - δ: Función de transición Q × Σ → Q
    - q₀: Estado inicial (q₀ ∈ Q)
    - F: Conjunto de estados finales o de aceptación (F ⊆ Q)
"""

from typing import Dict, List, Set, Tuple, Any, Optional

class AFD:
    def __init__(
        self,
        id_automata: str,
        nombre: str,
        descripcion: str,
        estados: List[str],
        alfabeto: Set[str],
        transiciones: Dict[Tuple[str, str], str],
        estado_inicial: str,
        estados_aceptacion: Set[str],
        explicacion_teorica: str,
        ejemplos_sugeridos: List[Dict[str, Any]],
        notas_casos_limite: str = ""
    ):
        self.id_automata = id_automata
        self.nombre = nombre
        self.descripcion = descripcion
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.explicacion_teorica = explicacion_teorica
        self.ejemplos_sugeridos = ejemplos_sugeridos
        self.notas_casos_limite = notas_casos_limite

    def validar_cadena_alfabeto(self, cadena: str) -> Tuple[bool, int, str]:
        """
        Verifica que todos los caracteres de la cadena pertenezcan al alfabeto Σ.
        Retorna (es_valido, posicion_error_1_based, caracter_invalido).
        """
        for idx, char in enumerate(cadena):
            if char not in self.alfabeto:
                return False, idx + 1, char
        return True, -1, ""

    def simular(self, cadena: str) -> Dict[str, Any]:
        """
        Ejecuta la simulación completa y paso a paso de la cadena en el autómata.
        """
        # 1. Validar símbolos contra el alfabeto Σ
        es_valida, pos_err, char_err = self.validar_cadena_alfabeto(cadena)
        if not es_valida:
            return {
                "exito": False,
                "error": f"Símbolo no permitido '{char_err}' en la posición {pos_err}. El alfabeto permitido es Σ = {{{', '.join(sorted(list(self.alfabeto)))}}}.",
                "pos_error": pos_err,
                "char_error": char_err,
                "pasos": [],
                "estado_final": None,
                "aceptada": False
            }

        estado_actual = self.estado_inicial
        pasos = []

        # 2. Caso de la cadena vacía (λ o ε)
        if not cadena:
            aceptada = estado_actual in self.estados_aceptacion
            return {
                "exito": True,
                "cadena": "",
                "es_vacia": True,
                "pasos": [],
                "estado_final": estado_actual,
                "aceptada": aceptada,
                "mensaje": (
                    f"Cadena vacía (λ) evaluada en el estado inicial '{estado_actual}'. "
                    f"{'Cadena ACEPTADA (El estado inicial q₀ pertenece al conjunto de aceptación F).' if aceptada else 'Cadena RECHAZADA (El estado inicial q₀ no pertenece a F).'}"
                )
            }

        # 3. Procesamiento símbolo por símbolo
        for idx, char in enumerate(cadena):
            estado_origen = estado_actual
            estado_destino = self.transiciones.get((estado_origen, char))
            
            if estado_destino is None:
                return {
                    "exito": False,
                    "error": f"Transición no definida para el estado '{estado_origen}' con el símbolo '{char}' en la posición {idx + 1}.",
                    "pasos": pasos,
                    "estado_final": estado_origen,
                    "aceptada": False
                }

            pasos.append({
                "paso": idx + 1,
                "posicion": idx,
                "simbolo": char,
                "estado_anterior": estado_origen,
                "transicion_str": f"δ({estado_origen}, '{char}') = {estado_destino}",
                "estado_siguiente": estado_destino,
                "es_aceptacion": estado_destino in self.estados_aceptacion
            })
            estado_actual = estado_destino

        aceptada = estado_actual in self.estados_aceptacion

        return {
            "exito": True,
            "cadena": cadena,
            "es_vacia": False,
            "pasos": pasos,
            "estado_final": estado_actual,
            "aceptada": aceptada,
            "mensaje": (
                f"La computación finalizó en el estado '{estado_actual}'. "
                f"{'Cadena ACEPTADA. Pertenece al lenguaje formal reconocido.' if aceptada else 'Cadena RECHAZADA. El estado final no pertenece a F.'}"
            )
        }

    def obtener_tabla_transiciones_data(self) -> List[Dict[str, Any]]:
        """
        Genera la matriz de transiciones δ en formato tabular para interfaz gráfica.
        """
        alfabeto_ordenado = sorted(list(self.alfabeto))
        filas = []

        for estado in self.estados:
            marca_inicial = "-> " if estado == self.estado_inicial else ""
            marca_final = "* " if estado in self.estados_aceptacion else ""
            etiqueta_estado = f"{marca_inicial}{marca_final}{estado}"

            fila = {"Estado": etiqueta_estado, "Identificador": estado}
            for simb in alfabeto_ordenado:
                destino = self.transiciones.get((estado, simb), "—")
                fila[f"Símbolo '{simb}'"] = destino
            filas.append(fila)

        return filas

    def generar_dot(
        self,
        estado_activo: Optional[str] = None,
        transicion_activa: Optional[Tuple[str, str, str]] = None
    ) -> str:
        """
        Genera el código en lenguaje DOT para Graphviz, resaltando:
        - El estado actual activo.
        - Los estados de aceptación (doble círculo).
        - La transición exacta ejecutada en el paso actual.
        """
        dot = [
            'digraph AFD {',
            '  rankdir=LR;',
            '  size="9,5";',
            '  bgcolor="transparent";',
            '  node [fontname="Helvetica, Arial, sans-serif", shape=circle, style="filled", fillcolor="#ffffff", color="#0284c7", penwidth=2.0, fontsize=13, fontcolor="#0f172a"];',
            '  edge [fontname="Helvetica, Arial, sans-serif", color="#64748b", fontcolor="#94a3b8", penwidth=1.5, fontsize=12, arrowsize=0.85];'
        ]

        # Flecha de entrada al estado inicial
        dot.append('  __start [shape=none, label="", width=0, height=0];')
        dot.append(f'  __start -> {self.estado_inicial} [label=" inicio", color="#38bdf8", fontcolor="#38bdf8", penwidth=2.2];')

        # Definición visual de cada nodo
        for estado in self.estados:
            es_aceptacion = estado in self.estados_aceptacion
            shape = "doublecircle" if es_aceptacion else "circle"

            if estado == estado_activo:
                # Estado activo en el paso actual (resaltado en celeste vibrante con borde cyan)
                fillcolor = "#0284c7"
                color = "#38bdf8"
                fontcolor = "#ffffff"
                penwidth = 3.2
            elif es_aceptacion:
                fillcolor = "#e0f2fe"
                color = "#0284c7"
                fontcolor = "#0369a1"
                penwidth = 2.4
            else:
                fillcolor = "#ffffff"
                color = "#0284c7"
                fontcolor = "#0f172a"
                penwidth = 1.8

            dot.append(
                f'  {estado} [shape={shape}, fillcolor="{fillcolor}", color="{color}", '
                f'fontcolor="{fontcolor}", penwidth={penwidth}];'
            )

        # Agrupar transiciones entre los mismos estados para que el grafo sea limpio
        trans_agrupadas: Dict[Tuple[str, str], List[str]] = {}
        for (origen, simbolo), destino in self.transiciones.items():
            trans_agrupadas.setdefault((origen, destino), []).append(simbolo)

        for (origen, destino), simbolos in trans_agrupadas.items():
            simbolos_str = ", ".join(sorted(simbolos))

            # Verificar si esta arista es la transición activa
            es_arista_activa = False
            if transicion_activa:
                t_orig, t_simb, t_dest = transicion_activa
                if t_orig == origen and t_dest == destino and t_simb in simbolos:
                    es_arista_activa = True

            if es_arista_activa:
                color_edge = "#38bdf8"
                color_font = "#38bdf8"
                penwidth_edge = 3.2
                arrowsize = 1.15
            else:
                color_edge = "#64748b"
                color_font = "#94a3b8"
                penwidth_edge = 1.5
                arrowsize = 0.85

            dot.append(
                f'  {origen} -> {destino} [label=" {simbolos_str} ", color="{color_edge}", '
                f'fontcolor="{color_font}", penwidth={penwidth_edge}, arrowsize={arrowsize}];'
            )

        dot.append("}")
        return "\n".join(dot)


# -------------------------------------------------------------------------
# AUTÓMATAS OBLIGATORIOS PREDEFINIDOS
# -------------------------------------------------------------------------

# 1. AFD: Cadenas binarias terminadas en '01'
afd_termina_01 = AFD(
    id_automata="termina_01",
    nombre="Cadenas binarias que terminan en '01'",
    descripcion=(
        "Este autómata finito determinista procesa cadenas en el alfabeto binario Σ = {0, 1} "
        "y acepta únicamente aquellas cuya secuencia finaliza con los dígitos '01'."
    ),
    estados=["q0", "q1", "q2"],
    alfabeto={"0", "1"},
    transiciones={
        ("q0", "0"): "q1",
        ("q0", "1"): "q0",
        ("q1", "0"): "q1",
        ("q1", "1"): "q2",
        ("q2", "0"): "q1",
        ("q2", "1"): "q0",
    },
    estado_inicial="q0",
    estados_aceptacion={"q2"},
    explicacion_teorica=(
        "**Función de cada estado según el sufijo visto:**\n\n"
        "* **q₀ (Estado Inicial):** Representa que el último símbolo leído no fue un '0' o la cadena está vacía. "
        "No termina en '01'.\n"
        "* **q₁ (Candidato a penúltimo símbolo):** Se acaba de leer un '0'. Si el siguiente símbolo es un '1', "
        "alcanzará el objetivo; si es otro '0', se mantiene en q₁ esperando un '1'.\n"
        "* **q₂ (Estado de Aceptación):** Se acaba de completar la secuencia '01'. La cadena es válida en este punto. "
        "Si llega un '0', pasa a q₁; si llega un '1', vuelve a q₀."
    ),
    ejemplos_sugeridos=[
        {"cadena": "01", "esperado": True, "tipo": "Aceptada básica"},
        {"cadena": "101", "esperado": True, "tipo": "Aceptada con prefijo 1"},
        {"cadena": "1101", "esperado": True, "tipo": "Aceptada con repeticiones"},
        {"cadena": "10", "esperado": False, "tipo": "Rechazada (termina en 10)"},
        {"cadena": "111", "esperado": False, "tipo": "Rechazada (solo unos)"},
        {"cadena": "100", "esperado": False, "tipo": "Rechazada (termina en 00)"},
        {"cadena": "", "esperado": False, "tipo": "Cadena vacía (λ)"},
        {"cadena": "10101", "esperado": True, "tipo": "Aceptada con alternancia"}
    ],
    notas_casos_limite=(
        "* **Cadena vacía (λ):** No contiene caracteres, por lo que no puede terminar en '01'. Es rechazada en q₀.\n"
        "* **Ceros consecutivos ('...00'):** Al leer ceros repetidos, el autómata permanece en q₁, ya que el último '0' siempre puede ser el inicio de un sufijo '01'."
    )
)


# 2. AFD: Números binarios divisibles por 3
afd_divisible_3 = AFD(
    id_automata="divisible_3",
    nombre="Números binarios divisibles por 3",
    descripcion=(
        "Este autómata reconoce las representaciones binarias de números enteros no negativos "
        "que son exactamente divisibles por 3 (es decir, con residuo 0 en la división módulo 3)."
    ),
    estados=["q0", "q1", "q2"],
    alfabeto={"0", "1"},
    transiciones={
        ("q0", "0"): "q0",
        ("q0", "1"): "q1",
        ("q1", "0"): "q2",
        ("q1", "1"): "q0",
        ("q2", "0"): "q1",
        ("q2", "1"): "q2",
    },
    estado_inicial="q0",
    estados_aceptacion={"q0"},
    explicacion_teorica=(
        "**Principio de la Aritmética Modular en Binario:**\n\n"
        "Cuando un número se lee de izquierda a derecha en binario (del bit más significativo al menos significativo), "
        "cada nuevo bit $b \\in \\{0, 1\\}$ multiplica el valor acumulado $v$ por 2 y le suma $b$:\n\n"
        "$$v_{\\text{nuevo}} = 2 \\cdot v_{\\text{anterior}} + b$$\n\n"
        "Aplicando congruencia módulo 3, la transición de estados responde exactamente a:\n\n"
        "$$\\delta(q_r, b) = q_{(2r + b) \\bmod 3}$$\n\n"
        "* **q₀ (Residuo 0 - Inicial y Aceptación):** El número acumulado hasta el momento es múltiplo exacto de 3.\n"
        "* **q₁ (Residuo 1):** El número acumulado deja residuo 1 al dividirse entre 3.\n"
        "* **q₂ (Residuo 2):** El número acumulado deja residuo 2 al dividirse entre 3."
    ),
    ejemplos_sugeridos=[
        {"cadena": "0", "esperado": True, "tipo": "0 decimal (0 mod 3 = 0)"},
        {"cadena": "11", "esperado": True, "tipo": "3 decimal (3 mod 3 = 0)"},
        {"cadena": "110", "esperado": True, "tipo": "6 decimal (6 mod 3 = 0)"},
        {"cadena": "1001", "esperado": True, "tipo": "9 decimal (9 mod 3 = 0)"},
        {"cadena": "1100", "esperado": True, "tipo": "12 decimal (12 mod 3 = 0)"},
        {"cadena": "100", "esperado": False, "tipo": "4 decimal (4 mod 3 = 1)"},
        {"cadena": "101", "esperado": False, "tipo": "5 decimal (5 mod 3 = 2)"},
        {"cadena": "111", "esperado": False, "tipo": "7 decimal (7 mod 3 = 1)"},
        {"cadena": "000", "esperado": True, "tipo": "Ceros iniciales (0 decimal)"}
    ],
    notas_casos_limite=(
        "* **Tratamiento de la Cadena Vacía (λ):** En la teoría pura de autómatas, si q₀ es de aceptación, la cadena vacía λ es aceptada formalmente (asociada al valor neutro 0). En la interfaz se documenta esta equivalencia formal.\n"
        "* **Ceros a la izquierda ('00...', '011'):** Agregar ceros a la izquierda no altera el valor del número ni su residuo módulo 3. Dado que δ(q₀, 0) = q₀, el autómata maneja de forma natural e invariante cualquier cantidad de ceros iniciales."
    )
)

def decimal_a_binario_info(cadena_binaria: str) -> Optional[Dict[str, Any]]:
    """
    Función utilitaria para el Módulo C: convierte la cadena binaria
    a entero decimal y desglosa el cálculo de divisibilidad por 3.
    """
    if not cadena_binaria:
        return {
            "decimal": 0,
            "cociente": 0,
            "residuo": 0,
            "es_divisible": True,
            "explicacion": "Cadena vacía evaluada con valor 0: 0 = 3 × 0 + 0 (residuo 0)"
        }
    try:
        val_dec = int(cadena_binaria, 2)
        cociente = val_dec // 3
        residuo = val_dec % 3
        es_divisible = (residuo == 0)
        return {
            "decimal": val_dec,
            "cociente": cociente,
            "residuo": residuo,
            "es_divisible": es_divisible,
            "explicacion": f"En base 10: {val_dec} = 3 × {cociente} + {residuo} (residuo = {residuo})"
        }
    except ValueError:
        return None
