import os 
#Agregar Docstrings
#Guardar archivos txt en una carpeta, salen todos en carpeta principal sin orden
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
    catalogos_creados = []
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = f"{nombre}.txt"
        self.peliculas = self.cargar_peliculas()
        
        # Verificar y crear el archivo si no existe
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'w', encoding='utf-8') as archivo:
                archivo.write("")  # Escribir un archivo vacío si es nuevo
        
        self.registrar_catalogo()
        
    def registrar_catalogo(self):
        if self.nombre not in CatalogoPeliculas.catalogos_creados:
            CatalogoPeliculas.catalogos_creados.append(self.nombre)
            print(f"\n==================================================")
            print(f"      Catálogo '{self.nombre}' creado.")
            print(f"==================================================")
        
    def listar_catalogos():
        if CatalogoPeliculas.catalogos_creados:
            print(f"\n==================================================")
            print(f"      Catálogos existentes:")
            print(f"==================================================")
            for catalogo in CatalogoPeliculas.catalogos_creados:
                print(f"      {catalogo}")
            print(f"==================================================")
        else: 
            print("No hay catálogos de películas creados")
           
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
        print ("\n==================================================")
        print(f"      Película '{pelicula.titulo}' agregada al catálogo.")
        print ("==================================================")
    
    def eliminar_pelicula(self, titulo):  
        pelicula_a_eliminar = None
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                pelicula_a_eliminar = pelicula
                break
        if pelicula_a_eliminar:
            self.peliculas.remove(pelicula_a_eliminar)
            ("\n==================================================")
            print(       f"Película '{titulo}' eliminada del catálogo.")
            ("\n==================================================")
        else:
            ("\n==================================================")
            print(       f"No se encontró la película '{titulo}' en el catálogo.")
            ("\n==================================================")
    
    def listar_peliculas(self):
        if self.peliculas:
            print("Catálogo de películas")
            for pelicula in self.peliculas:
                print(pelicula)
        else:
            ("\n==================================================")
            print(        "El Catálogo está vacío.")
            ("\n==================================================")
    def buscar_pelicula(self, titulo):
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                print("\nPelícula encontrada: ")
                print(pelicula)
                return
            else:
                print("\n==================================================")
                print(f"      No se encontró la película '{titulo}' en el catálogo.")
                print("==================================================")
            
    def actualizar_pelicula(self, titulo):
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                nuevo_director = input("Ingrese el nuevo director (dejar en blanco para mantener el actual): ")
                nuevo_año = input("Ingrese el nuevo año (dejar en blanco para mantener el actual): ")
                nuevo_genero = input("Ingrese el nuevo género (dejar en blanco para mantener el actual): ")
                nueva_calificacion = input("Ingrese la nueva calificación (dejar en blanco para mantener la actual): ")
                
                if nuevo_director:
                    pelicula.director = nuevo_director
                if nuevo_año:
                    pelicula.año = int(nuevo_año)
                if nuevo_genero:
                    pelicula.genero = nuevo_genero
                if nueva_calificacion:
                    pelicula.calificacion = float(nueva_calificacion)
                    
                print("\n==================================================")
                print(f"      Película '{titulo}' actualizada.")
                print("==================================================")
                return
            else:
                print("\n==================================================")
                print(f"      No se encontró la película '{titulo}' en el catálogo.")
                print("==================================================")
    def eliminar_catalogo(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            self.peliculas = []
            ("\n==================================================")
            print(      f"Catálogo '{self.nombre}' eliminado.")
            ("\n==================================================")
        else: 
            ("\n==================================================")
            print(         "El catálogo no existe.")
            ("\n==================================================")
    
class Funcionamientos():

    @staticmethod
    def mostrar_menu_principal():
        print("\nBienvenido al sistema de películas")
        print("1. Seleccionar Catálogo")
        print("2. Crear Nuevo Catálogo")
        print("3. Listar Catálogos")
        print("4. Salir")
        
    @staticmethod
    def mostrar_menu_catalogo():
        print("\nOpciones del catálogo")
        print("1. Agregar Película")
        print("2. Eliminar Película")
        print("3. Listar Películas")
        print("4. Buscar Película")
        print("5. Actualizar Película")
        print("6. Volver al Menú Principal")
        
    def seleccionar_catalogo():
        nombre_catalogo = input("Ingrese el nombre del catálogo de películas: ")
        if nombre_catalogo in CatalogoPeliculas.catalogos_creados:
            return CatalogoPeliculas(nombre_catalogo)
        else:
            print("\n==================================================")
            print(f"      No se encontró el catálogo '{nombre_catalogo}'.")
            print("==================================================")
            return None  
    
    @staticmethod
    def crear_catalogo():
        nombre_catalogo = input("Ingrese el nombre del catálogo de películas: ")
        if nombre_catalogo in CatalogoPeliculas.catalogos_creados:
            print("\n==================================================")
            print(f"      El catálogo '{nombre_catalogo}' ya existe.")
            print("==================================================")
            return None       
        else:
            return CatalogoPeliculas(nombre_catalogo)
    @staticmethod
    def main():
        print ("=============================================================================")
        print("                  ¡Bienvenido al Cátalogo de Películas! 🎥")
        print ("=============================================================================\n")
        
        catalogo_actual = None
        
        while True:
            if catalogo_actual:
                Funcionamientos.mostrar_menu_catalogo()
            else:
                Funcionamientos.mostrar_menu_principal()
                
            opcion = int(input("\nIngrese una opción: ")) #como sabe el usuario que debe digitar, no tiene sentido. Arreglar 
        
        if catalogo_actual:
            if opcion == 1:
                titulo = input("Ingrese el título de la película: ")
                director = input("Ingrese el director de la película: ")
                año = int(input("Ingrese el año de la película: "))
                genero = input("Ingrese el género de la película: ")
                calificacion = float(input("Ingrese la calificación de la película: "))
                pelicula = Pelicula(titulo, director, año, genero, calificacion)
                catalogo_actual.agregar_pelicula(pelicula)
            
            elif opcion == 2:
                titulo = input("Ingrese el título de la película a eliminar: ")
                catalogo_actual.eliminar_pelicula(titulo)
            elif opcion == 3:
                catalogo_actual.listar_peliculas()
            elif opcion == 4:
                titulo = input("Ingrese el título de la película a buscar")
                catalogo_actual.buscar_pelicula(titulo) 
            elif opcion == 5:
                titulo = input("Ingrese el título de la película a actualizar")
                catalogo_actual.actualizar.pelicula(titulo)
            elif opcion == '6':
                    catalogo_actual.guardar_peliculas()
                    catalogo_actual = None
            else:
                print("\n==================================================")
                print("      Opción no válida. Intente de nuevo.")
                print("==================================================")
        else:
            if opcion == '1':
                catalogo_actual = Funcionamientos.seleccionar_catalogo()
            elif opcion == '2':
                catalogo_actual = Funcionamientos.crear_catalogo()
            elif opcion == '3':
                CatalogoPeliculas.listar_catalogos()
            elif opcion == '4':
                print("\n==================================================")
                print("      Saliendo del programa. ¡Adiós!")
                print("==================================================")
                break #No sirve el programa por esto
            else:
                print("\n==================================================")
                print("      Opción no válida. Intente de nuevo.")
                print("==================================================")


if __name__ == "__main__":
    Funcionamientos()