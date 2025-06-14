from datetime import datetime


def escribir(entrada):
    with open('notas.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{datetime.now().strftime("%d/%m/%y")}: -- {entrada}\n')
        print("Nota agregada a 'notas.txt' 📒")

print("\n📚Este es tu gestor de notas📒🥸")
entrada = input('Introduce tu nota: ')
escribir(entrada)

