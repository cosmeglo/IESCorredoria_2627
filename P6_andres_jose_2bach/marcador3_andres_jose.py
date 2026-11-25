import turtle

# Configuración de la ventana
ventana = turtle.Screen()
ventana.setup(700, 500)
ventana.title("Marcador Futbolín - Derbi Asturiano")

# Lista para guardar el historial de goles en orden (necesaria para el VAR)
historial_goles = []

# Lápiz principal para los mensajes y tanteo
lapiz = turtle.Turtle()
lapiz.hideturtle()
lapiz.penup()

def actualizar_pantalla(texto_aviso, color_texto):
    lapiz.clear()
    
    # Contamos los goles actuales a partir de la lista
    goles_sporting = historial_goles.count("Sporting")
    goles_oviedo = historial_goles.count("Oviedo")
    
    # 1. Mensaje de aviso de gol / VAR
    lapiz.goto(0, 80)
    lapiz.color(color_texto)
    lapiz.write(texto_aviso, align="center", font=("Arial", 20, "bold"))
    
    # 2. Estado de la partida
    lapiz.goto(0, -10)
    lapiz.color("black")
    
    if goles_sporting > goles_oviedo:
        estado = "Va ganando Sporting de Gijón"
    elif goles_oviedo > goles_sporting:
        estado = "Va ganando Real Oviedo"
    else:
        estado = "Empate"
        
    lapiz.write(f"Sporting de Gijón  {goles_sporting}  -  {goles_oviedo}  Real Oviedo\n{estado}", align="center", font=("Arial", 16, "bold"))

def gol_sporting():
    historial_goles.append("Sporting")
    actualizar_pantalla("¡GOL DEL SPORTING DE GIJÓN!", "red")

def gol_oviedo():
    historial_goles.append("Oviedo")
    actualizar_pantalla("¡GOL DEL REAL OVIEDO!", "blue")

def var_anular():
    """Función del VAR: si la lista tiene elementos, borra el último con pop()"""
    if len(historial_goles) > 0:
        anulado = historial_goles.pop()
        equipo_anulado = "Sporting de Gijón" if anulado == "Sporting" else "Real Oviedo"
        actualizar_pantalla(f"¡VAR! Se anula el último gol del {equipo_anulado}", "purple")
    else:
        actualizar_pantalla("¡VAR! No hay goles para anular", "orange")

# Mensaje inicial del partido
actualizar_pantalla("¡Comienza el derbi asturiano!", "black")

# Asignación de teclas
ventana.onkey(gol_sporting, "a")
ventana.onkey(gol_oviedo, "b")
ventana.onkey(var_anular, "z")
ventana.listen()
ventana.mainloop()