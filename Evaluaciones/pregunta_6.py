import numpy as np
import scipy.stats as stats

# Datos del problema
mu = 653620  # Media de la población
sigma = 16000  # Desviación estándar de la población
n = 350  # Tamaño de la muestra
X = 670000  # Depósito medio de interés

# Calcular la desviación estándar de la media muestral
sigma_x_bar = sigma / np.sqrt(n)

# Calcular el valor Z
Z = (X - mu) / sigma_x_bar

# Calcular la probabilidad de que la media muestral sea mayor que X
probabilidad = 1 - stats.norm.cdf(Z)

# Convertir a porcentaje y redondear a dos decimales
probabilidad_porcentaje = probabilidad * 100
probabilidad_porcentaje_redondeada = round(probabilidad_porcentaje, 2)

# Mostrar el resultado
print(
    "La probabilidad de que el depósito medio sea $670,000 o más es:",
    probabilidad_porcentaje_redondeada,
    "%",
)
