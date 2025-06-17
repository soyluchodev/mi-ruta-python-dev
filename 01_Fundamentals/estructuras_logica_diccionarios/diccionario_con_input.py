#Creamos un diccionario vacio

persona = {}

#Pedimos datos al usuario

nombre = input("¿Cual es tu nombre?: ")
edad = input("¿Cual es tu edad?: ")
ciudad = input("¿Cual es tu ciudad?: ")

# Usamos update() para agregar todos los datos de una vez

persona.update({
    'nombre' : nombre,
    'edad' : edad,
    'ciudad' : ciudad
}
)
#Imprimimos el diccionario completo, con capitalize() para mostrar claves con mayus.

print('\nDatos diccionario:')
for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")