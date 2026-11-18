import unittest
from logic.cifrado import (
    cifrar_cesar_paso_a_paso,
    descifrar_cesar_paso_a_paso,
    obtener_alfabeto_desplazado,
    ALFABETO
)

class TestCifradoCesar(unittest.TestCase):
    def test_alfabeto_desplazado(self):
        orig, desp = obtener_alfabeto_desplazado(3)
        self.assertEqual(orig, ALFABETO)
        self.assertEqual(desp[:3], "DEF")
        self.assertEqual(desp[-3:], "ABC")

    def test_cifrado_basico(self):
        texto = "HOLA"
        cifrado, pasos = cifrar_cesar_paso_a_paso(texto, 3)
        self.assertEqual(cifrado, "KROD")
        self.assertEqual(len(pasos), 4)

    def test_descifrado_basico(self):
        texto_cifrado = "KROD"
        descifrado, pasos = descifrar_cesar_paso_a_paso(texto_cifrado, 3)
        self.assertEqual(descifrado, "HOLA")
        self.assertEqual(len(pasos), 4)

    def test_inversibilidad(self):
        original = "LENGUAJES FORMALES 2026!"
        cifrado, _ = cifrar_cesar_paso_a_paso(original, 7)
        descifrado, _ = descifrar_cesar_paso_a_paso(cifrado, 7)
        self.assertEqual(descifrado, original)

    def test_preservacion_signos_y_espacios(self):
        texto = "HOLA, MUNDO 123"
        cifrado, pasos = cifrar_cesar_paso_a_paso(texto, 3)
        self.assertEqual(cifrado, "KROD, PXQGR 123")
        
        # Verificar que la coma y espacio conserven "No aplica"
        self.assertEqual(pasos[4]["formula"], "No aplica (símbolo conservado)")

    def test_desplazamiento_modulo_26(self):
        # Desplazamiento de 26 no cambia el texto
        cifrado, _ = cifrar_cesar_paso_a_paso("ABC", 26)
        self.assertEqual(cifrado, "ABC")
        
        # Desplazamiento de 29 es equivalente a 3 (29 % 26 = 3)
        cifrado_29, _ = cifrar_cesar_paso_a_paso("ABC", 29)
        cifrado_3, _ = cifrar_cesar_paso_a_paso("ABC", 3)
        self.assertEqual(cifrado_29, cifrado_3)

if __name__ == "__main__":
    unittest.main()
