import turtle 
ventana = turtle.Screen() 
ventana.setup(400, 300) 
lapiz = turtle.Turtle() 
lapiz.penup() 
lapiz.goto(-50, 50) 
lapiz.pendown() 
def cuadrado(lado): 
for i in range(4): 
lapiz.forward(lado) 
lapiz.right(90) 
cuadrado(100) 
ventana.mainloop()
