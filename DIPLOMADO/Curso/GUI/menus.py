from tkinter import *
from tkinter import messagebox

def accion_submenu1():
    messagebox.showinfo("Submenú 1", "¡Has seleccionado Submenú 1!")

def accion_submenu2():
    messagebox.showinfo("Submenú 2", "¡Has seleccionado Submenú 2!")

def accion_submenu3():
    messagebox.showinfo("Submenú 3", "¡Has seleccionado Submenú 3!")

def accion_salir():
    ventana.quit()

ventana = Tk()
ventana.title("Menú y Submenús")

barra_menu = Menu(ventana)
ventana.config(menu=barra_menu)

menu_archivo = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Salir", command=accion_salir)

menu_opciones = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Opciones", menu=menu_opciones)

menu_opciones.add_command(label="Submenú 1", command=accion_submenu1)
menu_opciones.add_command(label="Submenú 2", command=accion_submenu2)
menu_opciones.add_command(label="Submenú 3", command=accion_submenu3)

ventana.mainloop()
