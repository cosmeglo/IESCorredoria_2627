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


def gol_azul():
    global goles_azul
    goles_azul += 1
    actualizar_marcador()


def gol_rojo():
    global goles_burdeos
    goles_burdeos += 1
    actualizar_marcador()


ventana.onkey(gol_azul, "a")
ventana.onkey(gol_rojo, "b")

ventana.listen()
actualizar_marcador()
ventana.mainloop()
