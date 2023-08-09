import tkinter as tk
from tkinter import simpledialog, messagebox

def suma():
    num1 = float(simpledialog.askstring("Suma", "Ingrese el primer número:"))
    num2 = float(simpledialog.askstring("Suma", "Ingrese el segundo número:"))
    resultado = num1 + num2
    messagebox.showinfo("Resultado", f"La suma es: {resultado}")

def resta():
    num1 = float(simpledialog.askstring("Resta", "Ingrese el primer número:"))
    num2 = float(simpledialog.askstring("Resta", "Ingrese el segundo número:"))
    resultado = num1 - num2
    messagebox.showinfo("Resultado", f"La resta es: {resultado}")

def multiplicacion():
    num1 = float(simpledialog.askstring("Multiplicación", "Ingrese el primer número:"))
    num2 = float(simpledialog.askstring("Multiplicación", "Ingrese el segundo número:"))
    resultado = num1 * num2
    messagebox.showinfo("Resultado", f"La multiplicación es: {resultado}")

def division():
    num1 = float(simpledialog.askstring("División", "Ingrese el primer número:"))
    num2 = float(simpledialog.askstring("División", "Ingrese el segundo número:"))
    if num2 != 0:
        resultado = num1 / num2
        messagebox.showinfo("Resultado", f"La división es: {resultado}")
    else:
        messagebox.showerror("Error", "No se puede dividir por cero.")

root = tk.Tk()
root.title("Calculadora Básica")

menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

submenu_operaciones = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Operaciones", menu=submenu_operaciones)
submenu_operaciones.add_command(label="Suma", command=suma)
submenu_operaciones.add_command(label="Resta", command=resta)
submenu_operaciones.add_command(label="Multiplicación", command=multiplicacion)
submenu_operaciones.add_command(label="División", command=division)

root.mainloop()
