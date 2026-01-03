import turtle
import tkinter as tk

# Fenêtre turtle
screen = turtle.Screen()
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

# Récupérer la fenêtre Tkinter
root = screen.getcanvas().winfo_toplevel()

# Fonction appelée quand on tape
def ecrire(event):
    pen.clear()
    pen.write(entry.get())

# Champ de texte (Entry)
entry = tk.Entry(root)
entry.pack()

# Lier la frappe clavier à la fonction
entry.bind("<KeyRelease>", ecrire)

turtle.mainloop()
