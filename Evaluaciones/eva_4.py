import scipy.stats as stats

# Datos
p_defectuosa = 0.04  # Proporción de piezas defectuosas
n = 400  # Tamaño de la muestra
p_deseada = 0.05  # Proporción deseada para la comparación

# Calcular la media y la desviación estándar de la distribución binomial
media = n * p_defectuosa
desviacion_estandar = (n * p_defectuosa * (1 - p_defectuosa)) ** 0.5

# Calcular el límite superior para más del 5% defectuosas
limite_superior = n * p_deseada

# Calcular el valor Z
Z = (limite_superior - media) / desviacion_estandar

# Calcular la probabilidad acumulada para Z
probabilidad_mas_5_por_ciento = 1 - stats.norm.cdf(Z)

# Redondear a 4 decimales
probabilidad_redondeada = round(probabilidad_mas_5_por_ciento, 4)

print(probabilidad_redondeada)
