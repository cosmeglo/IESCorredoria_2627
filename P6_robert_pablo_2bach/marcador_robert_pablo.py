import turtle

ventana = turtle.Screen()
ventana.title("Marcador Azul vs Burdeos")
ventana.bgcolor("white")
ventana.setup(width=600, height=400)

lapiz = turtle.Turtle()
lapiz.hideturtle()
lapiz.penup()
lapiz.goto(0, 50)

estrella = turtle.Turtle()
estrella.hideturtle()
estrella.penup()
estrella.speed(0)

goles_azul = 0
goles_burdeos = 0


def dibujar_estrella(x, y, color):
    """Dibuja una estrella de 5 puntas (5 segmentos con giros de 144°)."""
    estrella.clear()
    estrella.color(color)
    estrella.goto(x, y)
    estrella.pendown()
    estrella.setheading(90)
    for _ in range(5):
        estrella.forward(40)
        estrella.right(144)
    estrella.penup()


def actualizar_marcador():
    """Actualiza el texto del marcador y la estrella según el estado."""
    lapiz.clear()
    estrella.clear()

    if goles_azul == goles_burdeos:
        lapiz.color("black")
        mensaje = "Empate"
        lapiz.write(mensaje, align="center", font=("Arial", 28, "bold"))
    elif goles_azul > goles_burdeos:
        lapiz.color("blue")
        mensaje = "Va ganando Azul"
        lapiz.write(mensaje, align="center", font=("Arial", 28, "bold"))
        dibujar_estrella(-180, 40, "blue")
    else:
        lapiz.color("maroon")
        mensaje = "Va ganando Burdeos"
        lapiz.write(mensaje, align="center", font=("Arial", 28, "bold"))
        dibujar_estrella(180, 40, "maroon")

    lapiz.goto(0, -20)
    lapiz.color("black")
    lapiz.write(f"Azul {goles_azul} - {goles_burdeos} Burdeos",
                align="center", font=("Arial", 18, "normal"))
    lapiz.goto(0, 50) 


def gol_Azul():
    global goles_azul
    goles_azul += 1
    actualizar_marcador()


def gol_Bourdeos():
    global goles_burdeos
    goles_burdeos += 1
    actualizar_marcador()


actualizar_marcador()

ventana.onkey(gol_Azul, "a")
ventana.onkey(gol_Bourdeos, "b")
ventana.listen()
ventana.mainloop()