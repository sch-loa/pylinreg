import pandas as pd
import numpy as np
import sympy as sp
import math

# Retorna la recta más cercana a todos los puntos
def recta(x, puntos):
    a, b = hallar_a_y_b(puntos)
    return (a*x + b, (a,b))

# Retorna la función curva polinomial más cercana a todos los puntos
def curva_base_x(x, puntos):
    a, b = hallar_a_y_b(puntos)
    return (math.exp(b)*x**a, (a,b))

# Retorna la función curva exponencial de base e más cercana a todos los puntos
def curva_base_e(x, puntos):
    a, b = hallar_a_y_b(puntos)
    return (math.exp(b)*math.e**(a*x), (a, b))

# Calcula y retorna los valores de a y b de acuerdo a la fórmula que se conoce
def hallar_a_y_b(puntos):
    x = puntos[:,0]
    y = puntos[:,1]
    n = puntos.shape[0]

    x_sum = sumatoria(x)
    x_p2_sum = sumatoria(np.copy(x) ** 2)
    x_sum_p2 = x_sum**2
    y_sum = sumatoria(y)
    xy_sum = sumatoria(multiplicatoria(puntos))

    a = (n*xy_sum - x_sum*y_sum) / (n*x_p2_sum - x_sum_p2)
    b = (x_p2_sum*y_sum - x_sum*xy_sum) / (n*x_p2_sum - x_sum_p2)

    return (a, b)

# Calcula el coeficiente de correlacion
def calcular_coeficiente_r(puntos):
    x = puntos[:,0]
    y = puntos[:,1]
    n = puntos.shape[0]

    x_sum = sumatoria(x)
    x_p2_sum = sumatoria(np.copy(x) ** 2)
    x_sum_p2 = x_sum**2
    y_sum = sumatoria(y)
    y_p2_sum = sumatoria(np.copy(y) ** 2)
    y_sum_p2 = y_sum**2
    xy_sum = sumatoria(multiplicatoria(puntos))

    r = (n*xy_sum - x_sum*y_sum) / (math.sqrt(n*x_p2_sum - x_sum_p2) * math.sqrt(n*y_p2_sum - y_sum_p2))

    return r

# Suma todos los elementos en un array de una dimensión
def sumatoria(vector_puntos):
    return np.sum(np.copy(vector_puntos))

# Multiplica las columnas de una matriz de 2x2
def multiplicatoria(puntos):
    return puntos[:, 0] * puntos[:, 1]

# Retorna los puntos linealizados para una función polinomial
def pares_polinomial(puntos):
    return np.log(np.copy(puntos))

# Retorna los puntos linealizados para una función exponencial de base e
def pares_exponencial_base_e(puntos):
    arr = np.copy(puntos)
    arr[:, 1] = np.log(arr[:, 1])
    return arr

# Evalua la funcion en x y devuelve el resultado
def fx(func, x_n):
    x = sp.symbols('x')
    return func.subs(x, x_n).evalf()

# Calcula tiempo de duplicacion
def calcular_tiempo_duplicacion(grow_rate):
    return abs(np.log(2) / grow_rate)

# Calcula la derivada primera numérica aproximada de un punto dado en una funcion
def calcular_derivada_num_1ra(func, x_n, h = 10**-5):
    return (fx(func, x_n + h) - fx(func, x_n)) / h 

# Calcula la derivada segunda numérica aproximada de un punto dado en una funcion
def calcular_derivada_num_2da(func, x_n, h = 10**-5):
    return (fx(func, x_n - h) - 2*fx(func, x_n) + fx(func, x_n + h)) / h**2

# Retorna datos del archivo Excel en forma de DataFrame
def importar_datos():
    return pd.read_excel('./datos/ACUMULADOS vs DIAS.xlsx', sheet_name = 'Hoja1', usecols = ['día', 'acumulados'], skiprows = 4)[1:].values

# Imprime la relacion más precisa y su coeficiente de relacion r
def relacion_mas_precisa(relaciones_coeffs):
    func_mayor = 0
    mayor_valor = max([i[1] for i in relaciones_coeffs.values()])

    for clave, valor in relaciones_coeffs.items():
        if(valor[1] == mayor_valor):
            print(f'   Relación con el mayor grado de correlación: {clave},\n   Coeficiente de correlación: {round(valor[1], 2)}')
            func_mayor = valor[0]
    return func_mayor