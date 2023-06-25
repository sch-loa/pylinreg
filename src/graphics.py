import numpy as np
from matplotlib import pyplot as plt

def graficar(FUNCIONES, TITULOS, PUNTOS, COLORES):
    x_vals = PUNTOS[:,0]
    y_vals = PUNTOS[:,1]
  
    x_randvals = np.linspace(min(x_vals)-100, max(x_vals)+100, 400)


    for i in range(len(FUNCIONES)):
        fig, ax = plt.subplots()

        plt.xlim(min(x_vals), max(x_vals))
        plt.ylim(min(y_vals), max(y_vals))

        with np.errstate(invalid='ignore'):
            ax.plot(x_randvals, FUNCIONES[i](x_randvals), color = 'k')
        ax.scatter(x_vals, y_vals, color = COLORES[i])

        plt.grid(True, linestyle='--', linewidth=0.3, color='gray') 
        plt.title(f'Regresión Lineal: {TITULOS[i]}')

        plt.show()

