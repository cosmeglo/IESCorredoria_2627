
import turtle

ventana = turtle.Screen()
ventana.title("Marcador de futbolín - VAR")
ventana.setup(500, 350)
ventana.bgcolor("white")

lapiz = turtle.Turtle()
lapiz.hideturtle()
lapiz.speed(0)

estrella = turtle.Turtle()
estrella.hideturtle()
estrella.speed(0)

goles = []


# DIBUJAR ESTRELLA
def dibujar_estrella(x, y):
    estrella.penup()
    estrella.goto(x, y)
    estrella.setheading(0)
    estrella.color("gold")
    estrella.pendown()

    for i in range(5):
        estrella.forward(20)
        estrella.right(144)

    estrella.penup()


# ACTUALIZAR MARCADOR
def actualizar():
    lapiz.clear()
    estrella.clear()

    azul = goles.count("azul")
    burdeos = goles.count("burdeos")

    # NOMBRES DE LOS EQUIPOS
    lapiz.penup()
    lapiz.color("blue")
    lapiz.goto(-100, 100)
    lapiz.write("AZUL", align="center",
                font=("Arial", 18, "bold"))

    lapiz.color("maroon")
    lapiz.goto(100, 100)
    lapiz.write("BURDEOS", align="center",
                font=("Arial", 18, "bold"))

    # GOLES
    lapiz.color("black")
    lapiz.goto(-100, 45)
    lapiz.write(str(azul), align="center",
                font=("Arial", 28, "bold"))

    lapiz.goto(100, 45)
    lapiz.write(str(burdeos), align="center",
                font=("Arial", 28, "bold"))

    # RESULTADO
    if azul == burdeos:
        mensaje = "EMPATE"
        color = "orange"

    elif azul > burdeos:
        mensaje = "VA GANANDO AZUL"
        color = "blue"
        dibujar_estrella(-160, 105)

    else:
        mensaje = "VA GANANDO BURDEOS"
        color = "maroon"
        dibujar_estrella(155, 105)

    # MOSTRAR RESULTADO
    lapiz.goto(0, -20)
    lapiz.color(color)
    lapiz.write(mensaje, align="center",
                font=("Arial", 16, "bold"))

    # CONTROLES
    lapiz.goto(0, -90)
    lapiz.color("black")
    lapiz.write("A: Gol Azul    B: Gol Burdeos",
                align="center", font=("Arial", 11, "normal"))

    lapiz.goto(0, -115)
    lapiz.write("Z: VAR (anular último gol)",
                align="center", font=("Arial", 11, "normal"))


# GOLES
def gol_azul():
    goles.append("azul")
    actualizar()


def gol_burdeos():
    goles.append("burdeos")
    actualizar()


# VAR
def var():
    if len(goles) > 0:
        goles.pop()
        actualizar()


# CONTROLES DEL TECLADO
ventana.onkey(gol_azul, "a")
ventana.onkey(gol_burdeos, "b")
ventana.onkey(var, "z")

# INICIAR
ventana.listen()
actualizar()
ventana.mainloop()