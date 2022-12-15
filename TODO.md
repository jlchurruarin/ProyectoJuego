# Lista de modificaciones a realizar

### Todo

 - [ ] game_object_plataforma.py: Parametro flip innecesario, se debe llevar a game_config.json de esta forma no sería necesario tener una imagen nueva por la imagen de la plataforma espejada en el eje x
 - [ ] game_object_trampas.py y game_objects_trampas.py: Se pueden unificar los objetos, dejando solo game el objecto Trampa
 - [ ] game_main.py: Los formularios se cargan al iniciar el juego, por lo cual ocupan memoria innecesaria, para optimizarlo se deberían generar cuando se van a mostrar.
 - [ ] gui_form_*.py: la mayoria de los métodos que son llamados al presionar botones, reciben un parametro que no utilizan
 

### Bugs conocidos

- [ ] Al presionar un botón, si el mismo carga un nuevo formulario y tiene un botón en la misma posición que presionamos, el nuevo formulario puede recibir el click en el botón y ejecutar el método asociado al mismo