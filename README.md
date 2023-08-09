from tkinter import *
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text_widget.delete('1.0', END)
            text_widget.insert('1.0', file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_widget.get('1.0', END))

def change_font_size(size):
    text_widget.config(font=("Helvetica", size))

ventana = Tk()
ventana.title("Editor de Texto")

barra_menu = Menu(ventana)
ventana.config(menu=barra_menu, width=500, height=400)

archivo_menu = Menu(barra_menu, tearoff=0)
archivo_menu.add_command(label="Abrir", command=open_file)
archivo_menu.add_command(label="Guardar", command=save_file)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=ventana.quit)

formato_menu = Menu(barra_menu, tearoff=0)
formato_submenu = Menu(formato_menu, tearoff=0)
formato_submenu.add_command(label="Pequeño", command=lambda: change_font_size(10))
formato_submenu.add_command(label="Mediano", command=lambda: change_font_size(14))
formato_submenu.add_command(label="Grande", command=lambda: change_font_size(18))
formato_menu.add_cascade(label="Tamaño de Fuente", menu=formato_submenu)

barra_menu.add_cascade(label="Archivo", menu=archivo_menu)
barra_menu.add_cascade(label="Formato", menu=formato_menu)

text_widget = Text(ventana, wrap=WORD)
text_widget.pack(fill=BOTH, expand=True)

ventana.mainloop()

