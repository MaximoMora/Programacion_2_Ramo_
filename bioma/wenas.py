import tkinter as tk

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(tk.Entry(root, width=5))
            fila[j].grid(row=i, column=j)
        matriz.append(fila)
    return matriz

root = tk.Tk()
root.title("Matriz con Tkinter")

# Definir el tamaño de la matriz (por ejemplo, 3x3)
num_filas = 3
num_columnas = 3

mi_matriz = crear_matriz(num_filas, num_columnas)

root.mainloop()
