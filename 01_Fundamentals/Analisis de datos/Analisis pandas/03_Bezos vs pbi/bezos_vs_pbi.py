import pandas as pd
import matplotlib.pyplot as plt


#Datos en miles de millones 
datos = {
    'Nombres': ['Jeff Bezos', 'Haití', 'Paraguay', 'Bolivia', 'Argentina'],
    'Fortuna/PBI': [223.5, 19.9, 43, 45.1, 646]
}

df = pd.DataFrame(datos)

#Ordenamos de mayor a menor
df_ordenado = df.sort_values(by='Fortuna/PBI', ascending=False)
print(df_ordenado)

plt.figure(figsize=(10,6))
plt.bar(df_ordenado['Nombres'], df_ordenado['Fortuna/PBI'], color='skyblue')
plt.title('Fortuna de Jeff Bezos vs PBI de países seleccionados')
plt.xticks(rotation=45)
plt.ylabel('USD (miles de millones)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('grafico_1.png')
plt.show()

#CUantas veces supera

fortuna_bezos = df.loc[df['Nombres'] == 'Jeff Bezos', 'Fortuna/PBI'].values[0]
df['Veces que Bezos supera'] = fortuna_bezos / df['Fortuna/PBI']


# -------------------------------
# 4. Segundo gráfico: comparación relativa
# -------------------------------
df_sin_bezos = df[df['Nombres'] != 'Jeff Bezos']

plt.figure(figsize=(10,6))
plt.bar(df_sin_bezos['Nombres'], df_sin_bezos['Veces que Bezos supera'], color='salmon')
plt.title('¿Cuántas veces la fortuna de Jeff Bezos supera el PBI de estos países?')
plt.ylabel('Veces que la supera')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('grafico_2.png')
plt.show()