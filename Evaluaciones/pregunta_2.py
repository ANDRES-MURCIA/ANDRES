import numpy as np  # Para cálculos numéricos
import scipy.stats as stats  # Para herramientas estadísticas

# Datos de la encuesta
n_encuesta = 1200
votos_x = 744
proporcion_muestra = votos_x / n_encuesta

# Intervalo proporcionado
limite_inferior = 0.58
limite_superior = 0.66

# Cálculo del error estándar para la proporción
error_estandar = np.sqrt((proporcion_muestra * (1 - proporcion_muestra)) / n_encuesta)

# Cálculo del valor crítico z (para una distribución normal)
margen_error = (limite_superior - limite_inferior) / 2
z_critico = margen_error / error_estandar

# Cálculo del grado de confianza (nivel de confianza)
nivel_confianza = stats.norm.cdf(z_critico) * 2 - 1

# Convertimos el nivel de confianza a porcentaje
nivel_confianza_porcentaje = nivel_confianza * 100

nivel_confianza_porcentaje

print(nivel_confianza_porcentaje)