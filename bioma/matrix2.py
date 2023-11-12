import tkinter as tk
import random
import time

def cambiar_colores():
    for i in range(num_filas):
        for j in range(num_columnas):
            color_actual = mi_matriz[i][j].cget('bg')  # Obtener el color actual
            nuevo_color = generar_color_suave(color_actual)  # Generar un color suave
            mi_matriz[i][j].config(bg=nuevo_color)

    root.after(2000, cambiar_colores)  # Llamar a la función cada 2000 milisegundos (2 segundos)

def generar_color_suave(color):
    # Descomponer el color en componentes RGB
    r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)

    # Aumentar el valor de cada componente RGB
    r += 100
    g += 100
    b += 100

    # Formatear el nuevo color en formato hexadecimal
    nuevo_color = "#{}{}{}".format(r, g, b)

    return nuevo_color

root = tk.Tk()
root.title("Cambio de Colores")

# Definir el tamaño de la matriz (por ejemplo, 3x3)
num_filas = 25
num_columnas = 25

mi_matriz = []
for i in range(num_filas):
    fila = []
    for j in range(num_columnas):
        cuadro = tk.Label(root, width=5, height=2, relief="solid", borderwidth=1)
        cuadro.grid(row=i, column=j)
        fila.append(cuadro)
    mi_matriz.append(fila)

cambiar_colores()  # Iniciar el cambio de colores

root.mainloop()
