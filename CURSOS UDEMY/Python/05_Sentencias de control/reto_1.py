print("Tienda en linea")

compra_requerida = 1000
valor_comprado = float(input("¿Cuanto has comprado en dinero?: "))
miembro = input("Eres miembro de la tienda SI/NO?: ").lower()
descuento_alto = valor_comprado * (10 / 100)
descuento_medio = valor_comprado * (5 / 100)
valor_final_descuento_alto = valor_comprado - descuento_alto
valor_final_descuento_medio = valor_comprado - descuento_medio

if valor_comprado >= compra_requerida and miembro == "si":
    print(f"\nValor de la compra original: {valor_comprado}")
    print(
        f"""\nCumple con los requisitos para el descuento del 10%.
        \nSaldo a pagar {valor_final_descuento_alto}"""
    )
    print(f"\nEl descuento es: {descuento_alto}")

elif valor_comprado < compra_requerida and miembro == "si":
    print(f"\nValor de la compra original: {valor_comprado}")
    print(
        f"""\nCumple con los requisitos para el descuento del 5%.
        \nSaldo a pagar {valor_final_descuento_medio}"""
    )
    print(f"\nEl descuento es: {descuento_medio}")

else:
    print(f"No tienes descuentos, el valor a pagar es: {valor_comprado}")
