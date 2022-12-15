import pygame
from game_object import GameObject
from animacion import Animacion
from constantes import *


class Bullet(GameObject):

    def __init__(self,master_form, owner, x, y, direction, config, 
                f_get_effects_state, f_get_effects_volumen) -> None:

        '''
        Clase que representa a un proyectil

        Recibe por parametro el formulario padre, el objeto dueño, posición x, posición y, la dirección, la configuración del objeto (desde game_config.json),
        la función que devuelve el estado de los efectos de sonido y la función que devuelve el nivel de volumen de los efectos de sonido
        '''

        for item in config:
            setattr(self, item, config[item])

        super().__init__(   master_form=master_form, x=x, y=y, w=self.width, h=self.heigth, 
                            frame_rate_ms=self.frame_rate_ms, move_rate_ms=self.move_rate_ms)

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

        self.direction = direction
        if self.direction == DIRECTION_R:
            self.animation = self.idle_r
        else:
            self.animation = self.idle_l
        self.image_background = self.animation.next_frame()
        self.rect = self.image_background.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.owner = owner
        self.muerto = False

        self.f_get_effects_state = f_get_effects_state
        self.f_get_effects_volumen = f_get_effects_volumen
        self.sounds = {}

        self.sounds["hit"] = pygame.mixer.Sound("{0}sounds/objects/rock/hit.mp3".format(GAME_PATH))
        self.sounds["death"] = pygame.mixer.Sound("{0}sounds/objects/rock/hit.mp3".format(GAME_PATH))

        for sound in self.sounds:
            self.sounds[sound].set_volume(self.f_get_effects_volumen())

        self.rect_kill_collition = pygame.Rect(self.rect.x, self.rect.y , self.rect.w , self.rect.h)
        self.rects = [self.rect_kill_collition]

        self.render()

    def update(self, delta_ms)->None:
        '''
        Método que realiza el update del objeto (movimiento y animación)

        Recibe por parametro la diferencia de milisegundos desde el ultimo llamada al método
        '''
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)


    def do_movement(self,delta_ms):
        '''
        Método que realiza el movimiento del objeto segun su ratio de movimiento (move rate)

        Recibe por parametro la diferencia de milisegundos desde el ultimo llamada al método
        '''
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):

            self.tiempo_transcurrido_move = 0
            if self.direction == DIRECTION_R:
                self.add_x(self.velocity)
            else:
                self.add_x(-self.velocity)

            if (self.x + self.w < 0 or self.x > ANCHO_VENTANA):
                self.hit()

    def add_x(self, delta_x):
        '''
        Método que mueve el objeto sobre el eje x

        Recibe la cantidad de pixeles que se debe mover el objeto (admite positivos -> y negativos <-)
        '''
        super().add_x(delta_x)
        self.rect_kill_collition.x += delta_x
        

    def add_y(self, delta_y):
        '''
        Método que mueve el objeto sobre el eje y

        Recibe la cantidad de pixeles que se debe mover el objeto (admite positivos para mover hacia abajo y negativos para mover hacia arriba)
        '''
        super().add_y(delta_y)
        self.rect_kill_collition.y += delta_y


    def hit(self):
        if not self.muerto:
            super().hit()
            if self.f_get_effects_state():
                if not self.muerto:
                    self.sounds["hit"].set_volume(self.f_get_effects_volumen())
                    self.sounds["hit"].play()
                else:
                    self.sounds["death"].set_volume(self.f_get_effects_volumen())
                    self.sounds["death"].play()

    def actualizar_volumen(self, music_onoff, sounds_onoff, volumen_music, volumen_sounds):
        pass