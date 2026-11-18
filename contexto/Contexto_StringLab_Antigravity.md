# Contexto del proyecto: StringLab

## 1. Descripción general

**StringLab** es una aplicación educativa sencilla e interactiva para
aprender y experimentar con conceptos de análisis de cadenas, teoría
elemental de números y autómatas finitos.

El proyecto corresponde al **Tema 4: Herramientas de Análisis de Cadenas
y Teoría de Números**, cuyo propósito es aplicar conceptos de teoría de
números integrados con autómatas para el procesamiento de secuencias y
la encriptación básica.

La aplicación debe priorizar la comprensión de los procedimientos: no
basta con mostrar un resultado, debe explicar y visualizar, paso a paso,
cómo se obtiene.

## 2. Objetivo general

Desarrollar una aplicación educativa que permita analizar cadenas de
caracteres, explorar operaciones básicas de teoría de números y simular
autómatas finitos, mostrando visualmente los pasos y resultados de cada
proceso.

## 3. Público y enfoque

-   Dirigida a estudiantes que están aprendiendo Lenguajes Formales y
    Autómatas.
-   Enfoque educativo, práctico y visual.
-   Interfaz sencilla, clara y fácil de utilizar.
-   No requiere cuentas de usuario, base de datos ni conexión a
    servicios externos.
-   Los textos, ejemplos y explicaciones deben estar en español.

## 4. Alcance funcional

La primera versión debe tener cuatro módulos principales.

### Módulo A: Analizador de cadenas

Permitir que el estudiante escriba o pegue una cadena de texto y obtenga
un análisis básico.

Funciones: - Contar caracteres totales. - Contar letras, vocales,
consonantes, dígitos, espacios y símbolos. - Mostrar la frecuencia de
cada carácter. - Comprobar si la cadena es un palíndromo. - Buscar una
subcadena dentro del texto e indicar si aparece y en qué posiciones.

Visualización: - Mostrar los resultados en tarjetas o una tabla
sencilla. - Resaltar visualmente los caracteres o coincidencias cuando
corresponda. - Incluir una explicación breve de cómo se realiza cada
análisis.

Consideraciones: - Definir claramente si los espacios se incluyen en el
total de caracteres. - Para el palíndromo, ignorar mayúsculas, espacios
y signos de puntuación, e indicarlo en la interfaz. - Evitar que una
cadena vacía produzca resultados engañosos.

### Módulo B: Laboratorio de teoría de números

Ofrecer operaciones elementales con números enteros positivos.

Funciones: - Determinar si un número es primo. - Calcular el máximo
común divisor (MCD). - Calcular el mínimo común múltiplo (MCM). -
Calcular el residuo de una división y explicar la operación módulo. -
Mostrar ejemplos de congruencia modular.

Visualización: - Explicar el procedimiento paso a paso. - Para números
primos, mostrar los divisores probados o explicar por qué no se
encontraron divisores. - Para MCD, mostrar el algoritmo de Euclides
mediante una tabla de divisiones. - Para MCM, mostrar la relación
`MCM(a,b) = |a × b| / MCD(a,b)`. - Para módulo, mostrar una operación
como `17 mod 5 = 2` y explicar que 17 = 5 × 3 + 2.

Validaciones: - Aceptar únicamente números enteros dentro de un rango
razonable. - Informar cuando falten datos o se introduzcan valores no
válidos. - Evitar división entre cero.

### Módulo C: Simulador de autómatas finitos

Este módulo es central para relacionar el proyecto con Lenguajes
Formales y Autómatas.

Implementar inicialmente autómatas finitos deterministas (AFD)
predefinidos. No es necesario construir un editor complejo de autómatas
en la primera versión.

Autómatas sugeridos: 1. **Cadenas binarias que terminan en `01`.** -
Alfabeto: `{0, 1}`. - Acepta ejemplos como `01`, `101` y `1101`. -
Rechaza ejemplos como `10`, `111` y `100`.

