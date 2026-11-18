import turtle
ventana = turtle.Screen()
ventana.title("Mi saludo")
lapiz = turtle.Turtle()
lapiz.hideturtle()
lapiz.color("blue")
lapiz.write("José", align="center", font=("Arial", 24, "normal"))
ventana.mainloop()
