import turtle

ventana = turtle.Screen()
lapiz = turtle.Turtle()
lapiz.hideturtle()

def gol_azul():
    lapiz.clear()
    lapiz.color("blue")
    lapiz.write("Gol", align="center", font=("Arial", 24, "bold"))

def gol_rojo():
    lapiz.clear()
    lapiz.color("red")
    lapiz.write("Gol", align="center", font=("Arial", 24, "bold"))

ventana.onkey(gol_azul, "a")
ventana.onkey(gol_rojo, "b")

ventana.listen()
ventana.mainloop()
 prueba
