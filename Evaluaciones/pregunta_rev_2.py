import numpy as np
import scipy.stats as stats

# Datos del problema
n = 150  # Tamaño de la muestra
clientes_no_leche = 18  # Clientes que no llevan leche
clientes_leche = n - clientes_no_leche  # Clientes que llevan leche

# Proporción observada
p_hat = clientes_leche / n

# Límite inferior y superior
limite_inferior = 0.84
limite_superior = 0.92

# Error estándar de la proporción
SE = np.sqrt((p_hat * (1 - p_hat)) / n)

# Error máximo
error_inferior = limite_inferior - p_hat
error_superior = limite_superior - p_hat

# Cálculo de Z para el error máximo
Z_inferior = abs(error_inferior / SE)
Z_superior = abs(error_superior / SE)

# Calcular el porcentaje de confianza
confianza_inferior = 1 - stats.norm.cdf(Z_inferior)
confianza_superior = stats.norm.cdf(Z_superior)

# Convertir a porcentaje
porcentaje_confianza_inferior = confianza_inferior * 100
porcentaje_confianza_superior = confianza_superior * 100

# Promedio de confianza
porcentaje_confianza_promedio = (
    porcentaje_confianza_inferior + porcentaje_confianza_superior
) / 2

porcentaje_confianza_promedio

print(porcentaje_confianza_promedio)
