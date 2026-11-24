
import turtle

ventana = turtle.Screen()
ventana.setup(700, 450)
ventana.title("Real Madrid vs Barcelona")
ventana.bgcolor("#E8EDF2")

lapiz = turtle.Turtle()
lapiz.hideturtle()
lapiz.speed(0)

madrid = 0
barcelona = 0


def actualizar():
    lapiz.clear()

    # Titulo y datos del partido
    lapiz.penup()
    lapiz.goto(0, 175)
    lapiz.color("#172B4D")
    lapiz.write("EL CLASICO", align="center",
                font=("Arial", 26, "bold"))

    lapiz.goto(0, 140)
    lapiz.color("#555555")
    lapiz.write("LIGA | JORNADA 12 | 2026/27",
                align="center", font=("Arial", 11, "normal"))

    # Equipos
    lapiz.goto(-180, 65)
    lapiz.color("#2456A6")
    lapiz.write("REAL MADRID", align="center",
                font=("Arial", 17, "bold"))

    lapiz.goto(180, 65)
    lapiz.color("#A52A40")
    lapiz.write("BARCELONA", align="center",
                font=("Arial", 17, "bold"))

    # Resultado
    lapiz.goto(0, -5)
    lapiz.color("black")
    lapiz.write(str(madrid) + "   -   " + str(barcelona),
                align="center", font=("Arial", 32, "bold"))

    # Estado del partido
    lapiz.goto(0, -75)

    if madrid == barcelona:
        lapiz.color("#333333")
        texto = "EMPATE"
    elif madrid > barcelona:
        lapiz.color("#2456A6")
        texto = "VA GANANDO EL REAL MADRID"
    else:
        lapiz.color("#A52A40")
        texto = "VA GANANDO EL BARCELONA"

    lapiz.write(texto, align="center",
                font=("Arial", 17, "bold"))

    # Informacion inferior
    lapiz.goto(0, -130)
    lapiz.color("#555555")
    lapiz.write("MARCADOR EN DIRECTO",
                align="center", font=("Arial", 12, "bold"))

    lapiz.goto(0, -165)
    lapiz.write("A: Gol Real Madrid     B: Gol Barcelona",
                align="center", font=("Arial", 11, "normal"))


def gol_madrid():
    global madrid
    madrid = madrid + 1
    actualizar()


def gol_barcelona():
    global barcelona
    barcelona = barcelona + 1
    actualizar()


ventana.onkey(gol_madrid, "a")
ventana.onkey(gol_barcelona, "b")

ventana.listen()
actualizar()
ventana.mainloop()
