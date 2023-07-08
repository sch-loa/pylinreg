from matplotlib import pyplot as plt
import sympy as sp
import numpy as np

from algorithms import importar_datos, pares_polinomial, pares_exponencial_base_e
from algorithms import recta, curva_base_x, curva_base_e
from algorithms import calcular_coeficiente_r, relacion_mas_precisa
from algorithms import calcular_derivada_num_1ra, calcular_derivada_num_2da, calcular_tiempo_duplicacion
from graphics import graficar, graficar_derivadas


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
|  reales y los valores predichos. Intenta minimizar la suma de cuadrados    |
|  de las diferencias en las ordenadas entre los puntos generados por la     |
|  función elegida y los correspondientes valores en los datos.              |
|____________________________________________________________________________|
"""

CARTEL_DERIVADA_PRIMERA = """
 ____________________________________________________________________________
|                                                                            |
|                              DERIVADA PRIMERA                              |
|____________________________________________________________________________|
|                                                                            |
|  La derivada primera de una función representa la tasa de cambio de la     |
|  variable dependiente por cada cambio unitario en la variable              |
|  independiente. Brinda información sobre la pendiente y la dirección de    |
|  la relación entre las variables involucradas en el modelo lineal.         |
|____________________________________________________________________________|
"""

CARTEL_DERIVADA_SEGUNDA = """
 ____________________________________________________________________________
|                                                                            |
|                              DERIVADA SEGUNDA                              |
|____________________________________________________________________________|
|                                                                            |
|  La derivada segunda de una función en un contexto de regresión no lineal  |
|  proporciona información sobre la concavidad de la curva. Además, la       |
|  magnitud de la derivada puede indicar la tasa de cambio de la pendiente   |
|  en diferentes puntos de la misma.                                         |
|____________________________________________________________________________|
"""

CARTEL_CONCLUSIONES = """
 ____________________________________________________________________________
|                                                                            |
|                                CONCLUSIONES                                |
|____________________________________________________________________________|
|                                                                            |
|  Habiendo calculado el coeficiente de correlación para cada curva, existe  |
|  una cuyo valor es mayor al de los demás (acotado entre 0 y 1). Esto       |
|  implica que la misma expresa con mayor precisión la relación entre los    |
|  datos proporcionados y por lo tanto sería capaz de predecir resultados    |
|  más cercanos a los valores reales.                                        |
|____________________________________________________________________________|
"""

##########################
# CALCULOS E IMPRESIONES #
##########################

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

func_mas_precisa = relacion_mas_precisa({'Lineal': (recta_puntos, coef_recta), 'Polinomial': (recta_puntos_base_x, coef_curva_poli), 'Exponencial': (recta_puntos_base_e, coef_curva_exp) })

puntos_derivada_num_1ra = np.array([calcular_derivada_num_1ra(func_mas_precisa, i) for i in puntos[:,0]])
puntos_derivada_num_2da = np.array([calcular_derivada_num_2da(func_mas_precisa, j) for j in puntos[:,0]])

f_prima = sp.diff(func_mas_precisa, x)

func_prima = sp.lambdify(x, f_prima, 'numpy')
grow_rate = ((puntos[1][-1] - puntos[1][0])) / (puntos[1][0] * 100)
print(f'   Tiempo de duplicación respecto al último día: {round(calcular_tiempo_duplicacion(grow_rate), 2)} días')

print(CARTEL_CONCLUSIONES)

############
# GRAFICOS #
############

# CURVAS DE REGRESION
func_recta = sp.lambdify(x, recta_puntos, 'numpy')
func_curva_base_x = sp.lambdify(x, recta_puntos_base_x, 'numpy')
func_curva_base_e = sp.lambdify(x, recta_puntos_base_e, 'numpy')

FUNCIONES = [func_recta, func_curva_base_x, func_curva_base_e]
COEFICIENTES_CORRELACION = [coef_recta, coef_curva_poli, coef_curva_exp]
PARAMETROS = [recta_params, curva_poli_params, curva_exp_params]
TITULOS = ["Recta", "Curva Polinomial", "Curva Exponencial"]
COLORES = ['crimson', 'cornflowerblue', 'mediumslateblue']

graficar(FUNCIONES, TITULOS, puntos, COLORES, COEFICIENTES_CORRELACION, PARAMETROS)

# DERIVADAS DE LA CURVA DE MAYOR APROXIMACION
DERIVADAS = [sp.lambdify(x, f_prima, 'numpy'), sp.lambdify(x, sp.diff(f_prima,x), 'numpy')] 
TITULOS_DERIVADAS = ['Primera', 'Segunda']

graficar_derivadas(DERIVADAS, TITULOS_DERIVADAS, puntos)
