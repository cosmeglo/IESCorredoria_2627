import turtle

ventana = turtle.Screen()
ventana.title("Marcador Futbolín - Versión 2")
ventana.setup(600, 400)

lapiz = turtle.Turtle()
lapiz.hideturtle()
lapiz.penup()

estrella = turtle.Turtle()
estrella.hideturtle()
estrella.penup()
estrella.color("gold")

goles_azul = 0
goles_burdeos = 0

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

    lapiz.goto(0, 80)
    lapiz.color("black")
    lapiz.write(f"Azul {goles_azul} - {goles_burdeos} Burdeos", 
                align="center", font=("Arial", 24, "bold"))

    lapiz.goto(0, 20)
    if goles_azul > goles_burdeos:
        lapiz.color("blue")
        lapiz.write("Va ganando Azul", align="center", font=("Arial", 20, "bold"))
        dibujar_estrella(-180, 90)
    elif goles_burdeos > goles_azul:
        lapiz.color("darkred")
        lapiz.write("Va ganando Burdeos", align="center", font=("Arial", 20, "bold"))
        dibujar_estrella(180, 90)
    else:
        lapiz.color("black")
        lapiz.write("Empate", align="center", font=("Arial", 20, "bold"))

def gol_azul():
    global goles_azul
    goles_azul += 1
    actualizar_pantalla()

def gol_burdeos():
    global goles_burdeos
    goles_burdeos += 1
    actualizar_pantalla()

actualizar_pantalla()

ventana.onkey(gol_azul, "a")
ventana.onkey(gol_burdeos, "b")
ventana.listen()
ventana.mainloop()