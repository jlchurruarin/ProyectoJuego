
from game_object_enemy import Enemy
from animacion import Animacion
from constantes import *
import random 
import pygame

class Dust(Enemy):

    #def __init__(self, x, y, speed_walk, frame_rate_ms, move_rate_ms, f_add_points, scale=100) -> None:
    def __init__(self,master_form, x, y, config, 
                    f_add_points, f_get_coords_player, f_get_game_volume, lista_plataformas):

        '''
        Clase que representa al enemigo Dust

        Recibe por parametro el formulario padre, la posición x, la posición y, la configuración del objeto (desde game_config.json)
        la funcion del juego que agrega puntos, la funcion que obtiene las coordenadas del jugador, 
        la funcion que obtiene el volumen y la lista del plataformas del nivel
        '''

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
        self._direction = DIRECTION_L
        self.inicial_lives = self.lives
        self.image_background = self.animation.next_frame()
        self.rect = self.image_background.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.inicial_rect_x = self.rect.x
        self.inicial_rect_y = self.rect.y
        self.is_player_near = False
        self.move_x = 0
        self.move_restante = [0, 0]

        self.f_add_points = f_add_points
        self.f_get_coords_player = f_get_coords_player
        self.f_trigger_action = self.run_to_player
        self.f_get_game_volume = f_get_game_volume

        self.muerto = False

        self.rect_ground_collition = pygame.Rect(self.rect.x + 15, self.rect.y + self.rect.h / 2, self.rect.w - 30, self.rect.h / 2)
        self.rect_muerte_aplastado = pygame.Rect(self.rect.x + self.rect.w / 6, self.rect.y + self.rect.h / 2.5, self.rect.w / 4, GROUND_RECT_H)
        self.rect_muerte_proyectil = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, self.rect.h)
        self.rect_daño_jugador = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, self.rect.h)

        self.rects = [self.rect_muerte_aplastado, self.rect_muerte_proyectil, self.rect_daño_jugador, self.rect_ground_collition]

        self.render()

    @property
    def direction(self):
        return self._direction
    
    @direction.setter
    def direction(self, new_direction):
        '''
        Setter de dirección, se utiliza para cambiar la animación en el caso que cambie la direción
        '''
        if self._direction != new_direction:
            self._direction = new_direction
            if self.animation == self.walk_l:
                self.animation = self.walk_r
            elif self.animation == self.walk_r:
                self.animation = self.walk_l
            elif self.animation == self.idle_r:
                self.animation = self.idle_l
            elif self.animation == self.idle_l:
                self.animation = self.idle_r

        #print(str(self.rect_ground_collition.x) + " - " + str(self.rect_ground_collition.y))

    def do_movement(self, delta_ms):
        '''
        Método que realiza el movimiento del objeto

        Recibe por parametro la diferencia de milisegundos desde el ultimo llamado
        '''

        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):

            if self.is_player_near and not self.muerto:     #En el caso que el jugador este cerca, modificamos el movimiento a la velocidad de speed_run
                coords = self.f_get_coords_player()
                if coords[0] > self.rect_ground_collition.x:
                    self.move_x = self.speed_run
                else:
                    self.move_x = -self.speed_run
            
            elif not self.is_player_near and not self.muerto:   #En el caso que el jugador no este cerca, se mueve aleatoriamente
                if self.move_restante[0] == 0 and self.move_restante[1] == 0:
                    self.move_restante = [random.randint(
                                            self.inicial_rect_x-self.rect_ground_collition.x-self.walk_range[0], 
                                            self.inicial_rect_x-self.rect_ground_collition.x+self.walk_range[0]
                                            ),
                                         0]
                    #print(self.move_restante)
                else:
                    if self.move_restante[0] > 0:
                        self.move_x = self.speed_walk 
                        self.move_restante[0] -= self.speed_walk
                        if self.move_restante[0] < 0:
                            self.move_restante[0] = 0
                            self.move_x = -self.move_restante[0]
                    else:
                        self.move_x = -self.speed_walk
                        self.move_restante[0] += self.speed_walk
                        if self.move_restante[0] > 0:
                            self.move_restante[0] = 0
                            self.move_x = self.move_restante[0]

            self.add_x_move(self.move_x)

            self.is_player_near = False
            self.move_x = 0

        return super().do_movement(delta_ms)

    def do_animation(self, delta_ms):
        '''
        Método que muestra la animación del objeto

        Recibe por parametro la diferencia de milisegundos desde el ultimo llamado
        '''
        super().do_animation(delta_ms)

    def run_to_player(self):
        '''
        Método que hace que el enemigo corra hacia el jugador
        '''
        self.is_player_near = True

    def respawn(self):
        '''
        Método que realiza un respawn del enemigo
        '''
        self.move_restante = [0,0]
        return super().respawn()

    def add_x(self, delta_x):
        '''
        Método que agrega un valor a la posición x del objeto, se utiliza cuando el jugador se mueve

        Recibe por parametro el valor de x a sumar a la posición del objeto
        '''
        self.inicial_rect_x += delta_x
        super().add_x_move(delta_x)