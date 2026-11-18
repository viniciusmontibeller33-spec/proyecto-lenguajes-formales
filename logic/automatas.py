"""
Módulo C: Lógica de Autómatas Finitos Deterministas (AFD)
Responsable: Vini (Rama: vini)
"""

from typing import Dict, List, Set, Tuple, Any

class AFD:
    def __init__(
        self,
        nombre: str,
        descripcion: str,
        estados: List[str],
        alfabeto: Set[str],
        transiciones: Dict[Tuple[str, str], str],
        estado_inicial: str,
        estados_aceptacion: Set[str],
        explicacion_teorica: str
    ):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.explicacion_teorica = explicacion_teorica

    def validar_cadena_alfabeto(self, cadena: str) -> Tuple[bool, int, str]:
        """
        Verifica que todos los caracteres pertenezcan al alfabeto.
        Retorna (valido, posicion_error, caracter_invalido).
        """
        for idx, char in enumerate(cadena):
            if char not in self.alfabeto:
                return False, idx + 1, char
        return True, -1, ""

    def simular(self, cadena: str) -> Dict[str, Any]:
        """
        Ejecuta la simulación paso a paso de la cadena en el autómata.
        """
        es_valida, pos_err, char_err = self.validar_cadena_alfabeto(cadena)
        if not es_valida:
            return {
                "exito": False,
                "error": f"Símbolo no permitido '{char_err}' en la posición {pos_err}. Alfabeto permitido: {sorted(list(self.alfabeto))}",
                "pasos": [],
                "estado_final": None,
                "aceptada": False
            }

        estado_actual = self.estado_inicial
        pasos = []

        # Caso cadena vacía
        if not cadena:
            aceptada = estado_actual in self.estados_aceptacion
            return {
                "exito": True,
                "cadena": "λ (vacía)",
                "pasos": [],
                "estado_final": estado_actual,
                "aceptada": aceptada,
                "mensaje": f"Cadena vacía evaluada en el estado inicial {estado_actual}. " + 
                           ("Aceptada (pertenece a los estados de aceptación)." if aceptada else "Rechazada (no es estado de aceptación).")
            }

        for idx, char in enumerate(cadena):
            estado_origen = estado_actual
            estado_destino = self.transiciones.get((estado_origen, char))
            pasos.append({
                "paso": idx + 1,
                "simbolo": char,
                "estado_anterior": estado_origen,
                "estado_siguiente": estado_destino
            })
            estado_actual = estado_destino

        aceptada = estado_actual in self.estados_aceptacion

        return {
            "exito": True,
            "cadena": cadena,
            "pasos": pasos,
            "estado_final": estado_actual,
            "aceptada": aceptada,
            "mensaje": f"La cadena culminó en el estado '{estado_actual}'. " +
                       ("¡Cadena ACEPTADA!" if aceptada else "Cadena RECHAZADA (el estado final no es de aceptación).")
        }

    def generar_dot(self, estado_activo: str = None) -> str:
        """
        Genera el código DOT para visualizar el autómata con Graphviz,
        resaltando el estado activo en la simulación paso a paso.
        """
        dot = ["digraph AFD {"]
        dot.append('  rankdir=LR;')
        dot.append('  size="8,5"')
        dot.append('  node [fontname="Helvetica", shape=circle, style=filled, fillcolor="#f0f9ff", color="#0284c7", penwidth=1.5];')
        dot.append('  edge [fontname="Helvetica", color="#0369a1", fontcolor="#0c4a6e", penwidth=1.2];')

        # Flecha invisible al estado inicial
        dot.append('  __inicio [shape=point, style=invis];')
        dot.append(f'  __inicio -> {self.estado_inicial} [penwidth=1.5];')

        # Configuración de nodos
        for estado in self.estados:
            es_aceptacion = estado in self.estados_aceptacion
            shape = "doublecircle" if es_aceptacion else "circle"
            
            # Resaltar si es el estado actualmente activo
            if estado == estado_activo:
                fillcolor = "#38bdf8"
                color = "#0369a1"
                fontcolor = "#ffffff"
                penwidth = 2.5
            else:
                fillcolor = "#e0f2fe" if es_aceptacion else "#ffffff"
                color = "#0284c7"
                fontcolor = "#0f172a"
                penwidth = 1.8 if es_aceptacion else 1.2

            dot.append(f'  {estado} [shape={shape}, fillcolor="{fillcolor}", color="{color}", fontcolor="{fontcolor}", penwidth={penwidth}];')

        # Agrupar transiciones entre mismos pares de nodos
        trans_agrupadas: Dict[Tuple[str, str], List[str]] = {}
        for (origen, simbolo), destino in self.transiciones.items():
            par = (origen, destino)
            trans_agrupadas.setdefault(par, []).append(simbolo)

        for (origen, destino), simbolos in trans_agrupadas.items():
            label = ", ".join(sorted(simbolos))
            dot.append(f'  {origen} -> {destino} [label=" {label} "];')

        dot.append("}")
        return "\n".join(dot)


# Definición de Autómatas Obligatorios

# 1. Cadenas binarias que terminan en 01
afd_termina_01 = AFD(
    nombre="Cadenas binarias terminadas en '01'",
    descripcion="Reconoce secuencias binarias sobre Σ = {0, 1} cuya subcadena final sea exactamente '01'.",
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
        "• q0: Estado inicial. La cadena no termina en 0 ni en 01.\n"
        "• q1: Se leyó un '0'. Podría ser el penúltimo símbolo de la cadena.\n"
        "• q2: Se leyó un '1' inmediatamente después de un '0'. La cadena termina en '01' (Aceptación)."
    )
)

# 2. Números binarios divisibles por 3
afd_divisible_3 = AFD(
    nombre="Números binarios divisibles por 3",
    descripcion="Reconoce secuencias binarias cuyo valor numérico decimal sea divisible exactamente por 3 (módulo 3 = 0).",
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
        "En la lectura de números binarios de izquierda a derecha (MSB a LSB), al concatenar un bit b, "
        "el nuevo valor numérico es: v_nuevo = (2 × v_anterior + b) mod 3.\n\n"
        "• q0 (Residuo 0): El número actual es múltiplo de 3 (Estado inicial y de aceptación).\n"
        "• q1 (Residuo 1): El residuo de la división entre 3 es 1.\n"
        "• q2 (Residuo 2): El residuo de la división entre 3 es 2."
    )
)
