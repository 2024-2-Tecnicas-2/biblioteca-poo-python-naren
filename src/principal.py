from src.libro import Libro
from src.publicacion import Publicacion
from src.revista import Revista


def main():
    
    print("Ingrese los datos de la Publicación:")
    titulo_publicacion = input("Título: ")
    anio_publicacion = int(input("Año de publicación: "))
    publicacion = Publicacion(titulo_publicacion, anio_publicacion)

    
    print("\nIngrese los datos del Libro:")
    titulo_libro = input("Título: ")
    anio_libro = int(input("Año de publicación: "))
    autor_libro = input("Autor: ")
    paginas_libro = int(input("Número de páginas: "))
    libro = Libro(titulo_libro, anio_libro, autor_libro, paginas_libro)

    
    print("\nIngrese los datos de la Revista:")
    titulo_revista = input("Título: ")
    anio_revista = int(input("Año de publicación: "))
    numero_revista = int(input("Número de revista: "))
    nombre_revista = input("Nombre de revista: ")
    revista = Revista(titulo_revista, anio_revista, numero_revista, nombre_revista)

    
    print("\nInformación de la Publicación:")
    publicacion.mostrar_info()
    print("\nInformación del Libro:")
    libro.mostrar_info()
    print("\nInformación de la Revista:")
    revista.mostrar_info()


if __name__ == "__main__":
    main()
