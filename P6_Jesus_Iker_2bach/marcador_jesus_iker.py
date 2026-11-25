import turtle

ventana = turtle.Screen()
ventana.title("Marcador de futbolín")
ventana.setup(700, 500)
ventana.bgcolor("white")

lapiz = turtle.Turtle()
lapiz.hideturtle()
lapiz.penup()
lapiz.speed(0)

estrella = turtle.Turtle()
estrella.hideturtle()
estrella.penup()
estrella.speed(0)

# Lista que guarda los goles en orden
goles = []

def dibujar_estrella(x, y, color):
    estrella.clear()
    estrella.goto(x, y)
    estrella.color(color)
    estrella.pendown()
    estrella.begin_fill()

    for i in range(5):
        estrella.forward(30)
        estrella.right(144)

    estrella.end_fill()
    estrella.penup()

def actualizar():
    lapiz.clear()
    estrella.clear()

    azul = goles.count("Azul")
    burdeos = goles.count("Burdeos")

    lapiz.goto(0, 130)
    lapiz.color("black")
    lapiz.write(
        f"AZUL: {azul}       BURDEOS: {burdeos}",
        align="center",
        font=("Arial", 24, "bold")
    )

    if azul > burdeos:
        mensaje = "Va ganando Azul"
        dibujar_estrella(-180, 30, "blue")

    elif burdeos > azul:
        mensaje = "Va ganando Burdeos"
        dibujar_estrella(150, 30, "maroon")

    else:
        mensaje = "Empate"

    lapiz.goto(0, 50)
    lapiz.write (mensaje, )
    align="center",
    font=("Arial", 20, "bold")
    
def gol_azul():
    goles.append("Azul")
    actualizar()

def gol_burdeos():
    goles.append("Burdeos")
    actualizar()

def anular_gol():
    if len(goles) > 0:
        goles.pop()
        actualizar()

ventana.onkey(gol_azul, "a")
ventana.onkey(gol_burdeos, "b")
ventana.onkey(anular_gol, "z")

actualizar()
ventana.listen()
ventana.mainloop()
import turtle