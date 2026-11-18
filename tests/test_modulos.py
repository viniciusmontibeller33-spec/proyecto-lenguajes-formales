"""
Pruebas Unitarias de StringLab
Verifica la lógica de los módulos con énfasis en el Módulo C (Autómatas - Vini).
"""

from logic.cadenas import analizar_cadena, es_palindromo, buscar_subcadena
from logic.teoria_numeros import es_primo_paso_a_paso, mcd_euclides_paso_a_paso, mcm_con_explicacion, operacion_modulo_explicada
from logic.automatas import afd_termina_01, afd_divisible_3, decimal_a_binario_info
from logic.cifrado import cifrar_cesar_paso_a_paso, descifrar_cesar_paso_a_paso

def test_modulo_a_cadenas():
    res = analizar_cadena("Hola 123")
    assert res["total_con_espacios"] == 8
    assert res["total_sin_espacios"] == 7
    assert res["letras"] == 4
    assert res["digitos"] == 3
    assert res["espacios"] == 1

    es_pal, _, _ = es_palindromo("Anita lava la tina")
    assert es_pal is True
    es_pal_no, _, _ = es_palindromo("Hola")
    assert es_pal_no is False

    pos = buscar_subcadena("abracadabra", "abra")
    assert pos == [0, 7]
    print("Módulo A: OK")

def test_modulo_b_teoria_numeros():
    es_p, _, _ = es_primo_paso_a_paso(29)
    assert es_p is True
    es_comp, _, _ = es_primo_paso_a_paso(25)
    assert es_comp is False

    mcd, pasos = mcd_euclides_paso_a_paso(252, 105)
    assert mcd == 21

    mcm, _, _ = mcm_con_explicacion(12, 18)
    assert mcm == 36

    r, q, _ = operacion_modulo_explicada(17, 5)
    assert r == 2
    assert q == 3
    print("Módulo B: OK")

def test_modulo_c_automatas():
    # 1. AFD Termina en '01'
    # Casos de aceptación
    assert afd_termina_01.simular("01")["aceptada"] is True
    assert afd_termina_01.simular("101")["aceptada"] is True
    assert afd_termina_01.simular("1101")["aceptada"] is True
    assert afd_termina_01.simular("10101")["aceptada"] is True

    # Casos de rechazo
    assert afd_termina_01.simular("10")["aceptada"] is False
    assert afd_termina_01.simular("111")["aceptada"] is False
    assert afd_termina_01.simular("100")["aceptada"] is False
    assert afd_termina_01.simular("")["aceptada"] is False  # Cadena vacía rechazada

    # Detección de símbolos inválidos y posición 1-based
    inv = afd_termina_01.simular("11a01")
    assert inv["exito"] is False
    assert inv["pos_error"] == 3
    assert inv["char_error"] == "a"

    # 2. AFD Divisible por 3
    # Múltiplos de 3 en binario (Aceptados)
    assert afd_divisible_3.simular("0")["aceptada"] is True      # 0
    assert afd_divisible_3.simular("11")["aceptada"] is True     # 3
    assert afd_divisible_3.simular("110")["aceptada"] is True    # 6
    assert afd_divisible_3.simular("1001")["aceptada"] is True   # 9
    assert afd_divisible_3.simular("1100")["aceptada"] is True   # 12
    assert afd_divisible_3.simular("1111")["aceptada"] is True   # 15

    # Ceros iniciales (Invariancia del valor 0)
    assert afd_divisible_3.simular("000")["aceptada"] is True
    assert afd_divisible_3.simular("0011")["aceptada"] is True

    # Cadena vacía formalmente aceptada (asociada a residuo 0)
    assert afd_divisible_3.simular("")["aceptada"] is True

    # No divisibles por 3 (Rechazados)
    assert afd_divisible_3.simular("1")["aceptada"] is False     # 1 mod 3 = 1
    assert afd_divisible_3.simular("10")["aceptada"] is False    # 2 mod 3 = 2
    assert afd_divisible_3.simular("100")["aceptada"] is False   # 4 mod 3 = 1
    assert afd_divisible_3.simular("101")["aceptada"] is False   # 5 mod 3 = 2

    # 3. Verificación de generación de Grafos DOT y Tablas
    dot_termina = afd_termina_01.generar_dot(estado_activo="q1", transicion_activa=("q0", "0", "q1"))
    assert "digraph AFD" in dot_termina
    assert "q1 [shape=" in dot_termina

    tabla_div3 = afd_divisible_3.obtener_tabla_transiciones_data()
    assert len(tabla_div3) == 3
    assert "Estado" in tabla_div3[0]

    # 4. Verificación de utilitario decimal
    info = decimal_a_binario_info("110")
    assert info["decimal"] == 6
    assert info["residuo"] == 0
    assert info["es_divisible"] is True

    print("Módulo C (Autómatas - Vini): OK y verificado al 100%")

def test_modulo_d_cifrado():
    cifrado, _ = cifrar_cesar_paso_a_paso("HOLA", 3)
    assert cifrado == "KROD"

    descifrado, _ = descifrar_cesar_paso_a_paso("KROD", 3)
    assert descifrado == "HOLA"
    print("Módulo D: OK")

if __name__ == "__main__":
    test_modulo_a_cadenas()
    test_modulo_b_teoria_numeros()
    test_modulo_c_automatas()
    test_modulo_d_cifrado()
    print("¡Todas las pruebas pasaron exitosamente!")
