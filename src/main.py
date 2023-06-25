from algorithms import regresion_lineal, importar_datos
from algorithms import pares_exponencial_base_x, pares_exponencial_base_e

puntos = importar_datos().values
puntos_base_x = pares_exponencial_base_x(puntos)
puntos_base_e = pares_exponencial_base_e(puntos)

regresion_lineal(puntos)