from src.publicacion import Publicacion


class Libro(Publicacion):
    def __init__(self, titulo, anio_publicacion, autor, numero_paginas):
        super().__init__(titulo, anio_publicacion)
        self.autor = autor
        self.numero_paginas = numero_paginas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.numero_paginas}")
    
