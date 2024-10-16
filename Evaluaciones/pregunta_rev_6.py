import numpy as np
import scipy.stats as stats

# Datos del problema
mu = 168.43  # Media
sigma = 3.45  # Desviación estándar
n = 32  # Tamaño de la muestra
X = 165  # Valor de interés

# Calcular la desviación estándar de la media muestral
sigma_x_bar = sigma / np.sqrt(n)

# Calcular el valor Z
Z = (X - mu) / sigma_x_bar

# Calcular la probabilidad de que la medida sea menor que 165 cm
probabilidad_menor = stats.norm.cdf(Z)

# Calcular la probabilidad de que sea 165 cm o más
probabilidad_mayor = 1 - probabilidad_menor

# Convertir a porcentaje y redondear a dos decimales
probabilidad_porcentaje = probabilidad_mayor * 100
probabilidad_porcentaje_redondeada = round(probabilidad_porcentaje, 2)

print(probabilidad_porcentaje_redondeada)

