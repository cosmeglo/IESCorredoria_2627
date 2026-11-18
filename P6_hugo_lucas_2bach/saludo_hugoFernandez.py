import turtle
ventana = turtle.Screen()
ventana.title("Mi saludo")
lapiz = turtle.Turtle()
lapiz.hideturtle()
lapiz.color("blue")
lapiz.write("Hugo", align="center", font=("Calibri cuerpo", 22, "normal"))
ventana.mainloop()