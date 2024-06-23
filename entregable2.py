import os 
import shutil #Módulo para hacer movimientos en la papelera

class Pelicula:
    """
    Representa una película con título, director, año, género y calificación.
    """
    
    def __init__(self, titulo, director, año, genero, calificacion):
        self.__titulo = titulo
        self.director =director
        self.año = año
        self.genero = genero
        self.calificacion = calificacion 
        
    @property
    def titulo(self):
        """
        Devuelve el título de la película, accediendo al atributo privado.
        """
        return self.__titulo
    
    def __str__(self):
        """
        Devuelve una representación en forma de cadena de la película.
        """
        return (f"Título: {self.__titulo}, Director: {self.director}, "
                f"Año: {self.año}, Género: {self.genero}, Calificación: {self.calificacion}")
    
class CatalogoPeliculas:
    """
    Representa un catálogo de películas con muchos métodos.
    """
    catalogos_creados = []
    
    def __init__(self, nombre, nuevo=True):
        """
        Iniciar una nueva instancia del catálogo de películas.

        Parámetros:
        nombre (str): El nombre que tendrá el catálogo.
        nuevo (bool, opcional): Indica si el catálogo es nuevo. Su modo por default es True.
        """
        
        self.nombre = nombre        
        self.carpeta_catalogos = "Catálogos creados"
        self.ruta_catalogo = os.path.join(self.carpeta_catalogos, nombre)
        os.makedirs(self.ruta_catalogo, exist_ok=True) #Crear subcarpeta dentro de catalogo principal
        self.peliculas = self.cargar_peliculas() #Iniciar la lista de peliculas        
       
        if nuevo: #Asegurar que se diferencie registrar y seleccionar catalogos
            self.registrar_catalogo()
        
    def registrar_catalogo(self):
        if self.nombre not in CatalogoPeliculas.catalogos_creados:
            CatalogoPeliculas.catalogos_creados.append(self.nombre)
            print(f"\n==============================")
            print(f"Catálogo '{self.nombre}' creado.")
            print(f"================================")       
           
    def cargar_peliculas(self):
        peliculas = []
        for archivo in os.listdir(self.ruta_catalogo):
            if archivo.endswith(".txt"):
                ruta_pelicula = os.path.join(self.ruta_catalogo, archivo)
                with open(ruta_pelicula, 'r', encoding='utf-8') as archivo_pelicula:
                    titulo, director, año, genero, calificacion = archivo_pelicula.read().strip().split(',')
                    peliculas.append(Pelicula(titulo, director, int(año), genero, float(calificacion)))
        return peliculas
        
    def guardar_peliculas(self):
        for pelicula in self.peliculas:
            ruta_pelicula = os.path.join(self.ruta_catalogo, f"{pelicula.titulo}.txt")
            with open(ruta_pelicula, 'w', encoding = 'utf-8') as archivo:
                archivo.write(f"{pelicula.titulo}, {pelicula.director}, {pelicula.año}, {pelicula.genero}, {pelicula.calificacion}\n")
    
    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)
        self.guardar_peliculas()
        print ("\n================================================")
        print(f"Película '{pelicula.titulo}' agregada al catálogo.")
        print ("==================================================")
    
    def eliminar_pelicula(self, titulo):  
        pelicula_a_eliminar = None
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                pelicula_a_eliminar = pelicula
                break
        if pelicula_a_eliminar:
            self.peliculas.remove(pelicula_a_eliminar)
            self.mover_a_papelera(pelicula_a_eliminar)
            print("\n==========================================")
            print(f"Película '{titulo}' eliminada del catálogo.")
            print("============================================")
        else:
            print("\n====================================================")
            print(f"No se encontró la película '{titulo}' en el catálogo.")
            print("======================================================")
    
    def mover_a_papelera(self, pelicula):
        ruta_pelicula = os.path.join(self.ruta_catalogo, f"{pelicula.titulo}.txt")
        carpeta_papelera = "Papelera de reciclaje"
        os.makedirs(carpeta_papelera, exist_ok=True)
        ruta_papelera = os.path.join(carpeta_papelera, f"{pelicula.titulo}.txt")
        shutil.move(ruta_pelicula, ruta_papelera) #Mover de ruta pelicula a ruta papelera
    
    def restaurar_desde_papelera(self, titulo):
        carpeta_papelera = "Papelera de reciclaje"
        ruta_papelera = os.path.join(carpeta_papelera, f"{titulo}.txt")
        if os.path.exists(ruta_papelera):
            shutil.move(ruta_papelera, self.ruta_catalogo)
            pelicula_recuperada = self.cargar_pelicula_desde_archivo(titulo) #Obtener informción correcta
            self.peliculas.append(pelicula_recuperada)
            print(f"\n===============================================")
            print(f"Película '{titulo}' restaurada desde la papelera.")
            print("==================================================")
        else:
            print("\n====================================================")
            print(f"No se encontró la película '{titulo}' en la papelera.")
            print("======================================================")
    
    def cargar_pelicula_desde_archivo(self, titulo): #Restaurar la pelicula con toda su información
        ruta_pelicula = os.path.join(self.ruta_catalogo, f"{titulo}.txt") #Se agrega nuevamente a la ruta catalogo
        with open(ruta_pelicula, 'r', encoding='utf-8') as archivo_pelicula: 
            titulo, director, año, genero, calificacion = archivo_pelicula.read().strip().split(',')
            return Pelicula(titulo, director, int(año), genero, float(calificacion))
    
    def listar_peliculas(self):
        if self.peliculas:
            print("\nCatálogo de películas")
            for pelicula in self.peliculas:
                print(f"{pelicula}\n")
        else:
            print("\n=====================")
            print("El Catálogo está vacío.")
            print("=======================")
            
    def buscar_pelicula(self, titulo):
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                print("\n==============================")
                print(f"Película encontrada: {pelicula}")
                print("================================")
                return pelicula
            else:
                print("\n====================================================")
                print(f"No se encontró la película '{titulo}' en el catálogo.")
                print("======================================================")
                return None
            
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
                    
                print("\n===============================")
                print(f"Película '{titulo}' actualizada.")
                print("=================================")
                
                # Actualizar el archivo de la película
                ruta_pelicula = os.path.join(self.ruta_catalogo, f"{pelicula.titulo}.txt")
                with open(ruta_pelicula, 'w', encoding='utf-8') as archivo:
                    archivo.write(f"{pelicula.titulo},{pelicula.director},{pelicula.año},{pelicula.genero},{pelicula.calificacion}\n")
                return
            
            else:
                print("\n====================================================")
                print(f"No se encontró la película '{titulo}' en el catálogo.")
                print("======================================================")
                
    def eliminar_catalogo(self):
        if os.path.exists(self.ruta_catalogo):
            for archivo in os.listdir(self.ruta_catalogo):
                os.remove(os.path.join(self.ruta_catalogo, archivo))
            os.rmdir(self.ruta_catalogo) #Eliminar tambien los archivos 
            self.peliculas = []
            CatalogoPeliculas.catalogos_creados.remove(self.nombre)
            print("\n==================================")
            print(f"Catálogo '{self.nombre}' eliminado.")
            print("====================================")
        else: 
            print("\n====================")
            print("El catálogo no existe.")
            print("======================")
            
