import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
# Crear una matriz de 3x3 con valores iniciales
matrix_data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix = ax.imshow(matrix_data, cmap='viridis')

def update(frame):

    while exit != True:

        if frame == 2:  
            matrix.set_cmap('twilight')
        return matrix,

ani = FuncAnimation(fig, update, frames=range(128), blit=True)

plt.show()
