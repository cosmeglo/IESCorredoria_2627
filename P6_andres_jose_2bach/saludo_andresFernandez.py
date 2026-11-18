import turtle
ventana = turtle.Screen()
ventana.title("Mi saludo")
lapiz = turtle.Turtle()
lapiz.hideturtle()
lapiz.color("purple")
lapiz.write("Andrés", align="center", font=("Calibri", 20, "normal"))
ventana.mainloop()