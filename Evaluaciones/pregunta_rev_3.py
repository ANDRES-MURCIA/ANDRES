import scipy.stats as stats

# Datos del problema
n = 52  # Número de niños nacidos
p = 0.07  # Probabilidad de morir antes de un mes
k = 6  # Número máximo de muertes

# Calcular la probabilidad acumulativa de que 6 o menos mueran
probabilidad = stats.binom.cdf(k, n, p)

# Convertir a porcentaje y redondear a dos decimales
probabilidad_porcentaje = probabilidad * 100
probabilidad_porcentaje_redondeada = round(probabilidad_porcentaje, 2)

# Mostrar el resultado
print(
    "La probabilidad de que 6 o menos niños mueran antes de alcanzar el mes de vida es:",
    probabilidad_porcentaje_redondeada,
    "%",
)
