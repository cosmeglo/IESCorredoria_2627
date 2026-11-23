
import turtle

ventana = turtle.Screen()
ventana.title("Real Madrid vs Barcelona")

lapiz = turtle.Turtle()
lapiz.hideturtle()

def gol_madrid():
    lapiz.clear()
    lapiz.color("blue")
    lapiz.write("Gol Real Madrid", align="center",
                font=("Arial", 24, "bold"))

def gol_barcelona():
    lapiz.clear()
    lapiz.color("maroon")
    lapiz.write("Gol Barcelona", align="center",
                font=("Arial", 24, "bold"))

ventana.onkey(gol_madrid, "a")
ventana.onkey(gol_barcelona, "b")

ventana.listen()
ventana.mainloop()

