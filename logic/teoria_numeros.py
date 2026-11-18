"""
Lógica de Teoría de Números
Operaciones fundamentales: primalidad, Algoritmo de Euclides, MCM y congruencias modulares.
"""

import math

def es_primo_paso_a_paso(n: int):
    """
    Determina si un número es primo y registra los divisores probados.
    """
    if n <= 1:
        return False, [], f"El número {n} no es primo por definición (debe ser mayor que 1)."
        
    divisores_probados = []
    limite = int(math.isqrt(n))
    
    for i in range(2, limite + 1):
        resto = n % i
        divisores_probados.append((i, resto))
        if resto == 0:
            return False, divisores_probados, f"El número {n} es compuesto, divisible exactamente entre {i}."
            
    return True, divisores_probados, f"El número {n} es primo: no tiene divisores entre 2 y su raíz cuadrada ({limite})."

def mcd_euclides_paso_a_paso(a: int, b: int):
    """
    Calcula el MCD de a y b mediante el Algoritmo de Euclides,
    retornando cada división: dividendo = divisor * cociente + residuo.
    """
    if a < 0 or b < 0:
        raise ValueError("Los números deben ser enteros positivos.")
        
    pasos = []
    x, y = max(a, b), min(a, b)
    
    while y != 0:
        cociente = x // y
        residuo = x % y
        pasos.append({
            "dividendo": x,
            "divisor": y,
            "cociente": cociente,
            "residuo": residuo,
            "ecuacion": f"{x} = {y} × {cociente} + {residuo}"
        })
        x, y = y, residuo
        
    return x, pasos

def mcm_con_explicacion(a: int, b: int):
    """
    Calcula el MCM utilizando la relación con el MCD:
    MCM(a, b) = |a * b| / MCD(a, b)
    """
    if a == 0 or b == 0:
        return 0, 0, "El MCM de 0 con cualquier número es 0."
        
    mcd, pasos_mcd = mcd_euclides_paso_a_paso(a, b)
    mcm = abs(a * b) // mcd
    explicacion = f"MCM({a}, {b}) = |{a} × {b}| / MCD({a}, {b}) = {abs(a*b)} / {mcd} = {mcm}"
    
    return mcm, mcd, explicacion

def operacion_modulo_explicada(dividendo: int, divisor: int):
    """
    Explica la operación dividendo mod divisor.
    """
    if divisor == 0:
        raise ZeroDivisionError("No se permite la división entre cero.")
        
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    explicacion = f"{dividendo} mod {divisor} = {residuo} (ya que {dividendo} = {divisor} × {cociente} + {residuo})"
    
    return residuo, cociente, explicacion

def verificar_congruencia(a: int, b: int, m: int):
    """
    Verifica si dos números a y b son congruentes módulo m: a ≡ b (mod m).
    Retorna el resultado booleano, residuos y una explicación paso a paso.
    """
    if m <= 0:
        raise ValueError("El módulo m debe ser un entero positivo mayor que cero.")
        
    res_a = a % m
    res_b = b % m
    diferencia = a - b
    es_congruente = (res_a == res_b)
    cociente_dif = diferencia // m
    resto_dif = diferencia % m
    
    explicacion = (
        f"¿Es {a} ≡ {b} (mod {m})? -> {'SÍ, son congruentes' if es_congruente else 'NO son congruentes'}.\n"
        f"• {a} mod {m} = {res_a}\n"
        f"• {b} mod {m} = {res_b}\n"
        f"• Diferencia: a - b = {a} - ({b}) = {diferencia}\n"
        f"• Criterio de divisibilidad: {m} {'divide exactamente a ' if es_congruente else 'NO divide exactamente a '}{diferencia} "
        f"({diferencia} = {m} × {cociente_dif} + {resto_dif})."
    )
    
    return {
        "es_congruente": es_congruente,
        "a": a,
        "b": b,
        "m": m,
        "res_a": res_a,
        "res_b": res_b,
        "diferencia": diferencia,
        "cociente_dif": cociente_dif,
        "explicacion": explicacion
    }
