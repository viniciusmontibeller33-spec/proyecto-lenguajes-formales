"""
Pruebas Unitarias de StringLab
Verifica la lógica de los 4 módulos contra los ejemplos del documento.
"""

from logic.cadenas import analizar_cadena, es_palindromo, buscar_subcadena
from logic.teoria_numeros import es_primo_paso_a_paso, mcd_euclides_paso_a_paso, mcm_con_explicacion, operacion_modulo_explicada
from logic.automatas import afd_termina_01, afd_divisible_3
from logic.cifrado import cifrar_cesar_paso_a_paso, descifrar_cesar_paso_a_paso

def test_modulo_a_cadenas():
    res = analizar_cadena("Hola 123")
    assert res["total_con_espacios"] == 8
    assert res["total_sin_espacios"] == 7
    assert res["letras"] == 4
    assert res["digitos"] == 3
    assert res["espacios"] == 1

    # Palindromo
    es_pal, _, _ = es_palindromo("Anita lava la tina")
    assert es_pal is True
    es_pal_no, _, _ = es_palindromo("Hola")
    assert es_pal_no is False

    # Subcadena
    pos = buscar_subcadena("abracadabra", "abra")
    assert pos == [0, 7]
    print("Módulo A: OK")

def test_modulo_b_teoria_numeros():
    # Primos
    es_p, _, _ = es_primo_paso_a_paso(29)
    assert es_p is True
    es_comp, _, _ = es_primo_paso_a_paso(25)
    assert es_comp is False

    # MCD Euclides
    mcd, pasos = mcd_euclides_paso_a_paso(252, 105)
    assert mcd == 21

    # MCM
    mcm, _, _ = mcm_con_explicacion(12, 18)
    assert mcm == 36

    # Modulo
    r, q, _ = operacion_modulo_explicada(17, 5)
    assert r == 2
    assert q == 3
    print("Módulo B: OK")

def test_modulo_c_automatas():
    # AFD termina en 01
    assert afd_termina_01.simular("01")["aceptada"] is True
    assert afd_termina_01.simular("101")["aceptada"] is True
    assert afd_termina_01.simular("1101")["aceptada"] is True
    assert afd_termina_01.simular("10")["aceptada"] is False
    assert afd_termina_01.simular("111")["aceptada"] is False
    assert afd_termina_01.simular("100")["aceptada"] is False

    # Simbolos invalidos
    inv = afd_termina_01.simular("1021")
    assert inv["exito"] is False

    # AFD divisible por 3
    # 0 en binario es 0 (divisible)
    assert afd_divisible_3.simular("0")["aceptada"] is True
    # 3 en binario es 11 (divisible)
    assert afd_divisible_3.simular("11")["aceptada"] is True
    # 6 en binario es 110 (divisible)
    assert afd_divisible_3.simular("110")["aceptada"] is True
    # 9 en binario es 1001 (divisible)
    assert afd_divisible_3.simular("1001")["aceptada"] is True
    # 4 en binario es 100 (no divisible)
    assert afd_divisible_3.simular("100")["aceptada"] is False
    # 5 en binario es 101 (no divisible)
    assert afd_divisible_3.simular("101")["aceptada"] is False
    print("Módulo C: OK")

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
