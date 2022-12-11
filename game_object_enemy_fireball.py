
from game_object_enemy import Enemy
from animacion import Animacion
from constantes import *
import random 
import pygame

class Fireball(Enemy):

    #def __init__(self, x, y, speed_walk, frame_rate_ms, move_rate_ms, f_add_points, scale=100) -> None:
    def __init__(self,master_form, x, y, config, 
                    f_add_points, f_get_coords_player, f_get_game_volume, lista_plataformas):

        for item in config:
            setattr(self, item, config[item])

        super().__init__(master_form=master_form, x=x, y=y, w=self.width, h=self.heigth, speed_walk=self.speed_walk, speed_run=self.speed_run, 
                            frame_rate_ms=self.frame_rate_ms, move_rate_ms=self.move_rate_ms, respawn_time=self.respawn_time, f_add_points=f_add_points, dead_points=self.dead_points, lista_plataformas=lista_plataformas)

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
        
        self._animation = self.idle_l
        self._direction = DIRECTION_R
        self.image_background = self.animation.next_frame()
        self.rect = self.image_background.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.inicial_rect_x = self.rect.x
        self.inicial_rect_y = self.rect.y
        self.is_player_near = False
        self.move_y = self.speed_walk

        self.f_get_coords_player = f_get_coords_player
        self.f_trigger_action = self.hit
        self.jump_on = False
        self.timer_jump_min = 1000
        self.timer_jump_max = 3000
        self.f_get_game_volume = f_get_game_volume

        self.muerto = False

        self.rect_daño_jugador = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, self.rect.h)

        self.rects = [self.rect_daño_jugador]

        self.render()

    @property
    def direction(self):
        return self._direction
    
    @direction.setter
    def direction(self, new_direction):
        if self._direction != new_direction:
            self._direction = new_direction
            if self.animation == self.idle_r:
                self.animation = self.idle_l
            elif self.animation == self.idle_l:
                self.animation = self.idle_r

        #print(str(self.rect_ground_collition.x) + " - " + str(self.rect_ground_collition.y))

    def update(self, delta_ms=None):
        if self.rect_daño_jugador.y < self.inicial_rect_y - self.max_y_movement:
            self.move_y = self.speed_walk
        elif self.rect_daño_jugador.y >= self.inicial_rect_y:
            self.move_y = -self.speed_walk
        return super().update(delta_ms)

    def do_movement(self, delta_ms):
        
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):

            self.add_y_move(self.move_y)

        return super().do_movement(delta_ms)

    def add_x(self, delta_x):
        self.inicial_rect_x += delta_x
        super().add_x_move(delta_x)

    def do_animation(self, delta_ms):

        super().do_animation(delta_ms)

    def is_on_platform(self):
        return True

    def hit(self):
        pass