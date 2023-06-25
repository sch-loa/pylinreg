import pandas as pd
import numpy as np
import sympy as sp
import math

# Función principal del metodo de regresión por cuadrados mínimos, devuelve todas las funciones calculadas
def regresion_lineal(puntos):
    x = sp.symbols('x')
    
    return (recta(x, puntos), curva_base_x(x, puntos), curva_base_e(x, puntos))

# Retorna la recta más cercana a todos los puntos
def recta(x, puntos):
    a, b = hallar_a_y_b(puntos)
    return a*x + b

# Retorna la función curva polinomial más cercana a todos los puntos
def curva_base_x(x, puntos):
    puntos_base_x = pares_polinomial(puntos)
    a, b = hallar_a_y_b(puntos_base_x)
    return b*x**a

# Retorna la función curva exponencial de base e más cercana a todos los puntos
def curva_base_e(x, puntos):
    puntos_base_e = pares_exponencial_base_e(puntos)
    a, b = hallar_a_y_b(puntos_base_e)
    return b*math.e**(a*x)

# Calcula y retorna los valores de a y b resolviendo un sistema matricial
def hallar_a_y_b(puntos):
    a = sp.symbols('a')
    b = sp.symbols('b')

    x = puntos[:,0]
    y = puntos[:,1]
    n = puntos.shape[0]

    x_sum = sumatoria(x)
    y_sum = sumatoria(y)

    matriz_incognita = np.array([[(sumatoria(x**2)),(x_sum)],[x_sum, n]])
    matriz_resultado = np.array([sumatoria(multiplicatoria(puntos)), y_sum])

    return np.linalg.solve(matriz_incognita, matriz_resultado)

# Suma todos los elementos en un array de una dimensión
def sumatoria(vector_puntos):
    return np.sum(vector_puntos)

# Multiplica las columnas de una matriz de 2x2
def multiplicatoria(puntos):
    return puntos[:, 0] * puntos[:, 1]

# Retorna los puntos linealizados para una función polinomial
def pares_polinomial(puntos):
    return np.log(puntos)

# Retorna los puntos linealizados para una función exponencial de base e
def pares_exponencial_base_e(puntos):
    arr = puntos
    arr[:, 1] = np.log(arr[:, 1])
    return arr

# Retorna datos del archivo Excel en forma de DataFrame
def importar_datos():
    return pd.read_excel('./datos/ACUMULADOS vs DIAS.xlsx', sheet_name = 'Hoja1', usecols = ['día', 'acumulados'], skiprows = 4)[1:]