import unittest
from math_utils import es_primo, suma, resta, multiplica, divide


class TestMathUtils(unittest.TestCase):

    def test_es_primo_negativo(self):
        self.assertEqual(es_primo(-1), 'No es posible devolver números primos.')
        self.assertEqual(es_primo(-5), 'No es posible devolver números primos.')
        self.assertEqual(es_primo(-10), 'No es posible devolver números primos.')
        self.assertEqual(es_primo(-15), 'No es posible devolver números primos.')

    def test_es_primo_cero(self):
        self.assertFalse(es_primo(0))

    def test_es_primo_num(self):
        self.assertFalse(es_primo(1))
        self.assertFalse(es_primo(4))
        self.assertFalse(es_primo(6))
        self.assertFalse(es_primo(8))

    def test_es_primo_dos(self):
        self.assertTrue(es_primo(2))

    def test_es_primo_tres(self):
        self.assertTrue(es_primo(3))

    def test_es_primo_cuatro(self):
        self.assertFalse(es_primo(4))

    def test_es_primo_grande(self):
        self.assertTrue(es_primo(29))

    def test_suma_positivos(self):
        self.assertEqual(suma(3, 4), 7)

    def test_suma_negativos(self):
        self.assertEqual(suma(-3, -4), -7)

    def test_suma_mixtos(self):
        self.assertEqual(suma(-3, 4), 1)

    def test_suma_cero(self):
        self.assertEqual(suma(0, 0), 0)

    # Tests para resta
    def test_resta_positivos(self):
        self.assertEqual(resta(10, 4), 6)

    def test_resta_negativos(self):
        self.assertEqual(resta(-10, -4), -6)

    def test_resta_mixtos(self):
        self.assertEqual(resta(-10, 4), -14)

    def test_resta_cero(self):
        self.assertEqual(resta(0, 0), 0)

    # Tests para multiplica
    def test_multiplica_positivos(self):
        self.assertEqual(multiplica(3, 4), 12)

    def test_multiplica_negativos(self):
        self.assertEqual(multiplica(-3, -4), 12)

        def test_multiplica_mixtos(self):
            self.assertEqual(multiplica(-3, 4), -12)

    def test_multiplica_cero(self):
        self.assertEqual(multiplica(3, 0), 0)

        # Tests para divide

    def test_divide_positivos(self):
        self.assertEqual(divide(8, 4), 2)

    def test_divide_negativos(self):
        self.assertEqual(divide(-8, -4), 2)

    def test_divide_mixtos(self):
        self.assertEqual(divide(-8, 4), -2)

    def test_divide_cero(self):
        self.assertEqual(divide(8, 0), 'No se puede dividir por cero.')

    if __name__ == '__main__':
        unittest.main()


if __name__ == '__main__':
    unittest.main()
