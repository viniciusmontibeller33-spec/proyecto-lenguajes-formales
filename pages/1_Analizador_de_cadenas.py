from html import escape
from pathlib import Path
import sys

import streamlit as st

# Permite importar logic también al ejecutar esta página directamente.
RAIZ = Path(__file__).resolve().parents[1]
if str(RAIZ) not in sys.path:
    sys.path.insert(0, str(RAIZ))

from logic.cadenas import (analizar_cadena, buscar_subcadena,
                           frecuencia_caracteres, verificar_palindromo)


def nombre_caracter(caracter):
    nombres = {' ': '␠ Espacio', '\n': '↵ Salto de línea',
               '\t': '⇥ Tabulación', '\r': 'Retorno de carro'}
    if caracter in nombres:
        return nombres[caracter]
    return caracter if caracter.isprintable() else repr(caracter)


def resaltar_coincidencias(texto, posiciones, longitud):
    """Une intervalos solapados y escapa todo el contenido del usuario."""
    intervalos = []
    for inicio in posiciones:
        fin = inicio + longitud
        if intervalos and inicio <= intervalos[-1][1]:
            intervalos[-1][1] = max(intervalos[-1][1], fin)
        else:
            intervalos.append([inicio, fin])
    partes, anterior = [], 0
    for inicio, fin in intervalos:
        partes.append(escape(texto[anterior:inicio]))
        partes.append('<mark>' + escape(texto[inicio:fin]) + '</mark>')
        anterior = fin
    partes.append(escape(texto[anterior:]))
    return ''.join(partes)


st.title('Analizador de cadenas')
st.caption('Módulo A · StringLab · Sergio')
st.write('Explorá los caracteres de un texto y observá cómo funcionan los algoritmos.')
texto = st.text_area('Cadena de entrada', value='Anita lava la tina', height=130,
                     max_chars=10000, help='Máximo: 10 000 caracteres.')
st.caption('Las posiciones comienzan en 0. Se cuentan caracteres de Python; '
           'algunos emojis y acentos combinados pueden ocupar varias posiciones.')

if not texto:
    st.info('Escribí una cadena para comenzar. También podés analizar solo espacios.')

conteo = analizar_cadena(texto)
st.subheader('Conteo de caracteres')
columnas = st.columns(3)
for columna, etiqueta, valor in zip(columnas,
        ['Total con espacios', 'Total sin blancos', 'Espacios simples'],
        [conteo['total'], conteo['sin_espacios'], conteo['espacios_simples']]):
    columna.metric(etiqueta, valor)
columnas = st.columns(3)
for i, (clave, etiqueta) in enumerate([
        ('letras', 'Letras'), ('vocales', 'Vocales'), ('consonantes', 'Consonantes'),
        ('digitos', 'Dígitos'), ('espacios', 'Espacios y blancos'), ('simbolos', 'Símbolos')]):
    columnas[i % 3].metric(etiqueta, conteo[clave])
st.caption('Vocales y consonantes forman el total de letras. Las vocales con '
           'tilde y la ü cuentan como vocales. Los blancos incluyen espacios, '
           'tabulaciones y saltos de línea.')
with st.expander('Ver el procedimiento del conteo'):
    st.write('1. Recorrer la cadena carácter por carácter.\n'
             '2. Clasificar cada carácter como letra, dígito, blanco o símbolo.\n'
             '3. Si es letra, distinguir vocal de consonante.\n'
             '4. Sumar los contadores de cada categoría.')
    st.code(f"{conteo['letras']} letras + {conteo['digitos']} dígitos + "
            f"{conteo['espacios']} blancos + {conteo['simbolos']} símbolos "
            f"= {conteo['total']} caracteres", language='text')

st.subheader('Frecuencia de cada carácter')
frecuencias = frecuencia_caracteres(texto)
if frecuencias:
    st.dataframe([{'Carácter': nombre_caracter(c), 'Código Unicode': f'U+{ord(c):04X}',
                   'Frecuencia': n, 'Porcentaje': round(100 * n / len(texto), 2)}
                  for c, n in frecuencias.items()], hide_index=True,
                 use_container_width=True)
    st.caption('Se cuenta cada aparición. Mayúsculas y minúsculas se muestran por separado.')
