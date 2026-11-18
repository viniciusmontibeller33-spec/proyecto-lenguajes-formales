"""Operaciones del módulo A de StringLab, independientes de Streamlit."""

from collections import Counter
import unicodedata


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
    return {'total': len(texto), 'sin_espacios': len(texto) - conteo['espacios'],
            'espacios_simples': texto.count(' '), **conteo}


def frecuencia_caracteres(texto):
    """Frecuencias exactas, ordenadas de mayor a menor y luego por carácter."""
    return dict(sorted(Counter(texto).items(), key=lambda par: (-par[1], par[0])))


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
        pasos.append({'Paso': len(pasos) + 1, 'Índice izquierdo': izquierda,
                      'Carácter izquierdo': normalizado[izquierda],
                      'Índice derecho': derecha,
                      'Carácter derecho': normalizado[derecha],
                      'Resultado': 'Iguales' if iguales else 'Diferentes'})
        if not iguales:
            break
        izquierda += 1
        derecha -= 1
    return {'normalizado': normalizado, 'invertido': normalizado[::-1],
            'evaluable': bool(normalizado),
            'es_palindromo': bool(normalizado) and normalizado == normalizado[::-1],
            'pasos': pasos}


def buscar_subcadena(texto, subcadena):
    """Búsqueda directa, sensible a mayúsculas, con coincidencias solapadas.

    Las posiciones empiezan en cero y corresponden siempre al texto original.
    El patrón vacío se rechaza para evitar resultados ambiguos en la interfaz.
    """
    if not subcadena:
        raise ValueError('Escribí una subcadena no vacía.')
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
    return {'posiciones': posiciones, 'ocurrencias': len(posiciones),
            'comparaciones': comparaciones}
