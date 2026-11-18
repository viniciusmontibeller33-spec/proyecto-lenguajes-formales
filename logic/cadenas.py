"""
Operaciones de Análisis de Cadenas de StringLab.
"""

from collections import Counter
import unicodedata


class ResultadoBusqueda(dict):
    """
    Estructura de resultado de búsqueda de subcadenas.
    Funciona como diccionario con metadatos (posiciones, ocurrencias, comparaciones)
    y mantiene compatibilidad de igualdad con listas para pruebas unitarias.
    """
    def __eq__(self, other):
        if isinstance(other, list):
            return self.get('posiciones', []) == other
        return super().__eq__(other)


def frecuencia_caracteres(texto):
    """Frecuencias exactas, ordenadas de mayor a menor y luego por carácter."""
    return dict(sorted(Counter(texto).items(), key=lambda par: (-par[1], par[0])))


def analizar_cadena(texto):
    """Cuenta caracteres; espacios incluye tabulaciones y saltos de línea.

    Cada carácter ocupa una sola categoría. El total usa los puntos de código
    de Python, por lo que un emoji compuesto puede ocupar varias posiciones.
    """
    conteo = dict(letras=0, vocales=0, consonantes=0, digitos=0,
                  espacios=0, simbolos=0)
    for caracter in texto:
        if caracter.isalpha():
            conteo['letras'] += 1
            base = unicodedata.normalize('NFD', caracter.casefold())[0]
            if base in 'aeiou':
                conteo['vocales'] += 1
            else:
                conteo['consonantes'] += 1
        elif caracter.isdigit():
            conteo['digitos'] += 1
        elif caracter.isspace():
            conteo['espacios'] += 1
        else:
            conteo['simbolos'] += 1

    total = len(texto)
    sin_espacios = total - conteo['espacios']
    freq = frecuencia_caracteres(texto)

    return {
        'total': total,
        'sin_espacios': sin_espacios,
        'total_con_espacios': total,
        'total_sin_espacios': sin_espacios,
        'espacios_simples': texto.count(' '),
        'frecuencias': freq,
        **conteo
    }


def verificar_palindromo(texto):
    """Ignora mayúsculas, blancos y signos; conserva acentos y dígitos.

    NFC unifica acentos compuestos y descompuestos. Una entrada sin letras
    ni dígitos se considera no evaluable (es_palindromo=False).
    """
    normalizado = unicodedata.normalize('NFC', texto).casefold()
    normalizado = ''.join(c for c in normalizado if c.isalnum())
    pasos = []
    izquierda, derecha = 0, len(normalizado) - 1
    while izquierda < derecha:
        iguales = normalizado[izquierda] == normalizado[derecha]
        pasos.append({
            'Paso': len(pasos) + 1,
            'Índice izquierdo': izquierda,
            'Carácter izquierdo': normalizado[izquierda],
            'Índice derecho': derecha,
            'Carácter derecho': normalizado[derecha],
            'Resultado': 'Iguales' if iguales else 'Diferentes'
        })
        if not iguales:
            break
        izquierda += 1
        derecha -= 1

    return {
        'normalizado': normalizado,
        'invertido': normalizado[::-1],
        'evaluable': bool(normalizado),
        'es_palindromo': bool(normalizado) and normalizado == normalizado[::-1],
        'pasos': pasos
    }


def es_palindromo(texto: str):
    """Función de interfaz compatible que retorna (es_pal, limpio, invertido)."""
    res = verificar_palindromo(texto)
    return res['es_palindromo'], res['normalizado'], res['invertido']


def buscar_subcadena(texto, subcadena):
    """Búsqueda directa, sensible a mayúsculas, con coincidencias solapadas.

    Las posiciones empiezan en cero y corresponden siempre al texto original.
    Si la subcadena está vacía, retorna lista vacía sin error.
    """
    if not subcadena or not texto:
        return ResultadoBusqueda(posiciones=[], ocurrencias=0, comparaciones=0)

    posiciones = []
    comparaciones = 0
    for inicio in range(len(texto) - len(subcadena) + 1):
        coincide = True
        for desplazamiento, caracter in enumerate(subcadena):
            comparaciones += 1
            if texto[inicio + desplazamiento] != caracter:
                coincide = False
                break
        if coincide:
            posiciones.append(inicio)

    return ResultadoBusqueda(
        posiciones=posiciones,
        ocurrencias=len(posiciones),
        comparaciones=comparaciones
    )
