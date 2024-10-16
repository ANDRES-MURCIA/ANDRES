import math
import scipy.stats as stats

# Datos
E = 3000  # Error máximo permitido
sigma = 30000  # Desviación estándar
n = 350  # Tamaño de la muestra

# Cálculo del valor crítico Z
Z = (E * math.sqrt(n)) / sigma

# Determinar el nivel de confianza correspondiente al valor Z
nivel_confianza = 2 * (1 - stats.norm.cdf(abs(Z)))

# Convertir a porcentaje
nivel_confianza_porcentaje = round(nivel_confianza * 100, 2)

print("El porcentaje de confianza es:", nivel_confianza_porcentaje, "%")
