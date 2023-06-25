import numpy as np
from matplotlib import pyplot as plt

def graficar(FUNCIONES, TITULOS, PUNTOS,):
    x_vals = PUNTOS[:,0]
    y_vals = PUNTOS[:,1]

    x_randvals = np.linspace(min(x_vals)-1, max(x_vals)+1, 300)

    max_val = np.max(PUNTOS.flatten())

    for i in range(len(FUNCIONES)):
        fig, ax = plt.subplots()

        plt.xlim(min(x_vals)-1, max(x_vals)+1)
        plt.ylim(min(y_vals)-1, max(y_vals)+1)

        ax.plot(x_randvals, FUNCIONES[i](x_randvals), 'k')
        ax.scatter(x_vals, y_vals, color = 'k')

        plt.grid(True, linestyle='--', linewidth=0.3, color='gray') 
        plt.title(f'Regresión Lineal')

        plt.show()