class Funcionamientos(): 
    """
    Contiene métodos para mostrar menús y gestionar operaciones del catálogo de películas.
    """
    
    def listar_catalogos(self):
        carpeta_catalogos = "Catálogos creados"
        if os.path.exists(carpeta_catalogos):
            subcarpetas = [d for d in os.listdir(carpeta_catalogos) if os.path.isdir(os.path.join(carpeta_catalogos, d))]
            if subcarpetas:
                print(f"\n====================")
                print(f"Catálogos existentes: ")
                print(f"======================")
                for catalogo in subcarpetas:
                    print(f"{catalogo}\n")
            else: 
                print("No hay catálogos de películas creados")
        else: 
            print("No hay catálogos de películas creados")
    
    def crear_catalogo(self):
        nombre_catalogo = input("Ingrese el nombre del catálogo de películas: ")
        carpeta_catalogos = "Catálogos creados"
        ruta_catalogo = os.path.join(carpeta_catalogos, nombre_catalogo)
        if os.path.exists(ruta_catalogo):
            print("\n=========================================")
            print(f"El catálogo '{nombre_catalogo}' ya existe.")
            print("===========================================")
            return None       
        else:
            return CatalogoPeliculas(nombre_catalogo, nuevo=True)

    def seleccionar_catalogo(self):
        nombre_catalogo = input("Ingrese el nombre del catálogo de películas: ")
        carpeta_catalogos = "Catálogos creados"
        ruta_catalogo = os.path.join(carpeta_catalogos, nombre_catalogo)
        if os.path.exists(ruta_catalogo):
            return CatalogoPeliculas(nombre_catalogo, nuevo=False)
        else:
            print("\n==============================================")
            print(f"No se encontró el catálogo '{nombre_catalogo}'.")
            print("================================================")
            return None
            
    def mostrar_menu_principal(self):
        print("\nBienvenido al sistema de películas")
        print("1. Seleccionar Catálogo")
        print("2. Crear Nuevo Catálogo")
        print("3. Listar Catálogos")
        print("4. Eliminar catálogo")
        print("5. Salir")

    def mostrar_menu_catalogo(self):
        print("\nOpciones del catálogo")
        print("1. Agregar Película")
        print("2. Eliminar Película")
        print("3. Listar Películas")
        print("4. Buscar Película")
        print("5. Actualizar Película")
        print("6. Restaurar Película desde Papelera")
        print("7. Volver al Menú Principal")
        
    def main(self):
        '''
        Función principal del código.
        '''
        
        print ("=============================================================================")
        print("                  ¡Bienvenido al Cátalogo de Películas! 🎥")
        print ("=============================================================================\n")
        
        catalogo_actual = None
        
        while True:
            if catalogo_actual:
                self.mostrar_menu_catalogo()
            else:
                self.mostrar_menu_principal()
                
            opcion = input("\nIngrese una opción: ")
            if opcion.isdigit(): #Es un digito
                opcion = int(opcion)
            else:
                print("\n=================================")
                print("Opción no válida. Intente de nuevo.")
                print("===================================")
                continue #Asi no se rompe el programa
            
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
                    titulo = input("Ingrese el título de la película a buscar: ")
                    catalogo_actual.buscar_pelicula(titulo) 
                elif opcion == 5:
                    titulo = input("Ingrese el título de la película a actualizar: ")
                    catalogo_actual.actualizar_pelicula(titulo)
                elif opcion == 6:
                    titulo = input("Ingrese el título de la película a restaurar: ")
                    catalogo_actual.restaurar_desde_papelera(titulo)
                elif opcion == 7:
                        catalogo_actual.guardar_peliculas()
                        print("Guardando y volviendo al menú principal...")
                        catalogo_actual = None
                else:
                    print("\n=================================")
                    print("Opción no válida. Intente de nuevo.")
                    print("===================================")
            else:
                    if opcion == 1:
                        catalogo_actual = self.seleccionar_catalogo()
                    elif opcion == 2:
                        catalogo_actual = self.crear_catalogo()
                    elif opcion == 3:
                        self.listar_catalogos()
                    elif opcion == 4:
                        print("Esta opción también eliminará las películas almacenadas")
                        continuar = input("¿Desea continuar (Sí/No): ").strip().upper()
                        if continuar == "SI":
                            nombre_catalogo = input("Ingrese el nombre del catálogo a eliminar: ").strip()
                            if nombre_catalogo:
                                catalogo = CatalogoPeliculas(nombre_catalogo, nuevo=False)
                                catalogo.eliminar_catalogo()
                            else:
                                print("\nNo se proporcionó un nombre de catálogo válido.")
                        elif continuar == "NO":
                            print("\nNo se eliminó ningún catálogo.")
                            print("Volviendo al menú principal...")
                        else: 
                            print("\nInserte una opción válida (Sí/No).")
                    elif opcion == 5:
                        print("\n==================================================")
                        print("      Saliendo del programa. ¡Adiós!")
                        print("==================================================")
                        break 
                    else:
                        print("\n=================================")
                        print("Opción no válida. Intente de nuevo.")
                        print("===================================")

if __name__ == "__main__":
    funcionamientos = Funcionamientos()
    funcionamientos.main()
    