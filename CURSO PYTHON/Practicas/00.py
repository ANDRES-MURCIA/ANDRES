def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

print("Bienvenido a la calculadora")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

print("Elige la operación que deseas realizar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = int(input("Ingresa tu opción (1/2/3/4): "))

if opcion == 1:
    resultado = suma(num1, num2)
    print("El resultado de la suma es:", resultado)
elif opcion == 2:
    resultado = resta(num1, num2)
    print("El resultado de la resta es:", resultado)
elif opcion == 3:
    resultado = multiplicacion(num1, num2)
    print("El resultado de la multiplicación es:", resultado)
elif opcion == 4:
    if num2 != 0:
        resultado = division(num1, num2)
        print("El resultado de la división es:", resultado)
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Opción inválida. Por favor, ingresa una opción válida (1/2/3/4).")
