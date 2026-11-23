import turtle
ventana = turtle.Screen()
lapiz = turtle.Turtle()
lapiz.hideturtle()
def aviso(equipo, color_texto):
    lapiz.clear()
    lapiz.color(color_texto)  
    lapiz.write(f"Gol del {equipo}", align="center", font=("Arial", 22, "bold"))
ventana.onkey(lambda: aviso("Sporting de Gijon", "red"), "a")
ventana.onkey(lambda: aviso("Real Oviedo", "blue"), "b")
ventana.listen()
ventana.mainloop()