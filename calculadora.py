import tkinter as tk

def click_event(event):
    # Obtiene el contenido actual del campo de entrada (entry)
    current = str(entry.get())
    # Obtiene el texto del botón clicado durante el evento
    text = event.widget.cget("text")
    # Borra el contenido actual del campo de entrada
    entry.delete(0, tk.END)
    # Inserta el número u operador clicado al final del campo de entrada
    entry.insert(tk.END, current + text)

def clear():
    # Borra todo el contenido del campo de entrada
    entry.delete(0, tk.END)

def calculate():
    try:
        # Evalúa la expresión matemática del campo de entrada
        result = eval(entry.get())
        # Borra el contenido del campo de entrada
        entry.delete(0, tk.END)
        # Muestra el resultado en el campo de entrada
        entry.insert(tk.END, result)
    except Exception as e:
        # Si hay un error en la evaluación, muestra "Error" en el campo de entrada
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculadora Básica")

# Crear el campo de entrada
entry = tk.Entry(root, font="Helvetica 20 bold", bd=5, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Crear los botones numéricos
button_values = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("0", 4, 0), (".", 4, 1)
]

for value, row, col in button_values:
    # Crear un botón con el valor numérico y configuraciones de apariencia
    button = tk.Button(root, text=value, font="Helvetica 20", padx=15, pady=15)
    # Colocar el botón en la fila y columna especificada
    button.grid(row=row, column=col)
    # Asociar la función click_event() al evento clic izquierdo en el botón
    button.bind("<Button-1>", click_event)

# Crear los botones de operadores
operators = ["+", "-", "*", "/"]
row_counter = 1
col_counter = 3

for operator in operators:
    # Crear un botón con el operador y configuraciones de apariencia
    button = tk.Button(root, text=operator, font="Helvetica 20", padx=15, pady=15)
    # Colocar el botón en la fila y columna especificada
    button.grid(row=row_counter, column=col_counter)
    # Asociar la función click_event() al evento clic izquierdo en el botón
    button.bind("<Button-1>", click_event)
    # Pasar a la siguiente fila para el próximo botón
    row_counter += 1

# Botón de igual
button_equal = tk.Button(root, text="=", font="Helvetica 20", padx=15, pady=15, command=calculate)
button_equal.grid(row=4, column=2)

# Botón de limpiar
button_clear = tk.Button(root, text="C", font="Helvetica 20", padx=15, pady=15, command=clear)
button_clear.grid(row=4, column=1)

root.mainloop()
