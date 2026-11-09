import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Caleb Dorado NC = 0039
# crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de Videojuegos con 4 elementos por lista
# Problema 3: Juegos (Nombre, copias vendidas en millones, es multijugador, año lanzamiento)
mc  = ['Minecraft', 300, True, 2011]
gta = ['GTA V', 190, True, 2013]
tet = ['Tetris', 100, False, 1984]
wii = ['Wii Sports', 82.9, True, 2006]
pub = ['PUBG', 75, True, 2017]
# Creamos una lista de listas (conformando la tabla)
lista_videojuegos_populares=[mc, gta, tet, wii, pub]
# print(lista_videojuegos_populares)
# Utilizar pandas para organizar la tabla (dataframe o marco de datos)
# A cada columna le ponemos nombre
df_videojuegos=pd.DataFrame(lista_videojuegos_populares, columns=["Nombre","Copias_vendidas","Es_MP","Año"])
print(df_videojuegos)
# Creamos el archivo CSV y lo guardamos en csv
df_videojuegos.to_csv("redessociales.csv", index=False)
# Crear graficas de lineas
# Donde X es Nombre en el eje horizontal
# Donde Y es Cantidad en el eje vertical
plt.plot(df_videojuegos["Nombre"], df_videojuegos["Copias_vendidas"])
plt.title("Grafica videojuegos populares 0039")
plt.xlabel("Nombre de los videojuegos")
plt.ylabel("Cantidad de copias vendidas en millones")
plt.show()
# Creamos una grafica de puntos
plt.scatter(df_videojuegos["Nombre"], df_videojuegos["Copias_vendidas"])
plt.show()
# Grafica de barras
plt.bar(df_videojuegos["Nombre"], df_videojuegos["Copias_vendidas"])
# Etiquetas y titulo
plt.title("Videojuegos Populares 0039")
plt.xlabel("Nombre de los videojuegos")
plt.ylabel("Cantidad de copias vendidas")
# Mostrar la grafica
plt.show()
# Ordenar la grafica de barras de manera descendente
# De la mas grande a la mas pequeña
df_vj_ordenar=df_videojuegos.sort_values("Copias_vendidas",ascending=False)
plt.bar(df_vj_ordenar["Nombre"], df_vj_ordenar["Copias_vendidas"])
plt.show()
# Coloreando la grafica
plt.bar(df_vj_ordenar["Nombre"], df_vj_ordenar["Copias_vendidas"],
        color=["b", "g", "c", "m", "y", "r"])
plt.show()

# Grafica de Pastel
# plt.plot(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.pie(df_videojuegos["Copias_vendidas"], labels=df_videojuegos["Nombre"])
plt.show()