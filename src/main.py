from matplotlib import pyplot as plt

from algorithms import regresion_lineal, importar_datos

puntos = importar_datos().values

recta_puntos, recta_puntos_base_x, recta_puntos_base_e= regresion_lineal(puntos)

