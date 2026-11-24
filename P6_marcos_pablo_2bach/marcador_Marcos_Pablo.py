import turtle 

 

ventana = turtle.Screen() 

ventana.title("Marcador Futbolín - V3 (Con VAR)") 

ventana.setup(650, 450) 

 

# Lápiz para el marcador y estado 

lapiz = turtle.Turtle() 

lapiz.hideturtle() 

lapiz.penup() 

 

# Lápiz independiente para la estrella del líder 

lapiz_estrella = turtle.Turtle() 

lapiz_estrella.hideturtle() 

lapiz_estrella.speed(0) 

 

# Lápiz fijo para la leyenda de controles 

lapiz_leyenda = turtle.Turtle() 

lapiz_leyenda.hideturtle() 

lapiz_leyenda.penup() 

 

# Lista que registra en orden qué equipo marcó cada gol 

historial_goles = [] 

 

def dibujar_leyenda(): 

    lapiz_leyenda.clear() 

    lapiz_leyenda.goto(0, -140) 

    lapiz_leyenda.color("#333333") 

    texto_leyenda = ( 

        "CONTROLES DEL MARCADOR:\n" 

        "Tecla [a]: Suma gol al equipo Azul   |   " 

        "Tecla [b]: Suma gol al equipo Burdeos   |   " 

        "Tecla [z]: VAR (Deshace el último gol)" 

    ) 

    lapiz_leyenda.write(texto_leyenda, align="center", font=("Arial", 10, "normal")) 

 

def dibujar_estrella(x, y, color): 

    lapiz_estrella.clear() 

    lapiz_estrella.penup() 

    lapiz_estrella.goto(x, y) 

    lapiz_estrella.setheading(0) 

    lapiz_estrella.color(color) 

    lapiz_estrella.pendown() 

    lapiz_estrella.begin_fill() 

    for _ in range(5): 

        lapiz_estrella.forward(30) 

        lapiz_estrella.right(144) 

    lapiz_estrella.end_fill() 

    lapiz_estrella.penup() 

 

def actualizar_marcador(): 

    lapiz.clear() 

     

    # Contar goles a partir de la lista historial_goles 

    goles_azul = historial_goles.count("Azul") 

    goles_burdeos = historial_goles.count("Burdeos") 

     

    # Mostrar resultado actual 

    lapiz.goto(-130, 60) 

    lapiz.color("blue") 

    lapiz.write(f"Azul: {goles_azul}", align="center", font=("Arial", 24, "bold")) 

     

    lapiz.goto(130, 60) 

    lapiz.color("#800020") 

    lapiz.write(f"Burdeos: {goles_burdeos}", align="center", font=("Arial", 24, "bold")) 

     

    # Mostrar estado y estrella sobre el ganador 

    lapiz.goto(0, -20) 

    if goles_azul > goles_burdeos: 

        lapiz.color("blue") 

        lapiz.write("Va ganando Azul", align="center", font=("Arial", 20, "bold")) 

        dibujar_estrella(-145, 115, "gold") 

    elif goles_burdeos > goles_azul: 

        lapiz.color("#800020") 

        lapiz.write("Va ganando Burdeos", align="center", font=("Arial", 20, "bold")) 

        dibujar_estrella(115, 115, "gold") 

    else: 

        lapiz.color("black") 

        lapiz.write("Empate", align="center", font=("Arial", 20, "bold")) 

        lapiz_estrella.clear() 

 

def gol_azul(): 

    historial_goles.append("Azul") 

    actualizar_marcador() 

 

def gol_burdeos(): 

    historial_goles.append("Burdeos") 

    actualizar_marcador() 

 

def anular_gol(): 

    # Si la lista tiene elementos, retira el último con pop() 

    if len(historial_goles) > 0: 

        historial_goles.pop() 

        actualizar_marcador() 

 

# Inicializar pantalla 

dibujar_leyenda() 

actualizar_marcador() 

 

ventana.onkey(gol_azul, "a") 

ventana.onkey(gol_burdeos, "b") 

ventana.onkey(anular_gol, "z") 

ventana.listen() 

ventana.mainloop() 
