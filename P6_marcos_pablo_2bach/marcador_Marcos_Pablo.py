import turtle 

 

ventana = turtle.Screen() 

ventana.title("Marcador Futbolín - V2") 

ventana.setup(600, 400) 

 

# Lápiz para textos 

lapiz = turtle.Turtle() 

lapiz.hideturtle() 

lapiz.penup() 

 

# Lápiz independiente para la estrella 

lapiz_estrella = turtle.Turtle() 

lapiz_estrella.hideturtle() 

lapiz_estrella.speed(0) 

 

goles_azul = 0 

goles_burdeos = 0 

 

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

     

    # Mostrar tanteo de cada equipo 

    lapiz.goto(-120, 40) 

    lapiz.color("blue") 

    lapiz.write(f"Azul: {goles_azul}", align="center", font=("Arial", 22, "bold")) 

     

    lapiz.goto(120, 40) 

    lapiz.color("#800020") 

    lapiz.write(f"Burdeos: {goles_burdeos}", align="center", font=("Arial", 22, "bold")) 

     

    # Estado del partido y estrella 

    lapiz.goto(0, -40) 

    if goles_azul > goles_burdeos: 

        lapiz.color("blue") 

        lapiz.write("Va ganando Azul", align="center", font=("Arial", 20, "bold")) 

        dibujar_estrella(-135, 95, "gold") 

    elif goles_burdeos > goles_azul: 

        lapiz.color("#800020") 

        lapiz.write("Va ganando Burdeos", align="center", font=("Arial", 20, "bold")) 

        dibujar_estrella(105, 95, "gold") 

    else: 

        lapiz.color("black") 

        lapiz.write("Empate", align="center", font=("Arial", 20, "bold")) 

        lapiz_estrella.clear() 

 

def gol_azul(): 

    global goles_azul 

    goles_azul += 1 

    actualizar_marcador() 

 

def gol_burdeos(): 

    global goles_burdeos 

    goles_burdeos += 1 

    actualizar_marcador() 

 

actualizar_marcador() 

 

ventana.onkey(gol_azul, "a") 

ventana.onkey(gol_burdeos, "b") 

ventana.listen() 

ventana.mainloop() 