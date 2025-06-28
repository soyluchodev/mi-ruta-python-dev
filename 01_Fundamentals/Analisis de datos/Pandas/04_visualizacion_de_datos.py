import pandas as pd
import matplotlib.pyplot as plt

#Crear una serie de ejemplo

ts = pd.Series([1, 3, 5, 7, 9])


#Graficar la Serie

ts.plot()
plt.show()


#Crear un DataFrame de ejemplo

df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1]
})

#graficar el DataFrame

df.plot(kind='bar')
plt.show()

#Personalizar Graficos
ax = df.plot()
ax.set_xlabel("Índice")
ax.set_ylabel("Valores")
plt.show()


# fig = df.plot()
# fig.get_figure().savefig('grafico.png')
