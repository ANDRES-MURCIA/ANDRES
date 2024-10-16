import numpy as np  # Para cálculos numéricos
import scipy.stats as stats  # Para herramientas estadísticas

# Datos del problema
n_muestra = 36  # Tamaño de la muestra
p_promedio = 0.10  # Proporción promedio de defectuosas
probabilidad_derecha = 0.225  # Probabilidad de que exceda p

# Cálculo del error estándar de la proporción
error_estandar_proporcion = np.sqrt((p_promedio * (1 - p_promedio)) / n_muestra)

# Cálculo del valor crítico de z para la cola derecha (1 - probabilidad_derecha)
z_critico = stats.norm.ppf(1 - probabilidad_derecha)

# Cálculo del valor de p para el cual se detiene el proceso
p_detencion = p_promedio + z_critico * error_estandar_proporcion
p_detencion = p_detencion * 100  # Convertimos a porcentaje
print(p_detencion)
