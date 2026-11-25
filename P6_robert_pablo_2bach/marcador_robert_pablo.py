import turtle

ventana = turtle.Screen()
ventana.title("Marcador Azul vs Burdeos - Versión 3")
ventana.bgcolor("white")
ventana.setup(width=700, height=500)

lapiz = turtle.Turtle()
lapiz.hideturtle()
lapiz.penup()
lapiz.speed(0)

estrella = turtle.Turtle()
estrella.hideturtle()
estrella.penup()
estrella.speed(0)

# Contadores de goles
goles_azul = 0
goles_burdeos = 0

historial_goles = []   


def dibujar_estrella(x, y, color):
    estrella.clear()
    estrella.color(color)
    estrella.goto(x, y)
    estrella.pendown()
    estrella.setheading(90)
    for _ in range(5):
        estrella.forward(35)
        estrella.right(144)
    estrella.penup()


def actualizar_marcador():
    lapiz.clear()
    estrella.clear()

    lapiz.goto(0, 80)
    if goles_azul == goles_burdeos:
        lapiz.color("black")
        mensaje = "Empate"
        lapiz.write(mensaje, align="center", font=("Arial", 28, "bold"))
    elif goles_azul > goles_burdeos:
        lapiz.color("blue")
        mensaje = "Va ganando Azul"
        lapiz.write(mensaje, align="center", font=("Arial", 28, "bold"))
        dibujar_estrella(-170, 70, "blue")
    else:
        lapiz.color("maroon")
        mensaje = "Va ganando Burdeos"
        lapiz.write(mensaje, align="center", font=("Arial", 28, "bold"))
        dibujar_estrella(155, 70, "maroon")

    lapiz.goto(0, 20)
    lapiz.color("black")
    lapiz.write(f"Azul  {goles_azul}  -  {goles_burdeos}  Burdeos",
                align="center", font=("Arial", 22, "bold"))

    lapiz.goto(0, -80)
    lapiz.color("gray")
    lapiz.write("Leyenda:", align="center", font=("Arial", 14, "bold"))

    lapiz.goto(0, -110)
    lapiz.write("a → Gol Azul     |     b → Gol Burdeos     |     z → Anular último gol (VAR)",
                align="center", font=("Arial", 12, "normal"))


def gol_Azul():
    global goles_azul
    goles_azul += 1
    historial_goles.append("azul") 
    actualizar_marcador()


def gol_Bourdeos():
    global goles_burdeos
    goles_burdeos += 1
    historial_goles.append("burdeos")
    actualizar_marcador()


def anular_ultimo_gol():
    global goles_azul, goles_burdeos

    if len(historial_goles) == 0:
        return

    ultimo = historial_goles.pop()

    if ultimo == "azul":
        goles_azul -= 1
    else:
        goles_burdeos -= 1

    actualizar_marcador()


actualizar_marcador()

ventana.onkey(gol_Azul, "a")
ventana.onkey(gol_Bourdeos, "b")
ventana.onkey(anular_ultimo_gol, "z")
ventana.listen()
ventana.mainloop()