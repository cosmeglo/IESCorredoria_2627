# Práctica 6: Marcador de Futbolín Digital 
**Integrantes del equipo:** 
* Marcos (Integrante 1) 
* Pablo (Integrante 2) 
**Tablero de seguimiento (GitHub Project):** 
* [Acceder al tablero P6_Marcos_Pablo_2bach](https://github.com/users/marcossc10/projects/4/views/1)
  
## Funcionamiento del programa

### Cómo ejecutarlo 
1. Descargar el archivo `marcador_Marcos_Pablo.py` desde esta carpeta. 
2. Abrirlo en **Visual Studio Code** (o cualquier entorno con Python 3 instalado, ya que utiliza la librería estándar `turtle`). 
3. Ejecutar el archivo (`python marcador_Marcos_Pablo.py` o pulsando el botón *Run* en VS Code). Se abrirá una ventana gráfica con el marcador inicializado a `0 - 0` en estado de **Empate**. 

### Controles y efectos en el programa 

* **Tecla `a`:** Suma 1 gol al **equipo Azul**, registra el gol en el historial y actualiza el tanteo. 
* **Tecla `b`:** Suma 1 gol al **equipo Burdeos**, registra el gol en el historial y actualiza el tanteo. 
* **Tecla `z` (Revisión VAR):** Anula el último gol anotado eliminándolo del historial. Si el marcador está en `0 - 0`, ignora la pulsación sin producir errores. 

### Indicadores visuales 
* **Tanteo y estado:** Muestra los goles de cada equipo en su color correspondiente y un mensaje central indicando `"Va ganando Azul"`, `"Va ganando Burdeos"` o `"Empate"`. 
* **Estrella de líder:** Dibuja una estrella dorada sobre el equipo que va ganando y la borra automáticamente si se produce un empate. 
