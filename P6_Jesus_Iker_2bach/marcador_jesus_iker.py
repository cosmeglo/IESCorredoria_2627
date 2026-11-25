import turtle

ventana = turtle.Screen()
ventana.title("Marcador de futbolin")

lapiz = turtle.Turtle()
lapiz.hideturtle()

def aviso(color):
    lapiz.clear()
    lapiz.color(color)
    lapiz.write("Gol", align="center",
                 font=("Arial", 24, "bold"))

def gol_azul():
    aviso("blue")

def gol_burdeos():
    aviso("maroon")

ventana.onkey(gol_azul, "a")
ventana.onkey(gol_burdeos, "b")

ventana.listen()
ventana.mainloop()