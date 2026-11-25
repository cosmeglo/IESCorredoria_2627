
import turtle

ventana = turtle.Screen()
ventana.title("Marcador de futbolín")
ventana.setup(500, 300)

lapiz = turtle.Turtle()
lapiz.hideturtle()

estrella = turtle.Turtle()
estrella.hideturtle()

azul = 0
burdeos = 0

def dibujar_estrella(x, y):
    estrella.penup()
    estrella.goto(x, y)
    estrella.setheading(0)
    estrella.pendown()

    for i in range(5):
        estrella.forward(20)
        estrella.right(144)

    estrella.penup()

def actualizar():
    lapiz.clear()
    estrella.clear()

    lapiz.penup()
    lapiz.color("blue")
    lapiz.goto(-100, 70)
    lapiz.write("AZUL", align="center", font=("Arial", 18, "bold"))

    lapiz.color("maroon")
    lapiz.goto(100, 70)
    lapiz.write("BURDEOS", align="center", font=("Arial", 18, "bold"))

    lapiz.color("black")
    lapiz.goto(-100, 20)
    lapiz.write(str(azul), align="center", font=("Arial", 24, "bold"))

    lapiz.goto(100, 20)
    lapiz.write(str(burdeos), align="center", font=("Arial", 24, "bold"))

    if azul == burdeos:
        mensaje = "Empate"
    elif azul > burdeos:
        mensaje = "Va ganando Azul"
        dibujar_estrella(-150, 75)
    else:
        mensaje = "Va ganando Burdeos"
        dibujar_estrella(45, 75)

    lapiz.goto(0, -60)
    lapiz.write(mensaje, align="center", font=("Arial", 16, "bold"))

def gol_azul():
    global azul
    azul = azul + 1
    actualizar()

def gol_burdeos():
    global burdeos
    burdeos = burdeos + 1
    actualizar()

ventana.onkey(gol_azul, "a")
ventana.onkey(gol_burdeos, "b")

ventana.listen()
actualizar()
ventana.mainloop()
