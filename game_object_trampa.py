from game_object import GameObject
from animacion import Animacion
import pygame

class Trampa(GameObject):

    def __init__(self, master_form, x, y, w, h, animation_dict, frame_rate_ms=0, move_rate_ms=0):
        super().__init__(master_form, x, y, w, h, frame_rate_ms, move_rate_ms)

        self.stay = Animacion(
            path=animation_dict["image"],
            w= w,
            h= h,
            columnas=animation_dict["columnas"],
            filas=animation_dict["filas"],
            start_frame=animation_dict["start_frame"],
            end_frame=animation_dict["end_frame"], 
            quantity=animation_dict["quantity"]
        )

        self.animations = [
            self.stay
        ]
        
        self._animation = self.stay
        self.image_background = self.animation.next_frame()
        self.rect = self.image_background.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rect_daño_jugador = pygame.Rect(self.rect.x + self.rect.w*0.2, self.rect.y, self.rect.w*0.6, self.rect.h)

        self.rects = [self.rect_daño_jugador]

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
        