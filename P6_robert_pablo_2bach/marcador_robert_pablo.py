import turtle
ventana = turtle.Screen()
lapiz = turtle.Turtle()
lapiz.hideturtle()

def gol_Azul():
    lapiz.clear()
    lapiz.color("blue")
    lapiz.write("Gol", align="center", font=("Arial", 24, "bold"))

def gol_Bourdeos():
    lapiz.clear()
    lapiz.color("maroon")
    lapiz.write("Gol", align="center", font=("Arial", 24, "bold"))

ventana.onkey(gol_Azul, "a")
ventana.onkey(gol_Bourdeos, "b")
ventana.listen()
ventana.mainloop()