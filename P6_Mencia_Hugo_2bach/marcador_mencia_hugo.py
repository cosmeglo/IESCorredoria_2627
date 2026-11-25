import turtle

ventana = turtle.Screen()
ventana.title("Marcador Futbolín - Versión 3")
ventana.setup(700, 450)

lapiz = turtle.Turtle()
lapiz.hideturtle()
lapiz.penup()

estrella = turtle.Turtle()
estrella.hideturtle()
estrella.penup()
estrella.color("gold")

goles_azul = 0
goles_burdeos = 0
historial = []

def dibujar_estrella(x, y):
    estrella.clear()
    estrella.goto(x, y)
    estrella.pendown()
    estrella.begin_fill()
    for i in range(5):
        estrella.forward(30)
        estrella.right(144)
    estrella.end_fill()
    estrella.penup()

def actualizar_pantalla():
    lapiz.clear()
    estrella.clear()

    lapiz.goto(0, 100)
    lapiz.color("black")
    lapiz.write(f"Azul {goles_azul} - {goles_burdeos} Burdeos", 
                align="center", font=("Arial", 28, "bold"))

    lapiz.goto(0, 40)
    if goles_azul > goles_burdeos:
        lapiz.color("blue")
        lapiz.write("Va ganando Azul", align="center", font=("Arial", 20, "bold"))
        dibujar_estrella(-200, 110)
    elif goles_burdeos > goles_azul:
        lapiz.color("darkred")
        lapiz.write("Va ganando Burdeos", align="center", font=("Arial", 20, "bold"))
        dibujar_estrella(200, 110)
    else:
        lapiz.color("black")
        lapiz.write("Empate", align="center", font=("Arial", 20, "bold"))

    lapiz.goto(0, -120)
    lapiz.color("gray")
    lapiz.write("a = Gol Azul  |  b = Gol Burdeos  |  z = Anular último gol (VAR)", 
                align="center", font=("Arial", 12, "normal"))

def gol_azul():
    global goles_azul
    goles_azul += 1
    historial.append("azul")
    actualizar_pantalla()

def gol_burdeos():
    global goles_burdeos
    goles_burdeos += 1
    historial.append("burdeos")
    actualizar_pantalla()

def anular_gol():
    global goles_azul, goles_burdeos
    if len(historial) > 0:
        ultimo = historial.pop()
        if ultimo == "azul":
            goles_azul -= 1
        else:
            goles_burdeos -= 1
        actualizar_pantalla()

actualizar_pantalla()

ventana.onkey(gol_azul, "a")
ventana.onkey(gol_burdeos, "b")
ventana.onkey(anular_gol, "z")
ventana.listen()
ventana.mainloop()