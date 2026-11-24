import turtle

ventana = turtle.Screen()
ventana.title("Marcador Futbolín - Versión 1")
lapiz = turtle.Turtle()
lapiz.hideturtle()

def gol_azul():
    lapiz.clear()
    lapiz.color("blue")
    lapiz.write("Gol", align="center", font=("Arial", 36, "bold"))

def gol_burdeos():
    lapiz.clear()
    lapiz.color("darkred")
    lapiz.write("Gol", align="center", font=("Arial", 36, "bold"))

ventana.onkey(gol_azul, "a")
ventana.onkey(gol_burdeos, "b")
ventana.listen()
ventana.mainloop()