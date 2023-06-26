import numpy as np
from matplotlib import pyplot as plt

def graficar(FUNCIONES, TITULOS, PUNTOS, COLORES, COEFICIENTES_CORRELACION, PARAMETROS):
    for i in range(len(FUNCIONES)):
        x_vals = PUNTOS[i][:,0]
        y_vals = PUNTOS[i][:,1]
  
        x_randvals = np.linspace(min(x_vals)-100, max(x_vals)+100, 400)

        fig, ax = plt.subplots()

        plt.xlim(min(x_vals), max(x_vals))
        plt.ylim(min(y_vals), max(y_vals))

        with np.errstate(invalid='ignore'):
            ax.plot(x_randvals, FUNCIONES[i](x_randvals), color = 'k')
        ax.scatter(x_vals, y_vals, color = COLORES[i])

        plt.text(5, 285000, s= 'a: '+str(round(PARAMETROS[i][0], 2)), size=8, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5), fc=(1.0, 0.9, 0.8),)).set_bbox({"facecolor":"crimson", "edgecolor":"crimson"})
        plt.text(5, 264000, s= 'b: '+str(round(PARAMETROS[i][1], 2)), size=8, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5), fc=(1.0, 0.9, 0.8),)).set_bbox({"facecolor":"cornflowerblue", "edgecolor":"cornflowerblue"})
        plt.text(5, 239000, s= 'r: '+str(round(COEFICIENTES_CORRELACION[i], 2)), size=8, ha="left", va="bottom", bbox=dict(boxstyle="square", ec=(1.0, 0.7, 0.5), fc=(1.0, 0.9, 0.8),)).set_bbox({"facecolor":"mediumslateblue", "edgecolor":"mediumslateblue"})
        plt.grid(True, linestyle='--', linewidth=0.3, color='gray') 
        plt.title(f'Regresión Lineal: {TITULOS[i]}')

        plt.show()

