import tkinter as tk
from tkinter import simpledialog, messagebox

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

agenda = []

def mostrar_contactos():
    if len(agenda) > 0:
        lista_contactos.delete(0, tk.END)
        for contacto in agenda:
            lista_contactos.insert(tk.END, f"{contacto.nombre} - Teléfono: {contacto.telefono} - Email: {contacto.email}")
    else:
        lista_contactos.delete(0, tk.END)
        lista_contactos.insert(tk.END, "No hay contactos en la agenda.")

def buscar_por_nombre(nombre_buscado):
    resultados = []
    for contacto in agenda:
        if nombre_buscado.lower() in contacto.nombre.lower():
            resultados.append(contacto)
    lista_contactos.delete(0, tk.END)
    if resultados:
        for resultado in resultados:
            lista_contactos.insert(tk.END, f"{resultado.nombre} - Teléfono: {resultado.telefono} - Email: {resultado.email}")
    else:
        lista_contactos.insert(tk.END, "No se encontraron contactos con ese nombre.")

def agregar_contacto():
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    email = entry_email.get()
    nuevo_contacto = Contacto(nombre, telefono, email)
    agenda.append(nuevo_contacto)
    messagebox.showinfo("Éxito", "Contacto agregado exitosamente.")
    entry_nombre.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_email.delete(0, tk.END)

root = tk.Tk()
root.title("Agenda de Contactos")

frame_agregar = tk.Frame(root)
frame_agregar.pack(padx=10, pady=10)

label_nombre = tk.Label(frame_agregar, text="Nombre:")
label_nombre.grid(row=0, column=0, sticky="w")
entry_nombre = tk.Entry(frame_agregar)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

label_telefono = tk.Label(frame_agregar, text="Teléfono:")
label_telefono.grid(row=1, column=0, sticky="w")
entry_telefono = tk.Entry(frame_agregar)
entry_telefono.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(frame_agregar, text="Email:")
label_email.grid(row=2, column=0, sticky="w")
entry_email = tk.Entry(frame_agregar)
entry_email.grid(row=2, column=1, padx=10, pady=5)

btn_agregar = tk.Button(frame_agregar, text="Agregar Contacto", command=agregar_contacto)
btn_agregar.grid(row=3, columnspan=2, pady=10)

frame_contactos = tk.Frame(root)
frame_contactos.pack(padx=10, pady=10)

lista_contactos = tk.Listbox(frame_contactos, width=50, height=10)
lista_contactos.pack()

menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

submenu_contactos = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Contactos", menu=submenu_contactos)
submenu_contactos.add_command(label="Mostrar Todos los Contactos", command=mostrar_contactos)

submenu_ver = tk.Menu(submenu_contactos, tearoff=0)
submenu_contactos.add_cascade(label="Buscar", menu=submenu_ver)
submenu_ver.add_command(label="Buscar por Nombre", command=lambda: buscar_por_nombre(simpledialog.askstring("Búsqueda", "Ingrese el nombre a buscar:")))

root.mainloop()
