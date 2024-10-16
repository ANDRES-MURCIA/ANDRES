import math

# Datos
p = 0.36  # Proporción estimada
n = 300  # Tamaño de la muestra
N = 8000  # Tamaño de la población
Z = 1.96  # Valor crítico para un nivel de confianza del 95%

# Cálculo del error estándar
E = Z * math.sqrt((p * (1 - p) / n) * ((N - n) / (N - 1)))

# Redondear a 3 cifras decimales
E_redondeado = round(E, 3)

print("El error de muestreo es:", E_redondeado)
