import numpy as np
import scipy.stats as stats

# Datos
n = 826  # Tamaño de la muestra
x = 95   # Llamadas sin respuesta

# Proporción de llamadas sin respuesta
p_hat = x / n
# Proporción de usuarios en casa
p_casa = 1 - p_hat

# Error estándar
SE = np.sqrt((p_hat * (1 - p_hat)) / n)

# Valor crítico Z para 90% de confianza
Z = stats.norm.ppf(0.9)  # 0.95 porque estamos interesados en el 90% de confianza

# Margen de error
E = Z * SE

# Límites de confianza
limite_inferior = p_casa - E
limite_superior = p_casa + E

# Convertir a porcentaje
limite_inferior_porcentaje = limite_inferior * 100
limite_superior_porcentaje = limite_superior * 100

print(limite_inferior_porcentaje)
print(limite_superior_porcentaje)
