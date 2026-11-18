# StringLab - Laboratorio Educativo de Cadenas, Teoría de Números y Autómatas

**Materia:** Lenguajes Formales y Autómatas  
**Proyecto:** Tema 4 — *Herramientas de Análisis de Cadenas y Teoría de Números*  
**Integrantes:** Vini, Sergio, José  

---

## 📖 Descripción General
**StringLab** es una aplicación web interactiva y didáctica desarrollada con **Python y Streamlit**. Su objetivo es permitir a los estudiantes de Lenguajes Formales y Autómatas comprender los fundamentos teóricos mediante visualizaciones y explicaciones **paso a paso**, demostrando cómo la teoría de números, el análisis de cadenas y los autómatas finitos convergen en la computación y la criptografía elemental.

---

## 👥 División del Equipo y Asignación de Módulos

Para garantizar un desarrollo ordenado y sin conflictos de código en Git, el proyecto se divide entre los 3 integrantes con ramas independientes:

```
                      ┌──────────────────────────────────────────────┐
                      │                 RAMA MAIN                    │
                      └──────────────────────┬───────────────────────┘
                                             │
             ┌───────────────────────────────┼──────────────────────────────┐
             │                               │                              │
             ▼                               ▼                              ▼
      ┌──────────────┐                ┌──────────────┐               ┌──────────────┐
      │  RAMA VINI   │                │ RAMA SERGIO  │               │  RAMA JOSÉ   │
      └──────┬───────┘                └──────┬───────┘               └──────┬───────┘
             │                               │                              │
    • Shell y Home (app.py)        • Módulo A: Analizador         • Módulo B: Teoría
    • Estilos CSS (styles.css)       de Cadenas                     de Números
    • Módulo C: Simulador de       • logic/cadenas.py             • logic/teoria_numeros.py
      Autómatas Finitos            • pages/1_Analizador...py      • pages/2_Teoria_num...py
    • logic/automatas.py                                          • Módulo D: Cifrado
    • pages/3_Simulador...py                                        Educativo (César)
                                                                  • logic/cifrado.py
                                                                  • pages/4_Cifrado...py
```

### 1. Vini (`rama: vini`)
* **Responsabilidad Principal:** Arquitectura base del proyecto y **Módulo C (Simulador de Autómatas Finitos)**.
* **Archivos asignados:**
  * `app.py`: Página de bienvenida, tarjetas de navegación y presentación del equipo.
  * `assets/styles.css`: Paleta visual celeste y blanco, estilos de tarjetas y diagramas.
  * `logic/automatas.py`: Definición formal de la 5-tupla $M = (Q, \Sigma, \delta, q_0, F)$, tablas de transición y lógica de simulación paso a paso para:
    1. Cadenas binarias terminadas en `01`.
    2. Cadenas binarias divisibles por 3.
  * `pages/3_Simulador_de_automatas.py`: Grafo interactivo del autómata, resaltado dinámico de estados, tabla de ejecución y control paso a paso.

---

### 2. Sergio (`rama: sergio`)
* **Responsabilidad Principal:** **Módulo A (Analizador de Cadenas)**.
* **Archivos asignados:**
  * `logic/cadenas.py`:
    * Conteo total de caracteres (especificando espacios).
    * Desglose: letras, vocales, consonantes, dígitos, espacios y símbolos.
    * Frecuencia de cada carácter.
    * Verificador de palíndromos (ignorando mayúsculas, espacios y signos, con explicación).
    * Algoritmo de búsqueda de subcadenas (posiciones y ocurrencias).
  * `pages/1_Analizador_de_cadenas.py`:
    * Interfaz con tarjetas métricas, tabla de frecuencias y vista con resaltado de coincidencias.
    * Sección educativa: *"¿Qué conceptos estoy aprendiendo?"*.

---

### 3. José (`rama: jose`)
* **Responsabilidad Principal:** **Módulo B (Laboratorio de Teoría de Números)** y **Módulo D (Cifrado Educativo)**.
* **Archivos asignados:**
  * `logic/teoria_numeros.py`:
    * Test de primalidad con lista de divisores probados paso a paso.
    * Algoritmo de Euclides para MCD con tabla de divisiones ($a = b \times q + r$).
    * Cálculo de MCM con fórmula $MCM(a,b) = \frac{|a \times b|}{MCD(a,b)}$.
    * Operación residuo/módulo y ejemplos interactivos de congruencias.
  * `pages/2_Teoria_de_numeros.py`:
    * Interfaz gráfica del laboratorio matemático con tablas paso a paso.
  * `logic/cifrado.py`:
    * Cifrado César ($C = (P + K) \pmod{26}$) y Descifrado ($P = (C - K) \pmod{26}$).
    * Desglose paso a paso letra por letra.
  * `pages/4_Cifrado_educativo.py`:
    * Tiras de alfabetos (original vs desplazado), controles de texto y clave $K$.
    * Sección educativa sobre aritmética modular en criptografía.

---

## 🛠️ Estructura del Proyecto

```text
stringlab/
├── app.py                          # Menú principal y bienvenida (Vini)
├── pages/
│   ├── 1_Analizador_de_cadenas.py  # Módulo A (Sergio)
│   ├── 2_Teoria_de_numeros.py      # Módulo B (José)
│   ├── 3_Simulador_de_automatas.py # Módulo C (Vini)
│   └── 4_Cifrado_educativo.py      # Módulo D (José)
├── logic/
│   ├── __init__.py
│   ├── cadenas.py                  # Lógica Módulo A (Sergio)
│   ├── teoria_numeros.py           # Lógica Módulo B (José)
│   ├── automatas.py                # Lógica Módulo C (Vini)
│   └── cifrado.py                  # Lógica Módulo D (José)
├── assets/
│   └── styles.css                  # Estilos visuales celeste/blanco (Vini)
├── tests/
│   ├── test_cadenas.py
│   ├── test_teoria_numeros.py
│   ├── test_automatas.py
│   └── test_cifrado.py
├── contexto/
│   ├── Contexto_StringLab_Antigravity.md
│   └── TEMAS DE PROYECTO.docx
├── DISTRIBUCION_DEL_PROYECTO.md
├── requirements.txt
└── README.md
```

---

## 🚀 Guía de Flujo de Trabajo en Git

Cada integrante trabajará en su propia rama y enviará sus cambios mediante Pull Request (PR) hacia `main`:

### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd "Proyecto de lenguaje formales y automatas"
```

### 2. Cambiarse a su rama asignada
* **Vini:** `git checkout vini`
* **Sergio:** `git checkout sergio`
* **José:** `git checkout jose`

### 3. Guardar cambios y subir a GitHub
```bash
git add .
git commit -m "feat(modulo): descripcion clara de lo implementado"
git push origin <tu-rama>
```

---

## 🎨 Criterios de Aceptación
1. **Foco educativo:** Cada cálculo o simulación debe mostrar su procedimiento paso a paso.
2. **Estilo:** Fondos claros, tonalidades celeste y blanco, tipografía legible.
3. **Validación:** No permitir entradas no válidas (división por cero, caracteres fuera del alfabeto binario en los autómatas, etc.).
4. **Independencia:** La aplicación se ejecuta de forma local sin dependencias externas complejas.
