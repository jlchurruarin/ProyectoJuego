import pygame
from animacion import Animacion
from game_object import GameObject
from game_object_plataforma import Platform
from game_object_proyectil import Bullet
from constantes import *


class Player(GameObject):

    #def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,scale=100,lives=5) -> None:
    def __init__(self,master_form, x, y, config, vidas_restantes,
                    f_add_bullet, f_get_my_bullets, f_get_chk_sounds, f_get_value_volume_sounds):

        for item in config:
            setattr(self, item, config[item])

        super().__init__(master_form=master_form, x=x, y=y, w=self.width, h=self.heigth, frame_rate_ms=self.frame_rate_ms, move_rate_ms=self.move_rate_ms)
        '''
        self.walk_r = Animacion(
            path="images/caracters/stink/walk.png",
            w=self.width,
            h=self.heigth,
            columnas=15,
            filas=1,
            start_frame=0,
            end_frame=12, 
            flip=False
        )
        self.walk_l = Animacion(
            path="images/caracters/stink/walk.png",
            w=self.width,
            h=self.heigth,
            columnas=15,
            filas=1,
            start_frame=0,
            end_frame=12, 
            flip=True
        )

        self.stay_r = Animacion(
            path="images/caracters/stink/idle.png",
            w=self.width,
            h=self.heigth,
            columnas=16,
            filas=1,
            flip=False
        )

        self.stay_l = Animacion(
            path="images/caracters/stink/idle.png",
            w=self.width,
            h=self.heigth,
            columnas=16,
            filas=1,
            flip=True
        )
        self.jump_up_r = Animacion(
            path="images/caracters/stink/jump.png",
            w=self.width,
            h=self.heigth,
            columnas=33,
            filas=1,
            flip=False,
            end_frame=16,
            last_frame_loop=True
        )
        self.jump_down_r = Animacion(
            path="images/caracters/stink/jump.png",
            w=self.width,
            h=self.heigth,
            columnas=33,
            filas=1,
            flip=False,
            start_frame=17,
            end_frame=28,
            last_frame_loop=True
        )
        
        self.jump_up_l = Animacion(
            path="images/caracters/stink/jump.png",
            w=self.width,
            h=self.heigth,
            columnas=33,
            filas=1,
            flip=True,
            end_frame=16,
            last_frame_loop=True
        )

        self.jump_down_l = Animacion(
            path="images/caracters/stink/jump.png",
            w=self.width,
            h=self.heigth,
            columnas=33,
            filas=1,
            flip=True,
            start_frame=17,
            end_frame=28,
            last_frame_loop=True
        )

        self.shoot_r = Animacion(
            path="images/caracters/stink/jump.png",
            w=self.width,
            h=self.heigth,
            columnas=33,
            filas=1,
            flip=False,
            start_frame=12,
            end_frame=29,
            normal_loop=True
        )

        self.shoot_l = Animacion(
            path="images/caracters/stink/jump.png",
            w=self.width,
            h=self.heigth,
            columnas=33,
            filas=1,
            flip=True,
            start_frame=12,
            end_frame=29,
            normal_loop=True
        )

        self.animations = [
            self.walk_r,
            self.walk_l, 
            self.stay_r,
            self.stay_l,
            self.jump_up_r,
            self.jump_up_l, 
            self.jump_down_r,
            self.jump_down_l,
            self.shoot_l,
            self.shoot_r
        ]
        '''

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

        self.lives = vidas_restantes
        self.invulnerable = False
        self.tiempo_transcurrido_invulnerable = 0
        self.tiempo_max_invulnerable = 1500
        self.tiempo_transcurrido_move = 0
        self._animation = self.idle_r
        self.direction = DIRECTION_R
        self.image_background = self.animation.next_frame()
        self.rect = self.image_background.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.move_x = 0
        self.move_y = 0

        self.f_get_my_bullets = f_get_my_bullets
        self.f_add_bullet = f_add_bullet
        self.f_get_chk_sounds = f_get_chk_sounds
        self.f_get_value_volume_sounds = f_get_value_volume_sounds

        self.last_volume = self.f_get_value_volume_sounds()

        self.sounds = {}
        self.sounds["hit"] = pygame.mixer.Sound("{0}{1}".format(GAME_PATH, self.list_sounds["hit"]))
        self.sounds["death"] = pygame.mixer.Sound("{0}{1}".format(GAME_PATH, self.list_sounds["death"]))

        for sound in self.sounds:
            self.sounds[sound].set_volume(self.f_get_value_volume_sounds())

        self.is_jump = False
        self.is_shoot = False

        self.y_start_jump = 0
        self.enable_jump = True

        self.muerto = False
        
        self.rect_ground_collition = pygame.Rect(self.rect.x + 10 , self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w - 20, GROUND_RECT_H)
        self.rect_plataform_collition = pygame.Rect(self.rect.x + 10 , self.rect.y + 5, self.rect.w - 20, self.rect.h - 5)
        self.rect_death_collition = pygame.Rect(self.rect.x + self.rect.w / 5, self.rect.y + self.rect.h / 5, self.rect.w * 0.6, self.rect.h * 0.6)
        self.recoleccion_collition = pygame.Rect(self.rect.x, self.rect.y , self.rect.w, self.rect.h)
        
        self.rects = [self.rect_ground_collition, self.rect_death_collition, self.rect_plataform_collition, self.recoleccion_collition]

        self.render()
        


    def walk(self,direction):
        if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
            self.direction = direction
            if(direction == DIRECTION_R):
                self.move_x = self.speed_walk
                self.animation = self.walk_r
            else:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l



    def jump(self,on_off = True):

        if(on_off and self.is_jump == False):
            self.y_start_jump = self.rect_ground_collition.y
            if(self.direction == DIRECTION_R):
                self.move_x = self.speed_run
                self.move_y = -self.jump_power
                self.animation = self.jump_up_r
            else:
                self.move_x = -self.speed_run
                self.move_y = -self.jump_power
                self.animation = self.jump_up_l
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()


    def stay(self):
        if(self.animation != self.idle_r and self.animation != self.idle_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.idle_r
            else:
                self.animation = self.idle_l
            self.move_x = 0
            self.move_y = 0
            


    def shoot(self, on_off):
        if(self.animation != self.shoot_r and self.animation != self.shoot_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.shoot_r
            else:
                self.animation = self.shoot_l
            #Se debería generar una bala en la posicion del personaje

            if (self.f_get_my_bullets(owner=self) < self.proyectiles_maximos):
                # def __init__(self,master_form, owner, x, y, w, h, 
                #            velocity, direction,
                #            frame_rate_ms, move_rate_ms, 
                #            type, lives
                self.f_add_bullet(owner=self, x=self.x, y= self.y, id=self.proyectil_id, direction=self.direction)
                

            self.is_shoot = True
        if not on_off:
            self.is_shoot = False
            self.stay()



    def do_movement(self,delta_ms):

        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            if(abs(self.y_start_jump)- abs(self.rect_ground_collition.y) > self.jump_height and self.is_jump):
                self.move_y = 0
                if self.direction == DIRECTION_R:
                    self.animation = self.jump_down_r
                else:
                    self.animation = self.jump_down_l

            self.tiempo_transcurrido_move = 0

            #print(str(self.move_x) + " - " + str(self.move_y))
            if self.is_collition_plataforms():
                self.is_jump = False
                self.move_y = 0
                self.move_x = 0
                self.add_y(self.gravity)
                #self.corregir_posicion()
            else:
                #self.add_x(self.move_x)
                self.add_y(self.move_y)

            if(not self.is_on_platform()):
                self.add_y(self.gravity)
            elif(self.is_jump):
                self.jump(False)



    def add_x(self, delta_x):
        super().add_x(delta_x)
        self.rect_ground_collition.x += delta_x
        self.rect_death_collition.x += delta_x
        self.recoleccion_collition.x += delta_x
        self.rect_plataform_collition.x += delta_x
        


    def add_y(self, delta_y):
        super().add_y(delta_y)
        self.rect_ground_collition.y += delta_y
        self.rect_death_collition.y += delta_y
        self.recoleccion_collition.y += delta_y
        self.rect_plataform_collition.y += delta_y
        
        
    def is_collition_plataforms(self):
        lista_plataformas = self.master_form.lista_plataformas
        retorno = False
        for plataforma in lista_plataformas:
            if plataforma.rect_proyectil_collition.colliderect(self.rect_plataform_collition):
                retorno =  True
                break
        return retorno

    def is_on_platform(self):
        lista_plataformas = self.master_form.lista_plataformas
        retorno = False

        if(self.rect_ground_collition.y >= GROUND_LEVEL + 100):

            self.lives = 1
            self.hit()
            retorno = False
        else:
            for plataforma in lista_plataformas:
                if(self.rect_ground_collition.colliderect(plataforma.rect_ground_collition)):
                    delta_y = self.rect_ground_collition.y - (plataforma.rect_ground_collition.y - self.rect_ground_collition.h)
                    self.add_y(-delta_y + 1) 
                    retorno = True
                    break
        return retorno



    def update(self,delta_ms):
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
        self.hacer_vulnerable(delta_ms)
        

    def hacer_vulnerable(self, delta_ms):
        self.tiempo_transcurrido_invulnerable += delta_ms
        if self.invulnerable and self.tiempo_transcurrido_invulnerable > self.tiempo_max_invulnerable:
            self.invulnerable = False



    def events(self,keys):

        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not self.is_jump):
            self.walk(DIRECTION_L)
        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not self.is_jump):
            self.walk(DIRECTION_R)
        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()

        if keys[pygame.K_a]:
            if self.enable_shoot:
                self.shoot(True)
                self.enable_shoot = False
        else:
            self.enable_shoot = True
            
        if(keys[pygame.K_s]):
            #self.knife()
            pass

        if(keys[pygame.K_SPACE]):
            if self.enable_jump:
                self.enable_jump = False
                self.jump(True)
        else:
            self.enable_jump = True



    def hit(self):
        if not self.invulnerable:
            super().hit()
            self.invulnerable = True
            self.tiempo_transcurrido_invulnerable = 0
            if self.f_get_chk_sounds():
                if self.lives <= 0:
                    self.sounds["death"].set_volume(self.f_get_value_volume_sounds())
                    self.sounds["death"].play()
                else:
                    self.sounds["hit"].set_volume(self.f_get_value_volume_sounds())
                    self.sounds["hit"].play()

    def get_lives(self):
        return self.lives



    def get_coords(self):
        #print(str(self.rect_death_collition.x) + " - " + str(self.rect_death_collition.y))
        return self.rect_death_collition.x, self.rect_death_collition.y
