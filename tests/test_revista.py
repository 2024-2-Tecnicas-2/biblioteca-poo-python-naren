import sys
import os
import unittest
from io import StringIO
from unittest.mock import patch
from biblioteca import Publicacion, Libro, Revista

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestRevista(unittest.TestCase):
    def test_constructor(self):
        revista = Revista("Test Revista", 2023, 42, "Nombre Revista Test")
        self.assertEqual(revista.titulo, "Test Revista")
        self.assertEqual(revista.anio_publicacion, 2023)
        self.assertEqual(revista.numero_revista, 42)
        self.assertEqual(revista.nombre_revista, "Nombre Revista Test")

    def test_mostrar_info(self):
        revista = Revista("Test Revista", 2023, 42, "Nombre Revista Test")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            revista.mostrar_info()
            self.assertEqual(fake_out.getvalue().strip(), 
                             "Título: Test Revista\n"
                             "Año de publicación: 2023\n"
                             "Número de revista: 42\n"
                             "Nombre de revista: Nombre Revista Test")
        
if __name__ == '__main__':
    unittest.main()