2.  **Números binarios divisibles por 3.**
    -   Alfabeto: `{0, 1}`.
    -   El autómata debe reconocer las representaciones binarias de
        números divisibles por 3.
    -   Explicar que cada estado representa el residuo que se obtiene al
        dividir el valor leído entre 3.
    -   Usar como estados los residuos 0, 1 y 2; el estado inicial y de
        aceptación corresponde al residuo 0.
    -   Definir y documentar el tratamiento de la cadena vacía y de los
        ceros iniciales.

Funciones: - Permitir seleccionar un autómata. - Permitir introducir una
cadena para evaluarla. - Validar que la entrada utilice únicamente
símbolos del alfabeto. - Ejecutar la simulación paso a paso y también
permitir avanzar automáticamente si resulta sencillo implementarlo. -
Mostrar el estado inicial, cada transición, el estado final y si la
cadena es aceptada o rechazada. - Permitir reiniciar la simulación.

Visualización: - Dibujar los estados como círculos y las transiciones
como flechas etiquetadas. - Resaltar el estado actual durante cada
paso. - Diferenciar visualmente los estados de aceptación. - Mostrar una
tabla de ejecución con: posición, símbolo leído, estado anterior y
estado siguiente. - Si la cadena es inválida, indicar en qué posición se
encontró el símbolo no permitido.

La representación gráfica debe mantenerse sincronizada con la tabla y
con el avance de la simulación.

### Módulo D: Cifrado educativo

Implementar un cifrado César para mostrar una aplicación sencilla de la
aritmética modular.

Funciones: - Escribir un mensaje. - Elegir una clave de
desplazamiento. - Cifrar el mensaje. - Descifrar un mensaje previamente
cifrado. - Mostrar el alfabeto original y el alfabeto desplazado. -
Explicar el cálculo realizado para cada letra.

Fórmulas para el alfabeto inglés de 26 letras:

-   Cifrado: `C = (P + K) mod 26`
-   Descifrado: `P = (C - K) mod 26`

Donde: - `P` es la posición numérica de la letra original. - `C` es la
posición numérica de la letra cifrada. - `K` es la clave de
desplazamiento.

Ejemplo: - Texto: `HOLA` - Clave: `3` - Resultado: `KROD`

Consideraciones: - Explicar que se utiliza un alfabeto de 26 letras. -
Mantener los espacios y signos de puntuación sin cambios. - Definir cómo
tratar la letra Ñ. Para simplificar, utilizar inicialmente el alfabeto
A-Z y advertirlo en la interfaz. - Aclarar que César es un método
clásico con fines didácticos y no protege información real.

## 5. Relación entre los módulos

La aplicación debe mostrar que los temas están conectados:

-   El análisis de cadenas trabaja con secuencias de símbolos.
-   Los autómatas reconocen si una secuencia pertenece a un lenguaje
    definido.
-   La teoría de números aporta operaciones como divisibilidad y
    aritmética modular.
-   El cifrado César utiliza aritmética modular para transformar
    caracteres.

Incluir una pequeña sección de **"¿Qué conceptos estoy aprendiendo?"**
en cada módulo, con una explicación breve de su relación con la materia.

## 6. Interfaz y experiencia de usuario

Diseñar una interfaz web sencilla, moderna y adaptable a escritorio y
móvil.

Estructura sugerida: - Barra lateral o menú superior con el nombre
StringLab. - Inicio con una breve descripción y tarjetas para acceder a
los cuatro módulos. - Cada módulo debe tener título, explicación breve,
controles de entrada, botón para ejecutar y área de resultados. -
Mantener navegación clara y consistente. - Incluir ejemplos precargados
para que el estudiante pueda probar cada herramienta. - Mostrar mensajes
de error comprensibles y mensajes de resultado claros.

Estilo visual: - Fondo claro. - Colores principales: celeste y blanco. -
Texto negro o gris oscuro para facilitar la lectura. - Utilizar el
celeste para botones, estados activos y elementos destacados. - Evitar
exceso de animaciones, adornos o elementos visuales que distraigan. -
Usar diagramas limpios y etiquetas legibles.

## 7. Tecnología recomendada

Para mantener el proyecto simple, se recomienda:

