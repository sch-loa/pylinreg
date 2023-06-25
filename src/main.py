from matplotlib import pyplot as plt
import sympy as sp

from algorithms import importar_datos, calcular_coeficiente_r, pares_polinomial, pares_exponencial_base_e
from algorithms import recta, curva_base_x, curva_base_e
from graphics import graficar


CARTEL_METODO = """
 ____________________________________________________________________________
|                                                                            |
|                     REGRESIÓN LINEAL: CUADRADOS MINIMOS                    |
|____________________________________________________________________________|
|                                                                            |
|  INTEGRANTES:                                                              |
|  |_ Loana Abril Schleich Garcia.                                           |
|____________________________________________________________________________|
|                                                                            |
|                                                                            |
|____________________________________________________________________________|
"""

CARTEL_CUADRADOS_MINIMOS = """
 ____________________________________________________________________________
|                                                                            |
|                              CUADRADOS MINIMOS                             |
|____________________________________________________________________________|
|                                                                            |
|____________________________________________________________________________|
"""

CARTEL_CONCLUSIONES = """
 ____________________________________________________________________________
|                                                                            |
|                                CONCLUSIONES                                |
|____________________________________________________________________________|
|                                                                            |
|____________________________________________________________________________|
"""

print(CARTEL_METODO)

x = sp.symbols('x')

puntos = importar_datos()
puntos_base_x = pares_polinomial(puntos)
puntos_base_e = pares_exponencial_base_e(puntos)

print(calcular_coeficiente_r(puntos))
print(calcular_coeficiente_r(puntos_base_x))
print(calcular_coeficiente_r(puntos_base_e))

recta_puntos = recta(x, puntos)
recta_puntos_base_x = curva_base_x(x, puntos_base_x)
recta_puntos_base_e = curva_base_e(x, puntos_base_e)

#print(recta_puntos)
#print(recta_puntos_base_x)
#print(recta_puntos_base_e)

############
# GRAFICOS #
############
func_recta = sp.lambdify(x, recta_puntos, 'numpy')
func_curva_base_x = sp.lambdify(x, recta_puntos_base_x, 'numpy')
func_curva_base_e = sp.lambdify(x, recta_puntos_base_e, 'numpy')

FUNCIONES = [func_recta, func_curva_base_x, func_curva_base_e]
PUNTOS = [puntos, puntos, puntos]
TITULOS = ["Recta", "Curva Polinomial", "Curva Exponencial"]
COLORES = ['r', 'c', 'y']


graficar(FUNCIONES, TITULOS, PUNTOS, COLORES)
