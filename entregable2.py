import os 

class Pelicula:
    
    def __init__(self, titulo, director, año, genero, calificacion):
        self.__titulo: titulo
        self.director: director
        self.año: año
        self.genero: genero
        self.calificacion: calificacion 
    
    def __str__(self):
        return f"Título: {self.titulo}, Director: {self.director}, Año: {self.año}, Género: {self.genero}"
    
    def menu():
        print("Bienvenido al sistema de películas")
        print("1. Agregar película")
        print("2. Listar películas")
        print("3. Buscar película")
        print("4. Eliminar película")
        print("5. Salir")
        opcion = int(input("Ingrese una opción: "))
        return opcion
    
class Catalogo:
    def __init__(self):
        self.peliculas = []
        
    def AgregarPelicula(self): 
        pass
