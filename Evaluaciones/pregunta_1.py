import numpy as np
import scipy.stats as stats

# Datos de altura en cm
alturas = [
    161,
    158,
    159,
    150,
    158,
    159,
    153,
    158,
    157,
    151,
    160,
    153,
    153,
    161,
    152,
    154,
    151,
    161,
    158,
    160,
    156,
    153,
    160,
    157,
]

# Parámetros
confianza = 0.95
n = len(alturas)
media_muestra = np.mean(alturas)
desviacion_std_muestra = np.std(alturas, ddof=1)

# Cálculo del intervalo de confianza
alpha = 1 - confianza
t_critico = stats.t.ppf(
    1 - alpha / 2, df=n - 1
)  # Valor crítico de t para 95% de confianza
margen_error = t_critico * (desviacion_std_muestra / np.sqrt(n))

# Límite inferior y superior
limite_inferior = media_muestra - margen_error
limite_superior = media_muestra + margen_error

limite_inferior, limite_superior

print(limite_inferior)
print(limite_superior)
