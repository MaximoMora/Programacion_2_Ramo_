import tkinter as tk
import random
import time

def cambiar_colores():
    for i in range(num_filas):
        for j in range(num_columnas):
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # Generar un color hexadecimal aleatorio
            mi_matriz[i][j].config(bg=color)

    root.after(2000, cambiar_colores)  # Llamar a la función cada 2000 milisegundos (2 segundos)

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
