
import turtle

ventana = turtle.Screen()
ventana.title("Marcador del partido")
ventana.setup(600, 400)

# Lápiz para mostrar el marcador
lapiz = turtle.Turtle()
lapiz.hideturtle()
lapiz.penup()

# Lápiz independiente para dibujar la estrella
estrella = turtle.Turtle()
estrella.hideturtle()
estrella.speed(0)
estrella.penup()

# Contadores de goles
goles_azul = 0
goles_burdeos = 0

# Lista para guardar el historial de goles
historial_goles = []


def dibujar_estrella(x, y, color):
    estrella.clear()
    estrella.penup()
    estrella.goto(x, y)
    estrella.setheading(0)
    estrella.color(color)
    estrella.pendown()
    estrella.begin_fill()

    for i in range(5):
        estrella.forward(30)
        estrella.right(144)

    estrella.end_fill()
    estrella.penup()


def actualizar_marcador():
    lapiz.clear()
    estrella.clear()

    # Mostrar resultado actual
    lapiz.color("black")
    lapiz.goto(0, 130)
    lapiz.write(f"Azul {goles_azul} - {goles_burdeos} Burdeos",
                align="center",
                font=("Arial", 20, "bold"))

    if goles_azul == goles_burdeos:
        lapiz.color("black")
        lapiz.goto(0, 80)
        lapiz.write("Empate", align="center",
                    font=("Arial", 24, "bold"))

    elif goles_azul > goles_burdeos:
        lapiz.color("blue")
        lapiz.goto(0, 80)
        lapiz.write("Va ganando Azul",
                    align="center",
                    font=("Arial", 24, "bold"))

        dibujar_estrella(170, 85, "blue")

    else:
        lapiz.color("maroon")
        lapiz.goto(0, 80)
        lapiz.write("Va ganando Burdeos",
                    align="center",
                    font=("Arial", 24, "bold"))

        dibujar_estrella(170, 85, "maroon")

    # Leyenda de las teclas
    lapiz.color("black")
    lapiz.goto(0, -80)
    lapiz.write("TECLAS DEL FUTBOLÍN",
                align="center",
                font=("Arial", 14, "bold"))

    lapiz.goto(0, -110)
    lapiz.write("Tecla a: Suma gol al equipo Azul",
                align="center",
                font=("Arial", 12, "normal"))

    lapiz.goto(0, -135)
    lapiz.write("Tecla b: Suma gol al equipo Burdeos",
                align="center",
                font=("Arial", 12, "normal"))

    lapiz.goto(0, -160)
    lapiz.write("Tecla z: Deshace el último gol (VAR)",
                align="center",
                font=("Arial", 12, "normal"))


def gol_azul():
    global goles_azul
    goles_azul += 1
    historial_goles.append("azul")
    actualizar_marcador()


def gol_rojo():
    global goles_burdeos
    goles_burdeos += 1
    historial_goles.append("burdeos")
    actualizar_marcador()


def deshacer_gol():
    global goles_azul, goles_burdeos

    # Comprobar que hay goles en el historial
    if len(historial_goles) > 0:
        ultimo_gol = historial_goles.pop()

        if ultimo_gol == "azul":
            goles_azul -= 1
        else:
            goles_burdeos -= 1

        actualizar_marcador()


# Asociar las teclas a las funciones
ventana.onkey(gol_azul, "a")
ventana.onkey(gol_rojo, "b")
ventana.onkey(deshacer_gol, "z")

ventana.listen()
actualizar_marcador()

ventana.mainloop()