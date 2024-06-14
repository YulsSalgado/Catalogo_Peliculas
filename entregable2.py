import os 
class Pelicula:
    
    def __init__(self, titulo, director, año, genero, calificacion):
        self.__titulo: titulo
        self.director: director
        self.año: año
        self.genero: genero
        self.calificacion: calificacion 
        
    @property
    def titulo(self):
        return self.__titulo
    
    def __str__(self):
        return (f"Título: {self.__titulo}, Director: {self.director}, "
                f"Año: {self.año}, Género: {self.genero}, Calificación: {self.calificacion}")
    
    def menu():
        print("Bienvenido al sistema de películas")
        print("1. Agregar película")
        print("2. Listar películas")
        print("3. Buscar película")
        print("4. Eliminar película")
        print("5. Salir")
        opcion = int(input("Ingrese una opción: "))
        return opcion
    
class CatalogoPeliculas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f"{nombre}.txt"
        self.peliculas = self.cargar_peliculas()
    
    def cargar_peliculas(self):
        peliculas = []
        
    def AgregarPelicula(self): 
        pass
