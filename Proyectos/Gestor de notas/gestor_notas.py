from datetime import datetime

archivo = 'notas.txt'

def escribir(entrada):
    with open('notas.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{datetime.now().strftime("%d/%m/%y")}: -- {entrada}\n')
        print("Nota agregada a 'notas.txt' 📒")


def ver_notas():
    with open('notas.txt', encoding='UTF-8') as f:
        print(f.read())


# def imprimir ultimas 10 notas

def buscar_por_fechas():
    pass #implementar buscador por fechas




print("\n📚Este es tu gestor de notas📒🥸")
entrada = input('Introduce tu nota: ')
escribir(entrada)
ver_notas()