else:
    st.write('No hay caracteres para contar.')

st.subheader('Verificador de palíndromos')
resultado = verificar_palindromo(texto)
st.write('Se ignoran mayúsculas, espacios y signos. Se conservan los acentos y los dígitos.')
st.text('Cadena normalizada: ' + resultado['normalizado'])
st.text('Cadena invertida: ' + resultado['invertido'])
if not resultado['evaluable']:
    st.info('Se necesita al menos una letra o un dígito para evaluar el palíndromo.')
elif resultado['es_palindromo']:
    st.success('Es un palíndromo: se lee igual en ambos sentidos.')
else:
    st.warning('No es un palíndromo: se encontró un par de caracteres diferentes.')
with st.expander('Ver comparaciones paso a paso'):
    st.write('Comparamos los extremos y avanzamos hacia el centro. '
             'Si un par es diferente, detenemos la comparación. '
             'Los índices de esta tabla pertenecen a la cadena normalizada.')
    if resultado['pasos']:
        st.dataframe(resultado['pasos'], hide_index=True, use_container_width=True)
    elif resultado['evaluable']:
        st.write('Un solo carácter es palíndromo; no requiere comparar pares.')

st.subheader('Búsqueda de subcadenas')
subcadena = st.text_input('Subcadena que querés buscar', max_chars=10000)
st.caption('La búsqueda distingue mayúsculas y acentos e incluye coincidencias solapadas.')
if subcadena:
    busqueda = buscar_subcadena(texto, subcadena)
    st.metric('Ocurrencias', busqueda['ocurrencias'])
    if busqueda['posiciones']:
        st.dataframe([{'Ocurrencia': i + 1, 'Inicio (desde 0)': inicio,
                       'Fin incluido (desde 0)': inicio + len(subcadena) - 1}
                      for i, inicio in enumerate(busqueda['posiciones'])],
                     hide_index=True, use_container_width=True)
        resaltado = resaltar_coincidencias(texto, busqueda['posiciones'], len(subcadena))
        st.markdown('<div style="white-space:pre-wrap;overflow-wrap:anywhere;'
                    'padding:1rem;background:#eff9ff;color:#16324f;'
                    'border:1px solid #bae6fd;border-radius:10px">'
                    + resaltado + '</div>', unsafe_allow_html=True)
        st.caption('El resaltado une las coincidencias que se superponen; '
                   'la tabla conserva cada ocurrencia por separado.')
    else:
        st.info('La subcadena no aparece en el texto.')
    with st.expander('Ver el algoritmo de búsqueda'):
        st.write('1. Alinear el patrón con cada posición posible del texto.\n'
                 '2. Comparar sus caracteres de izquierda a derecha.\n'
                 '3. Si todos coinciden, guardar la posición inicial.\n'
                 '4. Avanzar una posición, incluso después de encontrar una coincidencia.')
        st.write(f"Se realizaron {busqueda['comparaciones']} comparaciones de caracteres.")
        st.code('Texto: aaaa\nPatrón: aa\nPosiciones: 0, 1, 2\nOcurrencias: 3', language='text')
else:
    st.info('Escribí una subcadena no vacía para buscar.')

with st.expander('¿Qué conceptos estoy aprendiendo?', expanded=True):
    st.markdown('''
    - **Alfabeto:** conjunto de símbolos que pueden formar una cadena.
    - **Cadena y longitud:** secuencia de símbolos y cantidad de caracteres.
    - **Frecuencia:** cantidad de apariciones de cada carácter.
    - **Normalización:** reglas para comparar textos de manera uniforme.
    - **Palíndromos:** comparación de caracteres simétricos de una cadena.
    - **Subcadenas:** secuencias contiguas dentro de otra cadena.
    - **Complejidad:** el conteo recorre n caracteres, O(n); la búsqueda directa
      puede comparar hasta m caracteres en cada posición, O(n × m).
    ''')
