

import unittest
from miapp import MiClase  # Importa la clase que deseas probar

class TestMiApp(unittest.TestCase):
    def test_algo(self):
        # Escribe tu prueba aquí
        self.assertEqual(2 + 2, 4)

if __name__ == '__main__':
    unittest.main()

python -m unittest test_app.py