-   **Python** como lenguaje principal.
-   **Streamlit** para construir la interfaz web.
-   **Graphviz** para representar los autómatas y sus transiciones.

La aplicación debe ejecutarse localmente. No necesita backend
independiente, autenticación, base de datos ni despliegue en internet
para la primera versión.

Si Graphviz no está disponible en el entorno, implementar una
alternativa visual sencilla o explicar qué dependencia falta; no dejar
el módulo de autómatas inutilizable.

## 8. Requisitos no funcionales

-   Facilidad de uso para estudiantes principiantes.
-   Resultados correctos y reproducibles.
-   Validación de entradas.
-   Explicaciones en español y con lenguaje académico sencillo.
-   Código organizado por módulos y funciones reutilizables.
-   Interfaz adaptable a diferentes tamaños de pantalla.
-   No almacenar los textos introducidos por el usuario.
-   No utilizar servicios externos ni enviar datos a internet.

## 9. Organización sugerida del código

Separar la lógica de los componentes visuales. Una estructura posible:

``` text
stringlab/
├── app.py
├── pages/
│   ├── 1_Analizador_de_cadenas.py
│   ├── 2_Teoria_de_numeros.py
│   ├── 3_Simulador_de_automatas.py
│   └── 4_Cifrado_educativo.py
├── logic/
│   ├── cadenas.py
│   ├── teoria_numeros.py
│   ├── automatas.py
│   └── cifrado.py
├── assets/
│   └── styles.css
├── requirements.txt
└── README.md
```

Puedes ajustar la estructura si Streamlit requiere otra organización,
pero conserva la separación entre lógica y presentación.

## 10. Criterios de aceptación

La primera versión se considerará funcional cuando:

1.  El estudiante pueda analizar una cadena y visualizar sus
    características.
2.  Pueda ejecutar operaciones de números primos, MCD, MCM y módulo,
    viendo los pasos.
3.  Pueda seleccionar un AFD, introducir una cadena y observar cada
    transición.
4.  Pueda cifrar y descifrar un texto con César y ver cómo se transforma
    cada letra.
5.  Los resultados coincidan con los ejemplos de prueba.
6.  Las entradas inválidas generen mensajes claros y no bloqueen la
    aplicación.
7.  La navegación entre los módulos funcione correctamente.
8.  La aplicación incluya instrucciones para instalar dependencias y
    ejecutarse localmente.

## 11. Fuera del alcance de la primera versión

Para evitar que el proyecto se vuelva demasiado grande, NO implementar
inicialmente:

-   Registro e inicio de sesión.
-   Base de datos.
-   Cifrado RSA completo.
-   Criptografía moderna o protección de información real.
-   Editor visual para crear autómatas personalizados.
-   Autómatas no deterministas o autómatas a pila.
-   Aplicación móvil nativa.
-   Integraciones con servicios externos.

Estas funciones podrían considerarse como mejoras futuras, únicamente
después de completar y probar la versión básica.

## 12. Instrucciones para el agente de desarrollo

Construye la aplicación por etapas y prioriza que cada módulo funcione
antes de agregar el siguiente.

Orden recomendado: 1. Crear la estructura del proyecto y la navegación.
2. Implementar y probar la lógica del analizador de cadenas. 3.
Implementar y probar las operaciones de teoría de números. 4.
Implementar los AFD y la simulación paso a paso. 5. Implementar el
cifrado y descifrado César. 6. Integrar el diseño visual y revisar la
adaptación a diferentes pantallas. 7. Ejecutar pruebas con los ejemplos
y corregir errores. 8. Documentar la instalación y el uso en el README.

Antes de terminar, verifica que: - Todos los botones realicen la acción
indicada. - Las transiciones del autómata sean correctas. - Los estados
y la tabla de ejecución coincidan. - Las operaciones matemáticas
contemplen casos límite. - El cifrado y descifrado recuperen
correctamente el texto original. - No existan páginas vacías, controles
decorativos sin funcionalidad ni errores de ejecución.

**Resultado esperado:** una aplicación educativa pequeña, funcional y
visual que permita comprender la relación entre análisis de cadenas,
teoría de números, autómatas finitos y encriptación básica.
