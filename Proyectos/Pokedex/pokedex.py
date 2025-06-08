#importamos biblioteca/ y modulo para abrir paginas web
import requests
import webbrowser
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Pedir entrada al ususario(nombre del pokemon)
nombre_o_id = input("Introduce el nombre de un Pokemon: ")

#Pedimos info a la API con el nombre que se introduce y los pasamos todo
#a minuscula para que no haya problemas

response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nombre_o_id.lower()}')
#paso 3: se verifica que la respuesta fue exitosa, y guardamos la respuesta en una variable (data)
if response.status_code == 200: 
    data = response.json()

    print(f"Nombre: {data['name']}")
    print(f"ID: {data['id']}")
    url_imagen = data['sprites']['other']['official-artwork']['front_default']
    
#Preguntar si abrimos imagen
    abrir = input("¿Quieres abrir la imagen en el navegador? (s/n): " )
    if abrir == 's':
        webbrowser.open(url_imagen)
else:
    print('Pokemon no encontrado! Revisa el nombre o ID')