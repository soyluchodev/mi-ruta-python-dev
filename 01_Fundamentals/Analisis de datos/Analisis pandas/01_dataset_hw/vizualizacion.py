#importamos herramientas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#leemos el archivo

df = pd.read_csv("hw_200.csv")
# Limpiar nombres de columnas: quitar espacios
df.columns = df.columns.str.strip()
print(df.columns)

# Calculamos la correlación entre Height y Weight
corr = df['Height(Inches)"'].corr(df['"Weight(Pounds)"'])
print(f"Correlación entre altura y peso: {corr:.2f}")


#damos un estilo a los graficos

sns.set(style="whitegrid")


#Graficar un histrograma de alturas

plt.figure(figsize=(8, 5)) #tamaño de la imagen
sns.histplot(data=df, x='Height(Inches)"', bins=10, kde=True, color="skyblue")
plt.title("Distribucion de la altura")
plt.xlabel("Altura (pulgadas)")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig("histograma_altura.png", dpi=300, bbox_inches='tight')  # <-- guarda imagen
plt.show()
plt.show()


#Graficar un histrograma de pesos

plt.figure(figsize=(8, 5)) #tamaño de la imagen
sns.histplot(data=df, x='"Weight(Pounds)"', bins=10, kde=True, color="skyblue")
plt.title("Distribucion del peso")
plt.xlabel("Peso (libras)")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig("histograma_peso.png", dpi=300, bbox_inches='tight')
plt.show()


#graficar la relación entre altura y peso

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Height(Inches)"', y='"Weight(Pounds)"', data=df, color="purple")
plt.title("Relación entre altura y peso")
plt.xlabel("Altura (pulgadas)")
plt.ylabel("Peso (libras)")
plt.tight_layout()
plt.savefig("dispersion_altura_peso.png", dpi=300, bbox_inches='tight')
plt.show()
