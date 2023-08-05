from tkinter import *

operacion = ""

def numero_pulsado(num):
    global operacion
    operacion += str(num)
    numero_pantalla.set(operacion)

def limpiar_pantalla():
    global operacion
    operacion = ""
    numero_pantalla.set("")

def resultado():
    global operacion
    try:
        resultado = str(eval(operacion))
        numero_pantalla.set(resultado)
        operacion = resultado
    except Exception as e:
        numero_pantalla.set("Error")
        operacion = ""

interfaz = Tk()
interfaz.title("Calculadora")
interfaz.iconbitmap("calculadora.ico")
interfaz.geometry("288x350")

frame = Frame()
frame.pack()
numero_pantalla = StringVar()

pantalla = Entry(frame, textvariable=numero_pantalla, width=40, borderwidth=10)
pantalla.grid(row=0, column=1, columnspan=4, padx=10, pady=10)
pantalla.config(justify="right", bg="black", fg="white")

boton7 = Button(frame, text="7", width=3, command=lambda: numero_pulsado("7"))
boton7.grid(row=1, column=1,padx=1, pady=1)
boton7.config(width="8", height="4")

boton8 = Button(frame, text="8", width=3, command=lambda: numero_pulsado("8"))
boton8.grid(row=1, column=2,padx=1, pady=1)
boton8.config(width="8", height="4")

boton9 = Button(frame, text="9", width=3, command=lambda: numero_pulsado("9"))
boton9.grid(row=1, column=3,padx=1, pady=1)
boton9.config(width="8", height="4")

division = Button(frame, text="/", width=3, command=lambda: numero_pulsado("/"))
division.grid(row=1, column=4,padx=1, pady=1)
division.config(width="8", height="4")

boton4 = Button(frame, text="4", width=3, command=lambda: numero_pulsado("4"))
boton4.grid(row=2, column=1,padx=1, pady=1)
boton4.config(width="8", height="4")

boton5 = Button(frame, text="5", width=3, command=lambda: numero_pulsado("5"))
boton5.grid(row=2, column=2,padx=1, pady=1)
boton5.config(width="8", height="4")

boton6 = Button(frame, text="6", width=3, command=lambda: numero_pulsado("6"))
boton6.grid(row=2, column=3,padx=1, pady=1)
boton6.config(width="8", height="4")

multiplicacion = Button(frame, text="*", width=3, command=lambda: numero_pulsado("*"))
multiplicacion.grid(row=2, column=4,padx=1, pady=1)
multiplicacion.config(width="8", height="4")

boton1 = Button(frame, text="1", width=3, command=lambda: numero_pulsado("1"))
boton1.grid(row=3, column=1,padx=1, pady=1)
boton1.config(width="8", height="4")

boton2 = Button(frame, text="2", width=3, command=lambda: numero_pulsado("2"))
boton2.grid(row=3, column=2,padx=1, pady=1)
boton2.config(width="8", height="4")

boton3 = Button(frame, text="3", width=3, command=lambda: numero_pulsado("3"))
boton3.grid(row=3, column=3,padx=1, pady=1)
boton3.config(width="8", height="4")

resta = Button(frame, text="-", width=3, command=lambda: numero_pulsado("-"))
resta.grid(row=3, column=4,padx=1, pady=1)
resta.config(width="8", height="4")

boton0 = Button(frame, text="0", width=3, command=lambda: numero_pulsado("0"))
boton0.grid(row=4, column=1,padx=1, pady=1)
boton0.config(width="8", height="4")

punto = Button(frame, text=".", width=3, command=lambda: numero_pulsado("."))
punto.grid(row=4, column=2,padx=1, pady=1)
punto.config(width="8", height="4")

igual = Button(frame, text="=", width=3, command=resultado)
igual.grid(row=4, column=3,padx=1, pady=1)
igual.config(width="8", height="4")

suma = Button(frame, text="+", width=3, command=lambda: numero_pulsado("+"))
suma.grid(row=4, column=4,padx=1, pady=1)
suma.config(width="8", height="4")

interfaz.mainloop()