from constantes import *
from game_object import GameObject
from animacion import Animacion
import pygame
#images/machines/teleporter_visible/teleporter_visible__x1_portal_png_1354836401

class Teleporter(GameObject):

    lista_teleports = []

    def __init__(self, master_form, x, y, config, f_get_effects_state, f_get_value_volume_sounds):

        for item in config:
            setattr(self, item, config[item])

        super().__init__(master_form, x, y, self.width, self.heigth, self.frame_rate_ms, self.move_rate_ms)

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
        
        self._animation = self.idle
        self.image_background = self.animation.next_frame()
        self.rect = self.image_background.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.f_get_value_volume_sounds = f_get_value_volume_sounds
        self.f_get_effects_state = f_get_effects_state

        self.sounds = {}

        self.sounds["hit"] = pygame.mixer.Sound("{0}sounds/objects/teleport/trigger.mp3".format(GAME_PATH))

        for sound in self.sounds:
            self.sounds[sound].set_volume(self.f_get_value_volume_sounds())

        self.rect_teleport = pygame.Rect(self.rect.x + self.rect.w/2 - 10 , self.rect.y, 20 , self.rect.h)
        self.rects = [self.rect_teleport]

        self.lista_teleports.append(self)

        self.render()

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            self.image_background = self.animation.next_frame()
        self.render()

    def update(self,delta_ms):
        super().update()
        self.do_animation(delta_ms)

    def add_x(self,delta_x):
        super().add_x(delta_x)
        for rect in self.rects:
            rect.x += delta_x

    def hit(self):
        if self.f_get_effects_state():
            self.sounds["hit"].set_volume(self.f_get_value_volume_sounds())
            self.sounds["hit"].play()