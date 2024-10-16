import scipy.stats as stats

# Datos
mu = 864500  # Media poblacional
sigma = 15000  # Desviación estándar
n = 25  # Tamaño de la muestra
x_bar = 857500  # Media muestral deseada

# Calcular la desviación estándar de la media muestral
sigma_x_bar = sigma / (n ** 0.5)

# Calcular el valor Z
Z = (x_bar - mu) / sigma_x_bar

# Calcular la probabilidad acumulada
probabilidad = stats.norm.cdf(Z)

# Redondear a 4 decimales
probabilidad_redondeada = round(probabilidad, 4)

print("La probabilidad es:", probabilidad_redondeada)
