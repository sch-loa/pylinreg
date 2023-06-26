import numpy as np
import sympy as sp
from matplotlib import pyplot as plt

def graficar(FUNCIONES, TITULOS, PUNTOS, COLORES, COEFICIENTES_CORRELACION, PARAMETROS):
    x_vals = PUNTOS[:,0]
    y_vals = PUNTOS[:,1]
    for i in range(len(FUNCIONES)):

        fig, ax = plt.subplots()

        plt.xlim(min(x_vals), max(x_vals))
        plt.ylim(min(y_vals), max(y_vals))

        with np.errstate(invalid='ignore'):
            ax.plot(x_vals, FUNCIONES[i](x_vals), color = 'k')
        ax.scatter(x_vals, y_vals, color = COLORES[i])

        plt.text(5, 285000, s= 'a: '+str(round(PARAMETROS[i][0], 2)), size=8, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5), fc=(1.0, 0.9, 0.8),)).set_bbox({"facecolor":"crimson", "edgecolor":"crimson"})
        plt.text(5, 264000, s= 'b: '+str(round(PARAMETROS[i][1], 2)), size=8, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5), fc=(1.0, 0.9, 0.8),)).set_bbox({"facecolor":"cornflowerblue", "edgecolor":"cornflowerblue"})
        plt.text(5, 239000, s= 'r: '+str(round(COEFICIENTES_CORRELACION[i], 2)), size=8, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5), fc=(1.0, 0.9, 0.8),)).set_bbox({"facecolor":"mediumslateblue", "edgecolor":"mediumslateblue"})
        plt.grid(True, linestyle='--', linewidth=0.3, color='gray') 
        plt.title(f'Regresión Lineal: {TITULOS[i]}')

    plt.show()

def graficar_derivadas(FUNCIONES, TITULOS, PUNTOS):
    x_vals = PUNTOS[:,0]
    y_vals = PUNTOS[:,1]
    for i in range(len(FUNCIONES)):
        fig, ax = plt.subplots()

        plt.xlim(min(x_vals), max(x_vals))
        plt.ylim(min(x_vals), max(x_vals))

        with np.errstate(invalid='ignore'):
            ax.plot(x_vals, FUNCIONES[i](x_vals), color = 'k')

        plt.grid(True, linestyle='--', linewidth=0.3, color='gray') 
        plt.title(f'Derivada {TITULOS[i]} de la curva más precisa')

    plt.show()
