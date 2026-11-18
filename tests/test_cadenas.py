"""
Pruebas Unitarias del Módulo A: Analizador de Cadenas
Responsable: Sergio
"""

import unittest
from logic.cadenas import analizar_cadena, verificar_palindromo, es_palindromo, buscar_subcadena, frecuencia_caracteres

class TestModuloCadenas(unittest.TestCase):

    def test_analisis_basico(self):
        res = analizar_cadena("Hola 123")
        self.assertEqual(res["total"], 8)
        self.assertEqual(res["sin_espacios"], 7)
        self.assertEqual(res["letras"], 4)
        self.assertEqual(res["vocales"], 2)
        self.assertEqual(res["consonantes"], 2)
        self.assertEqual(res["digitos"], 3)
        self.assertEqual(res["espacios"], 1)

    def test_frecuencia_caracteres(self):
        freq = frecuencia_caracteres("banana")
        self.assertEqual(freq["a"], 3)
        self.assertEqual(freq["n"], 2)
        self.assertEqual(freq["b"], 1)

    def test_verificar_palindromo_positivo(self):
        res = verificar_palindromo("Anita lava la tina")
        self.assertTrue(res["es_palindromo"])
        self.assertTrue(res["evaluable"])
        self.assertGreater(len(res["pasos"]), 0)

    def test_verificar_palindromo_negativo(self):
        res = verificar_palindromo("Python")
        self.assertFalse(res["es_palindromo"])

    def test_buscar_subcadena(self):
        res = buscar_subcadena("abracadabra", "abra")
        self.assertEqual(res["posiciones"], [0, 7])
        self.assertEqual(res["ocurrencias"], 2)
        self.assertGreater(res["comparaciones"], 0)

    def test_compatibilidad_es_palindromo(self):
        es_pal, limpio, invertido = es_palindromo("reconocer")
        self.assertTrue(es_pal)
        self.assertEqual(limpio, "reconocer")
        self.assertEqual(invertido, "reconocer")

if __name__ == "__main__":
    unittest.main()
