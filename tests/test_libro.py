import sys
import os
import unittest
from io import StringIO
from unittest.mock import patch
from biblioteca import Publicacion, Libro, Revista

# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestLibro(unittest.TestCase):
    def test_constructor(self):
        libro = Libro("Test Libro", 2023, "Autor Test", 200)
        self.assertEqual(libro.titulo, "Test Libro")
        self.assertEqual(libro.anio_publicacion, 2023)
        self.assertEqual(libro.autor, "Autor Test")
        self.assertEqual(libro.numero_paginas, 200)

    def test_mostrar_info(self):
        libro = Libro("Test Libro", 2023, "Autor Test", 200)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            libro.mostrar_info()
            self.assertEqual(fake_out.getvalue().strip(), 
                             "Título: Test Libro\n"
                             "Año de publicación: 2023\n"
                             "Autor: Autor Test\n"
                             "Número de páginas: 200")
        
if __name__ == '__main__':
    unittest.main()
