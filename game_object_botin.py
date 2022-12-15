
from game_object import GameObject
from animacion import Animacion

class Botin(GameObject):

    lista_botines = []

    #def __init__(self, x, y, speed_walk, frame_rate_ms, move_rate_ms, f_add_points, scale=100) -> None:
    def __init__(self,master_form, x, y, 
                    config, 
                    f_add_points, 
                    normal_loop=True, inverted_loop=False, last_frame_loop=False):

        '''
        Clase Botin, la cual contiene los objetos que son recolectables del juego

        Recibe por parametro el formulario padre, la posición x y la posición y, 
        un diccionario con la configuración del objeto y la referencia a una funcion para agregar puntos al juego
        '''

        for item in config:
            setattr(self, item, config[item])

        super().__init__(master_form=master_form, x=x, y=y, w=self.width, h=self.heigth, frame_rate_ms=self.frame_rate_ms, move_rate_ms=self.move_rate_ms)
        
        self.animations = []

        for animation in config["animations_dict"]:
            new_animation = Animacion(
                            path= config["animations_dict"][animation]["image"],
                            w=self.width,
                            h=self.heigth,
                            columnas= config["animations_dict"][animation]["columnas"],
                            filas= config["animations_dict"][animation]["filas"],
                            quantity = config["animations_dict"][animation]["quantity"],
                            flip= config["animations_dict"][animation]["flip"],
                            start_frame= config["animations_dict"][animation]["start_frame"],
                            end_frame= config["animations_dict"][animation]["end_frame"],
                            step = config["animations_dict"][animation]["step"],
                            normal_loop= config["animations_dict"][animation]["normal_loop"],
                            inverted_loop = config["animations_dict"][animation]["inverted_loop"],
                            last_frame_loop = config["animations_dict"][animation]["last_frame_loop"]
                        )
            setattr(self, animation, new_animation)

            self.animations.append(getattr(self, animation))

        self.f_add_points = f_add_points
        self._animation = self.idle

        self.muerto = False
        self.image_background = self.animation.next_frame()
        self.rect = self.image_background.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rects = [self.rect]

        self.lista_botines.append(self)

        self.render()

    def recolectado(self):
        '''
        Método de recolectado de objeto

        Agrega los puntos y desaparece el objeto de pantalla
        '''
        if not self.muerto:
            self.f_add_points(1000)
            self.muerto = True


    def do_movement(self, delta_ms):
        '''
        Método que realiza el movimiento del objeto

        Recibe por parametro la diferencia de milisegundos desde el ultimo llamado
        '''

        # Los objetos botin no tienen movimiento, de realiza un pass por compatibilidad
        pass


    def add_x(self,delta_x):
        '''
        Método que agrega un valor a la posición x del objeto, se utiliza cuando el jugador se mueve

        Recibe por parametro el valor de x a sumar a la posición del objeto
        '''

        super().add_x(delta_x)
        for rect in self.rects:
            rect.x += delta_x

    def update(self, delta_ms=None):
        '''
        Método que realiza el update del objeto (movimiento y animación)

        Recibe por parametro la diferencia de milisegundos desde el ultimo llamado
        '''
        
        super().update()
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
        
