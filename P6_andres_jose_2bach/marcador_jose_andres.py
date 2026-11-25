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

import turtle

# Configuración de la ventana
ventana = turtle.Screen()
ventana.setup(700, 500)
ventana.title("Marcador Futbolín - Derbi Asturiano")

# Contadores de goles directos
goles_sporting = 0
goles_oviedo = 0

# Lápiz principal para los mensajes y tanteo
lapiz = turtle.Turtle()
lapiz.hideturtle()
lapiz.penup()

def actualizar_pantalla(texto_aviso, color_texto):
    lapiz.clear()
    
    # 1. Mensaje de aviso de gol
    lapiz.goto(0, 100)
    lapiz.color(color_texto)
    lapiz.write(texto_aviso, align="center", font=("Arial", 20, "bold"))
    
    # 2. Estado de la partida
    lapiz.goto(0, 20)
    lapiz.color("black")
    
    if goles_sporting > goles_oviedo:
        estado = "Va ganando Sporting de Gijón"
    elif goles_oviedo > goles_sporting:
        estado = "Va ganando Real Oviedo"
    else:
        estado = "Empate"
        
    lapiz.write(f"Sporting de Gijón  {goles_sporting}  -  {goles_oviedo}  Real Oviedo\n{estado}", align="center", font=("Arial", 16, "bold"))
    
    # 3. Leyenda simplificada
    lapiz.goto(0, -120)
    lapiz.color("gray")
    leyenda = "Leyenda:\nTecla a: Gol Sporting de Gijón | Tecla b: Gol Real Oviedo"
    lapiz.write(leyenda, align="center", font=("Arial", 11, "normal"))

def gol_sporting():
    global goles_sporting
    goles_sporting += 1
    actualizar_pantalla("¡GOL DEL SPORTING DE GIJÓN!", "red")

def gol_oviedo():
    global goles_oviedo
    goles_oviedo += 1
    actualizar_pantalla("¡GOL DEL REAL OVIEDO!", "blue")

# Mensaje inicial del partido
actualizar_pantalla("¡Comienza el derbi asturiano!", "black")

# Asignación de teclas
ventana.onkey(gol_sporting, "a")
ventana.onkey(gol_oviedo, "b")
ventana.listen()
ventana.mainloop()
