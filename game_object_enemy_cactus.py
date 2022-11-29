
from game_object_enemy import Enemy
from animacion import Animacion
from constantes import *
import pygame

class Cactus(Enemy):

    #def __init__(self, x, y, speed_walk, frame_rate_ms, move_rate_ms, f_add_points, scale=100) -> None:
    def __init__(self,master_form, x, y, config, 
                    f_add_points, f_add_bullet, f_get_coords_player, f_get_game_volume, lista_plataformas):

        for item in config:
            setattr(self, item, config[item])

        super().__init__(master_form=master_form, x=x, y=y, w=self.width, h=self.heigth, speed_walk=self.speed_walk, speed_run=self.speed_run, frame_rate_ms=self.frame_rate_ms, move_rate_ms=self.move_rate_ms, respawn_time=self.respawn_time, f_add_points=f_add_points, dead_points=self.dead_points, lista_plataformas=lista_plataformas)
        
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
        self._direction = DIRECTION_L
        self.inicial_lives = self.lives
        self.image_background = self.animation.next_frame()
        self.rect = self.image_background.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.inicial_rect_x = self.rect.x
        self.inicial_rect_y = self.rect.y
        self.disparando = False
        self.proyectil_delay_time = 3000
        self.tiempo_transcurrido_proyectil = 0
        self.off_set_y_proyectil = 50
        self.f_add_points = f_add_points
        self.f_add_bullet = f_add_bullet
        self.f_get_coords_player = f_get_coords_player
        self.f_get_game_volume = f_get_game_volume
        self.f_trigger_action = self.shoot
        self.muerto = False

        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, self.rect.h)
        self.rect_muerte_aplastado = pygame.Rect(self.rect.x + self.rect.w / 6, self.rect.y + self.rect.h / 2.5, self.rect.w / 4, GROUND_RECT_H)
        self.rect_muerte_proyectil = pygame.Rect(self.rect.x + self.rect.w / 6, self.rect.y + self.rect.h / 2.5, self.rect.w / 3.7, self.rect.h / 2)
        self.rect_daño_jugador = pygame.Rect(self.rect.x + self.rect.w / 6, self.rect.y + self.rect.h / 2.5, self.rect.w / 3.7, self.rect.h / 2)

        self.rects = [self.rect_muerte_aplastado, self.rect_muerte_proyectil, self.rect_daño_jugador, self.rect_ground_collition]

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

    def do_movement(self, delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        return super().do_movement(delta_ms)

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_proyectil += delta_ms
        if self.tiempo_transcurrido_proyectil > self.proyectil_delay_time:
            self.disparando = False
        super().do_animation(delta_ms)

    def shoot(self):
        if not self.disparando:
            self.f_add_bullet(owner=self, x=self.x, y=self.y, w=50 , h=50, 
                        direction=self.direction,
                        velocity=5, 
                        move_rate_ms=self.move_rate_ms, 
                        frame_rate_ms=self.frame_rate_ms, 
                        type= PIEDRA, lives=1, f_get_game_volume=self.f_get_game_volume)
            self.tiempo_transcurrido_proyectil = 0
            self.disparando = True

    def add_x(self, delta_x):
        self.inicial_rect_x += delta_x
        super().add_x_move(delta_x)