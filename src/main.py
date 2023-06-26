from matplotlib import pyplot as plt
import sympy as sp

from algorithms import importar_datos, pares_polinomial, pares_exponencial_base_e
from algorithms import recta, curva_base_x, curva_base_e
from algorithms import calcular_coeficiente_r, relacion_mas_precisa
from graphics import graficar


CARTEL_METODO = """
 ____________________________________________________________________________
|                                                                            |
|                              REGRESION LINEAL                              |
|____________________________________________________________________________|
|                                                                            |
|  INTEGRANTES:                                                              |
|  |_ Loana Abril Schleich Garcia.                                           |
|____________________________________________________________________________|
|                                                                            |
|  Se basa en el uso de la ecuación de una línea recta para modelar la       |
|  relación entre una variable dependiente y una o más variables             |
|  independientes. Esto permite hacer predicciones basadas en la relación    |
|  lineal entre las variables.                                               |
|                                 y = ax + b                                 |
|  En caso de que la misma no fuera lineal, se puede linealizar operando     |
|  los datos para transformarlos.                                            |
|                                                                            |
|  Una relación polinomial y = bx^a se puede linealizar como:                |
|                           ln(y) = aln(x) + ln(b)                           |
|  Se trasforma cada valor de x e y aplicando el logaritmo, y como b         |
|  equivale ahora a ln(b) al hallarlo se le aplica la operación inversa.     |
|                                                                            |
|  Una relación exponencial y = be^ax se puede linealizar como:              |
|                             ln(y) = ln(b) + ax                             |
|  Se aplica la misma lógica para hallar el valor de b y transformar y.      |
|                                                                            |
|  Se reemplazan los parámetros a y b en las ecuaciones originales.          |
|____________________________________________________________________________|
|                                                                            |
|                              CUADRADOS MINIMOS                             |
|____________________________________________________________________________|
|                                                                            |
|  El método se basa en encontrar los valores óptimos para los coeficientes  |
|  de la funcion que minimicen el error cuadrático medio entre los valores   |
|  reales y los valores predichos. intenta minimizar la suma de cuadrados    |
|  de las diferencias en las ordenadas entre los puntos generados por la     |
|  función elegida y los correspondientes valores en los datos.              |
|____________________________________________________________________________|
"""

CARTEL_CONCLUSIONES = """
 ____________________________________________________________________________
|                                                                            |
|                                CONCLUSIONES                                |
|____________________________________________________________________________|
|                                                                            |
|  Habiendo calculado el coeficiente de correlación para cada curva, existe  |
|  una cuyo valor es mayor al de los demás. Esto implica que la misma        |
|  expresa con mayor precisión la relación entre los datos proporcionados    |
|  y por lo tanto sería capaz de predecir resultados más cercanos a los      |
|  valores reales.                                                           |
|____________________________________________________________________________|
"""

print(CARTEL_METODO)

x = sp.symbols('x')

puntos = importar_datos()
puntos_base_x = pares_polinomial(puntos)
puntos_base_e = pares_exponencial_base_e(puntos)

recta_puntos, recta_params = recta(x, puntos)
recta_puntos_base_x, curva_poli_params = curva_base_x(x, puntos_base_x)
recta_puntos_base_e, curva_exp_params = curva_base_e(x, puntos_base_e)

coef_recta = calcular_coeficiente_r(puntos)
coef_curva_poli = calcular_coeficiente_r(puntos_base_x)
coef_curva_exp = calcular_coeficiente_r(puntos_base_e)

print(CARTEL_CONCLUSIONES)
relacion_mas_precisa({'Lineal': coef_recta, 'Polinomial': coef_curva_poli, 'Exponencial': coef_curva_exp })

############
# GRAFICOS #
############
func_recta = sp.lambdify(x, recta_puntos, 'numpy')
func_curva_base_x = sp.lambdify(x, recta_puntos_base_x, 'numpy')
func_curva_base_e = sp.lambdify(x, recta_puntos_base_e, 'numpy')

FUNCIONES = [func_recta, func_curva_base_x, func_curva_base_e]
PUNTOS = [puntos, puntos, puntos]
COEFICIENTES_CORRELACION = [coef_recta, coef_curva_poli, coef_curva_exp]
PARAMETROS = [recta_params, curva_poli_params, curva_exp_params]
TITULOS = ["Recta", "Curva Polinomial", "Curva Exponencial"]
COLORES = ['crimson', 'cornflowerblue', 'mediumslateblue']

graficar(FUNCIONES, TITULOS, PUNTOS, COLORES, COEFICIENTES_CORRELACION, PARAMETROS)
