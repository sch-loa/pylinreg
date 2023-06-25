import pandas as pd
import numpy as np
import sympy as sp

###########################
def regresion_lineal(puntos):
    x = sp.symbols('x')
    a, b = hallar_a_y_b(puntos)
    return a*x + b

############################
def hallar_a_y_b(puntos):
    a = sp.symbols('a')
    b = sp.symbols('b')

    return (a, b)

# Suma todos los elementos en un array de una dimensión
def sumatoria(vector_puntos):
    return np.sum(vector_puntos)

###################################
def multiplicatoria(puntos):
    return puntos[:, 0] * puntos[:, 1]

##################################
def pares_exponencial_base_x(puntos):
    return np.log(puntos)

#################################
def pares_exponencial_base_e(puntos):
    arr = puntos
    arr[:, 1] = np.log(arr[:, 1])
    return arr

# Retorna datos del archivo Excel en forma de DataFrame
def importar_datos():
    return pd.read_excel('./datos/ACUMULADOS vs DIAS.xlsx', sheet_name = 'Hoja1', usecols = ['día', 'acumulados'], skiprows = 4)[1:]