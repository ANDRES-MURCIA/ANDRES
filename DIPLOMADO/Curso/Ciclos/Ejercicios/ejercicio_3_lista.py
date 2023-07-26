lista = []
while True:
    for i in range(8):
        x = int(input("Ingrese los datos: ")) #1,4,4,4,7,6,8,2,2
        lista.append(x)
        
    print(lista)
    y = int(input("Que datos quieres ver si son repetidos: "))
    print("Hay ",lista.count(y), "elementos repetidos del número ", y)