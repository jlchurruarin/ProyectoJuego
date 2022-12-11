## Detalle del proyecto

#### Proyecto de juego realizado en Python con pygame.

- El juego cuenta con tres niveles de longitud
- Cuenta con menú de configuración para volumen de musica y sonidos.
- Permite seleccionar entre dos personajes con diferentes habilidades
- Los niveles se configuran desde archivos json, lo cual permite adaptador con facilidad sin modificar el codigo
- Cuanta con un ranking de puntuación el cual es almacenado en una base de datos SQLite

## Video demostrativo

https://user-images.githubusercontent.com/75645175/206935096-a5d079ae-dd25-45a6-b1d9-37ff192bdfdb.mp4

## Requisitos


- Python 3.10
- Pygame

### Instalación

- Realizar instalación de Python ([como instalar python en Windows](https://docs.python.org/3/using/windows.html#installation-steps "como instalar python en Windows"))
- Realizar instalación de pygame ([Como instalar pygame](https://www.pygame.org/wiki/GettingStarted#Pygame%20Installation "Como instalar pygame"))
- Descargar el proyecto en formato zip y descomprimir o desde consola utilizando git con el siguiente comando
```sh
git clone git@github.com:jlchurruarin/ProyectoJuego.git
```

### Puesta en marcha
Ejecutar el archivo **game_main.py** con el siguiente comando:
  ```shell
python3 game_main.py
```

### Configuración

El juego puede configurarse desde el archivo **constantes.py**, en el mismo se encuentran las siguientes configuraraciones que pueden ser modificadas:

```python
ANCHO_VENTANA = 1500
ALTO_VENTANA = 800
FPS = 60
DEBUG = False
LEVEL_DEBUG = False
```

- **ANCHO_VENTANA**: Permite configurar los pixeles de ancho que tendrá la ventana del juego.
- **ALTO_VENTANA**: Permite configurar los pixeles de alto que tendrá la ventana del juego.
- **FPS**: Cantidad de fotogramas máximos que tendrá el juego.
- **DEBUG**: Permite ver los colliders de los objetos y ocultará la mayoria de las imagenes / animaciones. Imagen de ejemplo:
![debug](https://user-images.githubusercontent.com/75645175/206935363-901326e1-27cf-469f-98a5-f532e6f643eb.png)
- **LEVEL_DEBUG**: Agrega al menu principal 3 botones para acceder a los niveles directamente, sin tener que superarlos.
