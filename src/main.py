from matplotlib import pyplot as plt
import sympy as sp

from algorithms import regresion_lineal, importar_datos
from graphics import graficar

puntos = importar_datos()

recta_puntos, recta_puntos_base_x, recta_puntos_base_e = regresion_lineal(puntos)

############
# GRAFICOS #
############
x = sp.symbols('x')
func_recta = sp.lambdify(x, recta_puntos, 'numpy')
func_curva_base_x = sp.lambdify(x, recta_puntos_base_x, 'numpy')
func_curva_base_e = sp.lambdify(x, recta_puntos_base_e, 'numpy')

FUNCIONES = [func_recta, func_curva_base_x, func_curva_base_e]
TITULOS = ["Recta", "Curva Polinomial", "Curva Exponencial"]
COLORES = ['r', 'c', 'y']

graficar(FUNCIONES, TITULOS, puntos, COLORES)
