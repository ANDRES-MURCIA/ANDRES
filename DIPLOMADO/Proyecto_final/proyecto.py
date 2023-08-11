from tkinter import *
from tkinter import messagebox  
from PIL import Image, ImageTk

root = Tk()
root.title("Juego de Preguntas")
root.iconbitmap("icono.ico")
root.geometry("900x600")
root.config(bg="black")
root.resizable(0,0)

background_image = Image.open("galaxia.jpg")
background_photo = ImageTk.PhotoImage(background_image)

background_label = Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

questions = [
    {
        "question": "¿Qué significa 'GUI' en informática?",
        "options": ["a) Grand Unified Interface", "b) Graphical User Interface", "c) General User Interface", "d) Global User Integration"],
        "correct": 1
    },
    {
        "question": "¿Qué lenguaje de programación es conocido como 'el lenguaje del web'?",
        "options": ["a) Python", "b) JavaScript", "c) Java", "d) C++"],
        "correct": 1
    },
    {
        "question": "¿Qué protocolo de internet se utiliza para enviar correos electrónicos?",
        "options": ["a) FTP", "b) HTTP", "c) SMTP", "d) SSH"],
        "correct": 2
    }

]

question_label = Label(root, text="Questions", wraplength=750, font=("Helvetica", 25, "bold"))
question_label.pack(pady=20)

answer_buttons = [] 
for i in range(4):
    button = Button(root, text="Answers", command=lambda i=i: check_answer(i), height=3, width=40, font=("Helvetica", 12))
    button.pack(pady=5)
    answer_buttons.append(button)

opportunities = 2 
current_question = 0
attempts = 0
total_points = 0
highest_score = 0 

points_label = Label(root, text="Puntos", font=("Helvetica", 20, "bold"), fg="red")
points_label.pack(anchor="nw", padx=20, pady=2)

question_counter_label = Label(root, text="Preguntas", font=("Helvetica", 20, "bold"), fg="brown")
question_counter_label.pack(anchor="center", padx=10, pady=2)

highest_score_label = Label(root, text="Record", font=("Helvetica", 35, "bold"), fg="green")
highest_score_label.pack(anchor="se", padx=20, pady=2)

def load_question():
    global attempts
    if current_question < len(questions):
        question_data = questions[current_question]
        question_label.config(text=question_data["question"])

        for i in range(4):
            answer_buttons[i].config(text=question_data["options"][i])

        attempts = 0
        question_counter_label.config(text=f"Pregunta: {current_question+1}/{len(questions)}")
        points_label.config(text=f"Puntos: {total_points}/1000")  
        highest_score_label.config(text=f"Record: {highest_score}") 

def check_answer(selected):
    global current_question, opportunities, attempts, total_points, highest_score

    question_data = questions[current_question]
    correct_answer = question_data["correct"]
    attempts += 1
    
    if selected == correct_answer:
        if attempts == 1:
            total_points += 10  
        elif attempts == 2:
            total_points += 5  
        
        current_question += 1
        opportunities = 2 
        
        if total_points > highest_score:
            highest_score = total_points  
        
        if current_question < len(questions):
            load_question()
        else:
            messagebox.showinfo("Fin del juego", f"¡Has respondido todas las preguntas correctamente! Puntaje total: {total_points} puntos")
            fin = messagebox.askquestion("De nuevo", "¿Quieres superar tu record?")
            if fin == "yes":
                total_points = 0
                current_question = 0
                load_question()
            else:
                root.destroy()

    else:
        opportunities -= 1
        if opportunities > 0:
            messagebox.showinfo("Incorrecto", f"Respuesta incorrecta. Te queda {opportunities} oportunidad.")
        else:
            messagebox.showinfo("Sin oportunidades", f"¡Perdiste todas las oportunidades! Volviendo a la pregunta 1. Puntaje total: {total_points}")
            opportunities = 2  
            total_points = 0 
            current_question = 0
            load_question()

load_question()
root.mainloop()