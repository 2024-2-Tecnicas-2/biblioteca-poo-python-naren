import sys
import os
import unittest
from io import StringIO
from unittest.mock import patch
from biblioteca import Publicacion, Libro, Revista

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestPublicacion(unittest.TestCase):
    def test_constructor(self):
        publicacion = Publicacion("Test Publicación", 2023)
        self.assertEqual(publicacion.titulo, "Test Publicación")
        self.assertEqual(publicacion.anio_publicacion, 2023)

    def test_mostrar_info(self):
        publicacion = Publicacion("Test Publicación", 2023)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            publicacion.mostrar_info()
            self.assertEqual(fake_out.getvalue().strip(), 
                             "Título: Test Publicación\n"
                             "Año de publicación: 2023")
        
if __name__ == '__main__':
    unittest.main()
