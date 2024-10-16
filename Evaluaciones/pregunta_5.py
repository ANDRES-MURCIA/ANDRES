import numpy as np
import scipy.stats as stats

# Datos del problema
sigma = 28000  # Desviación estándar
E = 5000  # Error permitido
confianza = 1 - 0.045  # Nivel de confianza (96.5%)
N = 3000  # Tamaño de la población en el segundo caso

# Cálculo del valor crítico Z para el nivel de confianza
Z = stats.norm.ppf((1 + confianza) / 2)

# Tamaño de la muestra para una población infinita
n_infinito = (Z * sigma / E) ** 2

# Tamaño de la muestra para una población finita (N = 3000)
n_finito = (N * Z**2 * sigma**2) / (E**2 * (N - 1) + Z**2 * sigma**2)

# Resultados redondeados
print("Tamaño de la muestra para población infinita:", int(np.ceil(n_infinito)))
print("Tamaño de la muestra para una población de 3000:", int(np.ceil(n_finito)))
