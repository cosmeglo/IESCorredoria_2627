"""Ejemplo de la primera versión del marcador de futbolín."""
import turtle

ventana = turtle.Screen()
ventana.title("Marcador de futbolín")
ventana.setup(640, 320)
texto = turtle.Turtle()
texto.hideturtle()
texto.penup()
goles = []


def dibujar():
    texto.clear()
    texto.goto(0, 35)
    texto.write(f"Azul {goles.count('Azul')} - Blanco {goles.count('Blanco')}",
                align="center", font=("Arial", 24, "bold"))
    texto.goto(0, -35)
    texto.write("a: gol de Azul     b: gol de Blanco", align="center")


def gol(equipo):
    goles.append(equipo)
    dibujar()


ventana.onkey(lambda: gol("Azul"), "a")
ventana.onkey(lambda: gol("Blanco"), "b")
dibujar()
ventana.listen()
ventana.mainloop()
