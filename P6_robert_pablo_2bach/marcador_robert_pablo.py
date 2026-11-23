import turtle
ventana = turtle.Screen()
lapiz = turtle.Turtle()
lapiz.hideturtle()
def aviso():
    lapiz.clear()
    lapiz.write("Gol", align="center", font=("Arial", 24, "bold"))
ventana.onkey(aviso, "a")
ventana.onkey(aviso, "b")
ventana.listen()
ventana.mainloop()
