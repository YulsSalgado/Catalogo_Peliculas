import tkinter as tk
from tkinter import messagebox
import os

class Pelicula:
    def __init__(self, titulo, director, año, genero):
        self.titulo = titulo
        self.director = director
        self.año = año
        self.genero = genero

    def __str__(self):
        return f"Título: {self.titulo}, Director: {self.director}, Año: {self.año}, Género: {self.genero}"

    def to_file_string(self):
        return f"{self.titulo}|{self.director}|{self.año}|{self.genero}"

    @classmethod
    def from_file_string(cls, file_string):
        titulo, director, año, genero = file_string.strip().split('|')
        return cls(titulo, director, int(año), genero)

class CatalogoApp:
    def __init__(self, root):
        self.catalogo = []
        self.catalogo_file = 'catalogo.txt'
        self.root = root
        self.root.title("Catálogo de Películas")

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.label = tk.Label(self.frame, text="Catálogo de Películas", font=("Helvetica", 16))
        self.label.pack()

        self.add_button = tk.Button(self.frame, text="Agregar Película", command=self.agregar_pelicula)
        self.add_button.pack(fill='x')

        self.list_button = tk.Button(self.frame, text="Mostrar Películas", command=self.mostrar_peliculas)
        self.list_button.pack(fill='x')

        self.cargar_catalogo()

    def agregar_pelicula(self):
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Agregar Película")

        tk.Label(self.add_window, text="Título:").grid(row=0, column=0)
        self.titulo_entry = tk.Entry(self.add_window)
        self.titulo_entry.grid(row=0, column=1)

        tk.Label(self.add_window, text="Director:").grid(row=1, column=0)
        self.director_entry = tk.Entry(self.add_window)
        self.director_entry.grid(row=1, column=1)

        tk.Label(self.add_window, text="Año:").grid(row=2, column=0)
        self.año_entry = tk.Entry(self.add_window)
        self.año_entry.grid(row=2, column=1)

        tk.Label(self.add_window, text="Género:").grid(row=3, column=0)
        self.genero_entry = tk.Entry(self.add_window)
        self.genero_entry.grid(row=3, column=1)

        tk.Button(self.add_window, text="Agregar", command=self.guardar_pelicula).grid(row=4, columnspan=2)

    def guardar_pelicula(self):
        titulo = self.titulo_entry.get()
        director = self.director_entry.get()
        año = self.año_entry.get()
        genero = self.genero_entry.get()

        if titulo and director and año and genero:
            try:
                año = int(año)
                pelicula = Pelicula(titulo, director, año, genero)
                self.catalogo.append(pelicula)
                self.guardar_catalogo()
                messagebox.showinfo("Éxito", f"Película '{titulo}' agregada al catálogo.")
                self.add_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "El año debe ser un número entero.")
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")

    def mostrar_peliculas(self):
        self.list_window = tk.Toplevel(self.root)
        self.list_window.title("Catálogo de Películas")

        if not self.catalogo:
            tk.Label(self.list_window, text="El catálogo está vacío.").pack()
        else:
            for pelicula in self.catalogo:
                tk.Label(self.list_window, text=str(pelicula)).pack()

    def guardar_catalogo(self):
        with open(self.catalogo_file, 'w') as f:
            for pelicula in self.catalogo:
                f.write(pelicula.to_file_string() + '\n')

    def cargar_catalogo(self):
        if os.path.exists(self.catalogo_file):
            with open(self.catalogo_file, 'r') as f:
                for line in f:
                    self.catalogo.append(Pelicula.from_file_string(line))

if __name__ == "__main__":
    root = tk.Tk()
    app = CatalogoApp(root)
    root.mainloop()
