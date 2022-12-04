
from constantes import *
from game_object import GameObject
from game_object_plataforma import Platform

#"/images/assets/toy_star_1/toy_star_1__x1_glow_png_1354840045.png"

class Enemy(GameObject):

    lista_enemigos = []

    #def __init__(self, x, y, speed_walk, frame_rate_ms, move_rate_ms, f_add_points, scale=100) -> None:
    def __init__(self,master_form, x, y, w, h, speed_walk, speed_run,
                    frame_rate_ms, move_rate_ms, respawn_time, dead_points, f_add_points, lista_plataformas):

        super().__init__(master_form=master_form, x=x, y=y, w=w, h=h, frame_rate_ms=frame_rate_ms, move_rate_ms=move_rate_ms)
   
        self.speed_walk =  speed_walk
        self.speed_run = speed_run
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.respawn_time = respawn_time
        self.off_set_y_proyectil = 0
        self.tiempo_transcurrido_muerto = 0 
        self.rects = []
        self.gravity = 8
        self.move_x = 0 
        self.move_y = 0

        self.dead_points = dead_points
        self.f_add_points = f_add_points

        self.lista_plataformas = lista_plataformas

        self.lista_enemigos.append(self)

        self.render()


    def recolectado(self):
        # Reproducir sonido?
        self.f_add_points(1000)
        self.tiempo_transcurrido_muerto = 0
        self.muerto = True


    def add_x_move(self,delta_x):
        for rect in self.rects:
            rect.x += delta_x
        super().add_x(delta_x)


    def add_y_move(self,delta_y):
        for rect in self.rects:
            rect.y += delta_y
        super().add_y(delta_y)


    def is_on_platform(self):
        lista_plataformas = self.lista_plataformas
        retorno = False

        if(self.rect_ground_collition.y + self.rect_ground_collition.h >= GROUND_LEVEL):
            delta_y = self.rect_ground_collition.y + self.rect_ground_collition.h - GROUND_LEVEL
            self.add_y_move(-delta_y + 1)
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_ground_collition.colliderect(plataforma.rect_ground_collition)):
                    delta_y = self.rect_ground_collition.y - (plataforma.rect_ground_collition.y - self.rect_ground_collition.h)
                    self.add_y_move(-delta_y + 1) 
                    retorno = True
                    break
        return retorno

    def update(self, delta_ms=None):
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)

    def do_movement(self, delta_ms):
        self.tiempo_transcurrido_muerto += delta_ms

        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if self.muerto and self.tiempo_transcurrido_muerto > self.respawn_time:
                self.respawn()

            coords = self.f_get_coords_player()
            if coords[0] < self.x + self.w/2 and self.direction == DIRECTION_R:
                self.direction = DIRECTION_L
            elif coords[0] > self.x + self.w/2 and self.direction == DIRECTION_L:
                self.direction = DIRECTION_R

            self.add_x_move(self.move_x)
            self.add_y_move(self.move_y)

            if(not self.is_on_platform()):
                self.add_y_move(self.gravity)

    def do_animation(self, delta_ms):
        super().do_animation(delta_ms)

    def trigger(self, f_trigger):
        pass

    def draw(self):
        if not self.muerto:
            super().draw()

    def respawn(self):
        if self.respawn_time > 0:
            self.tiempo_transcurrido_proyectil = 0
            self.disparando = True
            self.lives = self.inicial_lives
            self.add_x_move(self.inicial_rect_x - self.rect_ground_collition.x)
            self.add_y_move(self.inicial_rect_y - self.rect_ground_collition.y)
            self.muerto = False

    def hit(self):
        super().hit()
        if self.muerto:
            self.f_add_points(self.dead_points)


    def trigger(self):
        coords = self.f_get_coords_player()
        #print(str(coords[0]) + " - " + str(coords[1]))
        if coords[0] > self.x:
            self.direction = DIRECTION_R
            self.f_trigger_action()
        if coords[0] < self.x:
            self.direction = DIRECTION_L
            self.f_trigger_action()