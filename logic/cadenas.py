"""
Módulo A: Lógica del Analizador de Cadenas
Responsable: Sergio (Rama: sergio)
"""

from collections import Counter
import re
import unicodedata

def analizar_cadena(texto: str):
    """
    Analiza una cadena de texto y retorna estadísticas básicas.
    """
    total_con_espacios = len(texto)
    total_sin_espacios = len(texto.replace(" ", ""))
    
    letras = sum(1 for c in texto if c.isalpha())
    digitos = sum(1 for c in texto if c.isdigit())
    espacios = sum(1 for c in texto if c.isspace())
    simbolos = total_con_espacios - (letras + digitos + espacios)
    
    vocales = sum(1 for c in texto.lower() if c in "aeiouáéíóúü")
    consonantes = sum(1 for c in texto.lower() if c.isalpha() and c not in "aeiouáéíóúü")
    
    frecuencias = dict(Counter(texto))
    
    return {
        "total_con_espacios": total_con_espacios,
        "total_sin_espacios": total_sin_espacios,
        "letras": letras,
        "vocales": vocales,
        "consonantes": consonantes,
        "digitos": digitos,
        "espacios": espacios,
        "simbolos": simbolos,
        "frecuencias": frecuencias
    }

def es_palindromo(texto: str):
    """
    Comprueba si una cadena es palíndromo ignorando mayúsculas, espacios y signos.
    """
    if not texto.strip():
        return False, "", "Cadena vacía"
        
    # Normalizar quitando acentos y signos
    texto_norm = unicodedata.normalize('NFD', texto)
    texto_limpio = ''.join(c.lower() for c in texto_norm if c.isalnum())
    
    invertido = texto_limpio[::-1]
    es_igual = (texto_limpio == invertido) and len(texto_limpio) > 0
    
    return es_igual, texto_limpio, invertido

def buscar_subcadena(texto: str, patron: str):
    """
    Busca todas las apariciones de una subcadena e indica sus posiciones (1-based e 0-based).
    """
    if not patron or not texto:
        return []
        
    posiciones = []
    inicio = 0
    while True:
        pos = texto.find(patron, inicio)
        if pos == -1:
            break
        posiciones.append(pos)
        inicio = pos + 1
        
    return posiciones
