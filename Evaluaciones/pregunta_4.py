import numpy as np
import scipy.stats as stats

# Datos del primer caso
N1 = 3000  # Tamaño de la población
p = 0.87  # Proporción estimada de artículos no alterados
E = 0.04  # Error permitido (4%)
confianza1 = 0.975  # Coeficiente de confianza

# Datos del segundo caso
N2 = 15000  # Tamaño de la población
confianza2 = 0.935  # Coeficiente de confianza

# Cálculo del valor crítico Z para ambos niveles de confianza
Z1 = stats.norm.ppf((1 + confianza1) / 2)  # Coeficiente de confianza 97.5%
Z2 = stats.norm.ppf((1 + confianza2) / 2)  # Coeficiente de confianza 93.5%


# Tamaño de la muestra para la población de 2000 artículos
n1 = (N1 * Z1**2 * p * (1 - p)) / (E**2 * (N1 - 1) + Z1**2 * p * (1 - p))

# Tamaño de la muestra para la población de 20000 artículos (casi infinita)
n2 = (N2 * Z2**2 * p * (1 - p)) / (E**2 * (N2 - 1) + Z2**2 * p * (1 - p))

# Tamaño de la muestra si se considera una población infinita
n_infinito = (Z2**2 * p * (1 - p)) / E**2

# Resultados redondeados
int(np.ceil(n1)), int(np.ceil(n2)), int(np.ceil(n_infinito))

# Resultados redondeados y mostrados
print("Tamaño de la muestra para la población de 2000 artículos:", int(np.ceil(n1)))
print("Tamaño de la muestra para la población de 20000 artículos:", int(np.ceil(n2)))
print("Tamaño de la muestra para una población infinita:", int(np.ceil(n_infinito)))
