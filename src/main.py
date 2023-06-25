from matplotlib import pyplot as plt
import numpy as np
import sympy as sp

from algorithms import regresion_lineal, importar_datos
from graphics import graficar

puntos = importar_datos().values

recta_puntos, recta_puntos_base_x, recta_puntos_base_e = regresion_lineal(puntos)

############
x = sp.symbols('x')
func_recta = sp.lambdify(x, recta_puntos, 'numpy')
func_curva_base_x = sp.lambdify(x, recta_puntos_base_x, 'numpy')
func_curva_base_e = sp.lambdify(x, recta_puntos_base_e, 'numpy')

graficar([func_recta, func_curva_base_x, func_curva_base_e], ["a", "b", "c"], puntos)
