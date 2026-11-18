import unittest
from logic.teoria_numeros import (
    es_primo_paso_a_paso,
    mcd_euclides_paso_a_paso,
    mcm_con_explicacion,
    operacion_modulo_explicada,
    verificar_congruencia
)

class TestTeoriaNumeros(unittest.TestCase):
    def test_primos(self):
        # 1 y menores no son primos
        es_p, _, _ = es_primo_paso_a_paso(1)
        self.assertFalse(es_p)
        
        es_p, _, _ = es_primo_paso_a_paso(0)
        self.assertFalse(es_p)
        
        # 2 y 3 son primos
        es_p, _, _ = es_primo_paso_a_paso(2)
        self.assertTrue(es_p)
        
        es_p, _, _ = es_primo_paso_a_paso(3)
        self.assertTrue(es_p)
        
        # Compuestos
        es_p, _, _ = es_primo_paso_a_paso(4)
        self.assertFalse(es_p)
        
        es_p, _, _ = es_primo_paso_a_paso(29)
        self.assertTrue(es_p)
        
        es_p, _, _ = es_primo_paso_a_paso(100)
        self.assertFalse(es_p)

    def test_mcd_euclides(self):
        mcd, pasos = mcd_euclides_paso_a_paso(252, 105)
        self.assertEqual(mcd, 21)
        self.assertGreater(len(pasos), 0)
        
        mcd, _ = mcd_euclides_paso_a_paso(17, 13)
        self.assertEqual(mcd, 1)

    def test_mcm(self):
        mcm, mcd, _ = mcm_con_explicacion(12, 18)
        self.assertEqual(mcd, 6)
        self.assertEqual(mcm, 36)
        
        mcm_cero, _, _ = mcm_con_explicacion(0, 10)
        self.assertEqual(mcm_cero, 0)

    def test_modulo(self):
        res, coc, _ = operacion_modulo_explicada(17, 5)
        self.assertEqual(res, 2)
        self.assertEqual(coc, 3)
        
        with self.assertRaises(ZeroDivisionError):
            operacion_modulo_explicada(10, 0)

    def test_congruencia(self):
        # 38 ≡ 14 (mod 12) es verdadero porque 38 % 12 == 2 y 14 % 12 == 2
        res = verificar_congruencia(38, 14, 12)
        self.assertTrue(res["es_congruente"])
        self.assertEqual(res["res_a"], 2)
        self.assertEqual(res["res_b"], 2)
        
        # 17 ≡ 5 (mod 7) es falso porque 17 % 7 = 3 != 5 % 7 = 5
        res_falsa = verificar_congruencia(17, 5, 7)
        self.assertFalse(res_falsa["es_congruente"])

if __name__ == "__main__":
    unittest.main()
