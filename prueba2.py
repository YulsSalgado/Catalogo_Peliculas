import requests

def obtener_informacion_pelicula(titulo, api_key):
    url = f"http://www.omdbapi.com/?t={titulo}&apikey={api_key}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos['Response'] == 'True':
            return datos
        else:
            return f"Error: {datos['Error']}"
    else:
        return f"Error: No se pudo obtener la información, código de estado {respuesta.status_code}"

def main():
    api_key = 'tu_clave_de_api_aqui'
    while True:
        titulo_pelicula = input("Ingresa el título de la película (o 'salir' para terminar): ")
        if titulo_pelicula.lower() == 'salir':
            break
        info_pelicula = obtener_informacion_pelicula(titulo_pelicula, api_key)
        print(info_pelicula)

if __name__ == "__main__":
    main()

