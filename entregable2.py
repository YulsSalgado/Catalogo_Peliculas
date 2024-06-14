import os 
class Pelicula:
    
    def __init__(self, titulo, director, año, genero, calificacion):
        self.__titulo = titulo
        self.director =director
        self.año = año
        self.genero = genero
        self.calificacion = calificacion 
        
    @property
    def titulo(self):
        return self.__titulo
    
    def __str__(self):
        return (f"Título: {self.__titulo}, Director: {self.director}, "
                f"Año: {self.año}, Género: {self.genero}, Calificación: {self.calificacion}")
    
class CatalogoPeliculas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f"{nombre}.txt"
        self.peliculas = self.cargar_peliculas()
    
    def cargar_peliculas(self):
        peliculas = []
        if os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'r', encoding= 'utf-8') as archivo:
                for linea in archivo:
                    if linea.strip(): # Verifica que la línea no esté vacía
                        titulo, director, año, genero, calificacion = linea.strip().split(',')
                        peliculas.append(Pelicula(titulo, director, int(año), genero, float(calificacion)))
        return peliculas 
        
    def guardar_peliculas(self): 
        with open(self.ruta_archivo, 'w', encoding = 'utf-8') as archivo:
            for pelicula in self.peliculas:
                archivo.write(f"{pelicula.titulo}, {pelicula.director}, {pelicula.año}, {pelicula.genero}, {pelicula.calificacion}\n")
    
    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)
        print(f"Película '{pelicula.titulo}' agregada al catálogo.")
    
    def eliminar_pelicula(self, titulo):  
        pelicula_a_eliminar = None
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                pelicula_a_eliminar = pelicula
                break
        if pelicula_a_eliminar:
            self.peliculas.remove(pelicula_a_eliminar)
            print(f"Película '{titulo}' eliminada del catálogo.")
        else:
            print(f"No se encontró la película '{titulo}' en el catálogo.")
    
    def listar_peliculas(self):
        if self.peliculas:
            print("Catálogo de películas")
            for pelicula in self.peliculas:
                print(pelicula)
        else: 
            print("El Catálogo está vacío.")
            
    def eliminar_catalogo(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            self.peliculas = []
            print(f"Catálogo '{self.nombre}' eliminado.")
        else: 
            print("El catálogo no existe.")
    
def mostrar_menu():
    print("\nBienvenido al sistema de películas")
    print("1. Agregar Película")
    print("2. Eliminar Película")
    print("3. Listar Película")
    print("4. Eliminar Catálogo")
    print("5. Salir")
    
def main():
    nombre_catalogo = input("Ingrese el nombre del catálogo de películas: ")
    catalogo = CatalogoPeliculas(nombre_catalogo) 

    while True:
        mostrar_menu()
        opcion = int(input("\nIngrese una opción: "))
        
        if opcion == 1:
            titulo = input("Ingrese el título de la película: ")
            director = input("Ingrese el director de la película: ")
            año = int(input("Ingrese el año de la película: "))
            genero = input("Ingrese el género de la película: ")
            calificacion = float(input("Ingrese la calificación de la película: "))
            pelicula = Pelicula(titulo, director, año, genero, calificacion)
            catalogo.agregar_pelicula(pelicula)
        elif opcion == 2:
            titulo = input("Ingrese el título de la película a eliminar: ")
            catalogo.eliminar_pelicula(titulo)
        elif opcion == 3:
            catalogo.listar_peliculas()
        elif opcion == 4:
            catalogo.eliminar_catalogo()
        elif opcion == 5:
            catalogo.guardar_peliculas()
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()