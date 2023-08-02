import tkinter as tk

def on_button_click(event):
    # Obtener el texto del botón presionado
    button_text = event.widget.cget('text')

    if button_text == '=':
        try:
            # Evaluar la expresión matemática y mostrar el resultado
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    else:
        # Agregar el texto del botón al final del campo de entrada
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text + button_text)

root = tk.Tk()
root.title("Calculadora")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=20)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", on_button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()