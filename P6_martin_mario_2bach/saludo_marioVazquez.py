import turtle
ventana = turtle.Screen()
ventana.title("Mi saludo")
lapiz = turtle.Turtle()
lapiz.hideturtle()
lapiz.color("green")
lapiz.write("Mario", align="center", font=("Arial", 24, "normal"))
ventana.mainloop()