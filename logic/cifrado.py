"""
Lógica de Cifrado Educativo (César Modular)
Implementa transformaciones en el anillo cíclico Z26:
    C = (P + K) mod 26
    P = (C - K) mod 26
"""

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = len(ALFABETO)

def obtener_alfabeto_desplazado(k: int):
    """
    Retorna el alfabeto original y el alfabeto desplazado k posiciones.
    """
    k = k % N
    desplazado = ALFABETO[k:] + ALFABETO[:k]
    return ALFABETO, desplazado

def cifrar_cesar_paso_a_paso(mensaje: str, k: int):
    """
    Cifra un mensaje usando César y registra el cálculo paso a paso.
    Fórmula: C = (P + K) mod 26
    """
    k = k % N
    pasos = []
    resultado = []
    
    for idx, c in enumerate(mensaje):
        es_mayus = c.isupper()
        c_upper = c.upper()
        
        if c_upper in ALFABETO:
            p = ALFABETO.index(c_upper)
            c_pos = (p + k) % N
            letra_cifrada = ALFABETO[c_pos] if es_mayus else ALFABETO[c_pos].lower()
            
            pasos.append({
                "posicion": idx + 1,
                "caracter_original": c,
                "valor_p": p,
                "clave_k": k,
                "formula": f"({p} + {k}) mod 26 = {c_pos}",
                "caracter_cifrado": letra_cifrada
            })
            resultado.append(letra_cifrada)
        else:
            pasos.append({
                "posicion": idx + 1,
                "caracter_original": c,
                "valor_p": "-",
                "clave_k": k,
                "formula": "No aplica (símbolo conservado)",
                "caracter_cifrado": c
            })
            resultado.append(c)
            
    return "".join(resultado), pasos

def descifrar_cesar_paso_a_paso(mensaje_cifrado: str, k: int):
    """
    Descifra un mensaje usando César y registra el cálculo paso a paso.
    Fórmula: P = (C - K) mod 26
    """
    k = k % N
    pasos = []
    resultado = []
    
    for idx, c in enumerate(mensaje_cifrado):
        es_mayus = c.isupper()
        c_upper = c.upper()
        
        if c_upper in ALFABETO:
            c_pos = ALFABETO.index(c_upper)
            p = (c_pos - k) % N
            letra_descifrada = ALFABETO[p] if es_mayus else ALFABETO[p].lower()
            
            pasos.append({
                "posicion": idx + 1,
                "caracter_cifrado": c,
                "valor_c": c_pos,
                "clave_k": k,
                "formula": f"({c_pos} - {k}) mod 26 = {p}",
                "caracter_descifrado": letra_descifrada
            })
            resultado.append(letra_descifrada)
        else:
            pasos.append({
                "posicion": idx + 1,
                "caracter_cifrado": c,
                "valor_c": "-",
                "clave_k": k,
                "formula": "No aplica (símbolo conservado)",
                "caracter_descifrado": c
            })
            resultado.append(c)
            
    return "".join(resultado), pasos
