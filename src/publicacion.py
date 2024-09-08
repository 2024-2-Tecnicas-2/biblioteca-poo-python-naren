import sys
class Publicacion:
    def __init__(self, titulo, anio_publicacion):
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Año de publicación: {self.anio_publicacion}")
