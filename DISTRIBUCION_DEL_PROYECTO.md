# DISTRIBUCIÓN DEL PROYECTO: STRINGLAB
### Lenguajes Formales y Autómatas — Tema 4

Este documento establece la distribución formal del trabajo, responsabilidades técnicas y directrices para los tres integrantes del equipo: **Vini**, **Sergio** y **José**.

---

## 📌 Contexto del Proyecto

El proyecto corresponde al **Tema 4: Herramientas de Análisis de Cadenas y Teoría de Números**.
El objetivo es construir **StringLab**, una herramienta educativa interactiva con **Python y Streamlit** que permita a los estudiantes comprender cómo se relacionan las secuencias de texto, la aritmética elemental y los autómatas finitos.

### Reglas generales de desarrollo:
1. **Paso a paso:** Toda operación debe explicar o mostrar el procedimiento seguido (no solo el resultado final).
2. **Paleta visual:** Blanco y celeste, diseño limpio y minimalista.
3. **Manejo de errores:** Validar entradas de usuario para evitar caídas (cadenas vacías, caracteres fuera de $\Sigma$, división por cero).
4. **Sección didáctica:** Cada módulo debe contener el apartado final: *"¿Qué conceptos estoy aprendiendo?"*.

---

## 👥 Asignación por Integrante y Ramas

### 🔵 1. VINI — Rama `vini`
**Rol:** Líder técnico, Arquitectura general y Módulo de Autómatas Finitos.

#### Tareas asignadas:
1. **Configuración base (`app.py` y `assets/styles.css`):**
   * Estructura general de navegación de Streamlit.
   * Página principal de bienvenida con tarjetas de acceso rápido a los 4 módulos.
   * Hoja de estilos con la paleta celeste y blanco.
2. **Módulo C: Simulador de Autómatas Finitos (`logic/automatas.py` y `pages/3_Simulador_de_automatas.py`):**
   * Modelar formalmente la 5-tupla $M = (Q, \Sigma, \delta, q_0, F)$.
   * Implementar los dos autómatas obligatorios:
     * **Autómata 1:** Cadenas binarias terminadas en `01`.
     * **Autómata 2:** Cadenas binarias divisibles por 3 (estados $q_0, q_1, q_2$ correspondientes a los residuos).
   * Generar la tabla de transiciones formal.
   * Renderizar el grafo interactivo con Graphviz (círculos, doble círculo para aceptación, flechas etiquetadas).
   * Implementar simulación interactiva paso a paso (resaltando el estado activo y la tabla de ejecución).

---

### 🟢 2. SERGIO — Rama `sergio`
**Rol:** Especialista en Procesamiento de Secuencias y Análisis de Cadenas.

#### Tareas asignadas:
1. **Lógica de Cadenas (`logic/cadenas.py`):**
   * Conteo total de caracteres (con y sin espacios).
   * Conteo categorizado: letras, vocales, consonantes, dígitos, espacios y símbolos.
   * Frecuencia de caracteres (generación de diccionario / tabla de frecuencias).
   * Verificación de palíndromos (normalización: ignorando mayúsculas, espacios y signos).
   * Búsqueda de subcadenas (índices de inicio, longitud y total de ocurrencias).
2. **Interfaz del Módulo A (`pages/1_Analizador_de_cadenas.py`):**
   * Área de texto para ingresar o pegar cadenas de prueba.
   * Tarjetas métricas con los conteos.
   * Tabla o gráfico de frecuencias.
   * Componente visual con resaltado de las coincidencias de la subcadena en el texto.
   * Tarjeta explicativa sobre cómo se detectó el palíndromo y la subcadena.
   * Sección didáctica: *"¿Qué conceptos estoy aprendiendo?"*.

---

### 🟡 3. JOSÉ — Rama `jose`
**Rol:** Especialista en Teoría de Números y Criptografía Educativa.

#### Tareas asignadas:
1. **Módulo B: Laboratorio de Teoría de Números (`logic/teoria_numeros.py` y `pages/2_Teoria_de_numeros.py`):**
   * Test de primalidad paso a paso: listar divisores probados hasta $\lfloor\sqrt{n}\rfloor$ y justificar por qué es o no es primo.
   * Máximo Común Divisor (MCD): Algoritmo de Euclides con tabla detallada de divisiones ($a = b \cdot q + r$).
   * Mínimo Común Múltiplo (MCM): Demostración de la relación $MCM(a,b) = \frac{|a \cdot b|}{MCD(a,b)}$.
   * Aritmética modular: explicación de $a \pmod m$ y ejemplos didácticos de congruencias modulares ($a \equiv b \pmod m$).
   * Interfaz interactiva para el ingreso de números y visualización de pasos.
2. **Módulo D: Cifrado Educativo (`logic/cifrado.py` y `pages/4_Cifrado_educativo.py`):**
   * Cifrado César con la fórmula $C = (P + K) \pmod{26}$.
   * Descifrado César con la fórmula $P = (C - K) \pmod{26}$.
   * Visualización comparativa de los alfabetos (original vs desplazado).
   * Desglose paso a paso: tabla mostrando cada carácter original, su valor numérico $P$, la fórmula aplicada y el carácter resultante $C$.
   * Nota didáctica sobre el uso del alfabeto A-Z (sin Ñ) y la naturaleza clásica del algoritmo.
   * Sección didáctica: *"¿Qué conceptos estoy aprendiendo?"*.

---

## 🌿 Flujo de Trabajo en Git

1. Cada integrante trabajará **exclusivamente** en su rama asignada.
2. Antes de empezar una sesión de trabajo:
   ```bash
   git checkout <tu-rama>
   git pull origin <tu-rama>
   ```
3. Para guardar avances:
   ```bash
   git add .
   git commit -m "feat(modulo): avance detallado"
   git push origin <tu-rama>
   ```
4. Cuando un módulo esté listo y probado, se creará un **Pull Request (PR)** hacia la rama `main` para ser revisado e integrado.
