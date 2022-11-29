from pygame.locals import *
import pygame
from constantes import *
from game_object_player import Player
from game_object_background import Background
from game_object_plataforma import Platform
from game_object_teleporter import Teleporter
from game_objects_trampas import Trampas
from game_object_proyectil import Bullet
from game_object_botin import Botin
from game_object_enemy_cactus import Cactus
from game_object_enemy_dust import Dust
from controller_balas import BalasController
from controller_enemy import EnemyController
from gui_form import Form
from gui_item_puntuación import Puntuación
from gui_item_imagen import Imagen
from gui_item_vida import Vida
from gui_item_cronometro import Cronometro
import json


class FormNivel(Form):
    def __init__(self,name,master_surface,
                        game_config,
                        player_id,
                        f_game_add_points, f_game_add_time, 
                        f_get_value_chk_sounds, 
                        f_get_value_chk_music, 
                        f_get_value_volume_sounds, 
                        f_get_value_volume_music,
                        f_set_game_volumen,
                        active=False):

        self.game_config = game_config
        self.level_config = self.leerJSON("{0}resourses/{1}.json".format(GAME_PATH, name))

        x=0
        y=0
        w=ANCHO_VENTANA
        h=ALTO_VENTANA

        super().__init__(name,master_surface,x,y,w,h,
                        f_get_value_chk_sounds=f_get_value_chk_sounds,
                        f_get_value_chk_music=f_get_value_chk_music,
                        f_get_value_volume_sounds=f_get_value_volume_sounds,
                        f_get_value_volume_music=f_get_value_volume_music,
                        background_image_path=None,background_color= None,color_border=None,active=active, background_sound_path=self.level_config["background_sound"])

        self.player_id = player_id

        self.f_game_add_points = f_game_add_points
        self.f_game_add_time = f_game_add_time
        self.f_get_value_chk_sounds = f_get_value_chk_sounds
        self.f_get_value_chk_music = f_get_value_chk_music
        self.f_get_value_volume_sounds = f_get_value_volume_sounds
        self.f_set_game_volumen = f_set_game_volumen

        self.tiempo_print = 0
        self.move_x = 0
        self.load_widwets()

        '''
        nivel.player.events(keys, nivel.balas_controller)
        nivel.draw(screen)
        nivel.update(delta_ms)
        nivel.player.draw(screen)
        '''


    def load_widwets(self):

        self.balas_controller = BalasController(f_remove_widwet= self.remove_winget)
        self.endgame = False
        self.points = 0
        self.lista_widget = []
        self.lista_plataformas = []
        self.lista_enemigos = []
        self.lista_botines = []
        self.lista_trampas = []
        self.lista_metas = []
        self.lista_controllers = []
        self.lista_game_objects = []
        self.lista_controllers.append(self.balas_controller)
        
        #self.imagen_fondo = Imagen( master_form=self,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_border=(0,0,0),image_background=self.level_config["background"])

        self.background = Background(master_form=self, x=0, y=0, config=self.level_config["background"])

        self.lista_widget = [self.background]
        self.lista_game_objects.append(self.background)


        self.puntuacion = Puntuación(   master_form=self,
                                        config= self.get_item_listdicts("puntuacion", self.game_config["UI"]), 
                                        f_get_points= self.get_points
                                        )
    
        self.lista_widget.append(self.puntuacion)
        
        
        player_config = self.get_item_listdicts(self.player_id, self.game_config["Personajes"])

        self.player = Player(
                    master_form= self, 
                    x= self.level_config["jugador"]["pos_x"], 
                    y= self.level_config["jugador"]["pos_y"], 
                    config=player_config,
                    f_add_bullet=self.add_bullet,
                    f_get_my_bullets= self.balas_controller.get_my_bullets_quantity,
                    f_get_chk_sounds= self.f_get_value_chk_sounds,
                    f_get_value_volume_sounds= self.f_get_value_volume_sounds)

        self.lista_widget.append(self.player)

        
        if "plataformas" in self.level_config:
            for plataforma in self.level_config["plataformas"]:
                config_plataform = self.get_item_listdicts(plataforma["id"], self.game_config["Plataformas"])
                if "flip" in plataforma:
                    flip = plataforma["flip"]
                else:
                    flip = False

                new_plataforma = Platform(
                    master_form= self,
                    x= plataforma["pos_x"],
                    y= plataforma["pos_y"],
                    config= config_plataform, 
                    flip=flip
                )
                self.lista_widget.append(new_plataforma)
                self.lista_plataformas.append(new_plataforma)
                self.lista_game_objects.append(new_plataforma)

        
        if "trampas" in self.level_config:
            for trampa in self.level_config["trampas"]:
                config_trampa = self.get_item_listdicts(trampa["id"], self.game_config["Trampas"])
                new_trampa = Trampas(
                    master_form= self,
                    x= trampa["pos_x"],
                    y= trampa["pos_y"],
                    config= config_trampa
                )
                self.lista_widget.append(new_trampa)
                self.lista_trampas.append(new_trampa)
                self.lista_game_objects.append(new_trampa)

        
        if "meta" in self.level_config:
            for teleporter in self.level_config["meta"]:
                new_meta = Teleporter(
                    master_form= self,
                    x= teleporter["pos_x"],
                    y= teleporter["pos_y"],
                    config= self.get_item_listdicts(teleporter["id"], self.game_config["Objetivos"]),
                    f_get_value_volume_sounds = self.f_get_value_volume_sounds
                )
                self.lista_widget.append(new_meta)
                self.lista_metas.append(new_meta)
                self.lista_game_objects.append(new_meta)
        
        if "enemigos" in self.level_config:
            for enemigo in self.level_config["enemigos"]:
                if enemigo["id"] == "Cactus":
                    new_enemigo = Cactus(master_form=self,
                                            x= enemigo["pos_x"], 
                                            y= enemigo["pos_y"],
                                            config= self.get_item_listdicts("Cactus", self.game_config["Enemigos"]), 
                                            f_add_points= self.add_points,
                                            f_add_bullet= self.add_bullet,
                                            f_get_game_volume = self.f_get_value_volume_sounds,
                                            f_get_coords_player = self.player.get_coords,
                                            lista_plataformas=self.lista_plataformas
                                            )
                    self.lista_widget.append(new_enemigo)
                    self.lista_enemigos.append(new_enemigo)
                    self.lista_game_objects.append(new_enemigo)

                elif enemigo["id"] == "Dust":
                    new_enemigo = Dust(master_form=self,
                                            x= enemigo["pos_x"], 
                                            y= enemigo["pos_y"],
                                            config= self.get_item_listdicts("Dust", self.game_config["Enemigos"]), 
                                            f_add_points= self.add_points,
                                            f_get_coords_player = self.player.get_coords,
                                            f_get_game_volume = self.f_get_value_volume_sounds,
                                            lista_plataformas=self.lista_plataformas
                                            )
                    self.lista_widget.append(new_enemigo)
                    self.lista_enemigos.append(new_enemigo)
                    self.lista_game_objects.append(new_enemigo)

        if "recolectables" in self.level_config:
            for botin in self.level_config["recolectables"]:
                new_botin = Botin(  master_form=self,
                                    x= botin["pos_x"], 
                                    y= botin["pos_y"],
                                    config=self.get_item_listdicts(botin["id"], self.game_config["Recolectables"]),
                                    f_add_points= self.add_points,)

                self.lista_widget.append(new_botin)
                self.lista_botines.append(new_botin)
                self.lista_game_objects.append(new_botin)
        
        self.enemy_controller = EnemyController(self.lista_enemigos, self.lista_plataformas)
        self.lista_controllers.append(self.enemy_controller)
        
        vidas = []
        for numero_vida in range(self.player.get_lives()):
            vidas.append(Vida(master_form=self, value= numero_vida + 1,
                            config=self.get_item_listdicts("player_lives", self.game_config["UI"]),
                            player_lives=self.player.get_lives))

        for vida in vidas:
            self.lista_widget.append(vida)
        

        self.cronometro = Cronometro(   master_form=self, 
                                        config=self.get_item_listdicts("cronometro", self.game_config["UI"]),
                                        segundos=180
                                        #segundos=20
                                    )

        self.lista_widget.append(self.cronometro)
        
        self.f_set_game_volumen()

    def leerJSON(self, nombre_archivo) -> None:
        with open(nombre_archivo, "r") as archivo:
            dict_json = json.load(archivo)

        return dict_json["Nivel"]

    def cargar_endgame(self, parametro="MenuPrincipal"):
        #if not self.muerto: guardar puntuación y llevar a siguiente nivel
        self.set_active(parametro)

    def update_lists(self, delta_ms):
        for controller in self.lista_controllers:
            controller.update_list(delta_ms)

    def events(self,keys):

        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.move_x = self.player.speed_walk
        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.move_x = -self.player.speed_walk
        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.move_x = 0



    def update(self, keys_pressed, delta_ms, lista_eventos=None):
        
        if LEVEL_DEBUG:
            self.tiempo_print += delta_ms
            if self.tiempo_print > 1000:
                self.tiempo_print -= 1000
                #print("Coordenadas: x:{0}, y:{1}".format(self.player.x, self.player.y))

        self.player.events(keys=keys_pressed)

        self.events(keys=keys_pressed)

        self.player.update(delta_ms=delta_ms)

        self.verificar_colisiones()

        self.update_lists(delta_ms=delta_ms)

        for item in self.lista_widget:
            item.update(delta_ms=delta_ms)

        for item in self.lista_game_objects:
            item.add_x(self.move_x)
            item.render()

        self.enemy_controller.verificar_triggers(self.player.get_coords)
    
        if self.player.muerto or self.cronometro.timeout:
            self.endgame = True
            self.cargar_endgame()

    def reset_form(self):
        self.load_widwets()
        pass

    def draw(self): 
        super().draw()
        #self.nivel_controller.draw(self.master_surface)
 
        for aux_widget in self.lista_widget:
            if aux_widget.x > -150 and aux_widget.x < 1650:
                aux_widget.draw()

    def add_x_to_game_objects(self, valor):
        for item in self.lista_game_objects:
            item.add_x(valor)
        
    def verificar_colisiones(self):

        for plataforma in self.lista_plataformas:
            if plataforma.rect_proyectil_collition.colliderect(self.player.rect_plataform_collition):
                if self.player.rect_plataform_collition.x > plataforma.rect_proyectil_collition.x:
                    self.add_x_to_game_objects(-8)
                else:
                    self.add_x_to_game_objects(8)

            for enemy in self.lista_enemigos:
                if plataforma.rect_proyectil_collition.colliderect(enemy.rect_ground_collition):
                    if enemy.rect_ground_collition.x > plataforma.rect_proyectil_collition.x:
                        enemy.add_x(8)
                    else:
                        enemy.add_x(-8)


        for botin in self.lista_botines:
            if botin.rect.colliderect(self.player.recoleccion_collition):
                if botin in self.lista_widget:
                    self.lista_widget.remove(botin)
                botin.recolectado()

        for enemy in self.lista_enemigos:
            if not enemy.muerto:
                if enemy.rect_daño_jugador.colliderect(self.player.rect_death_collition):
                    self.player.hit()

        for bala in self.balas_controller.get_list():
            for bala_dos in self.balas_controller.get_list():
                if (bala.owner != bala_dos.owner and 
                    bala.rect_kill_collition.colliderect(bala_dos.rect_kill_collition)):
                    bala.hit()
                    bala_dos.hit()

            for plataforma in self.lista_plataformas:
                if bala.rect_kill_collition.colliderect(plataforma.rect_proyectil_collition):
                    bala.hit()

            for enemy in self.lista_enemigos:
                if bala.owner != enemy and not enemy.muerto:
                    if bala.rect_kill_collition.colliderect(enemy.rect_muerte_proyectil):
                        enemy.hit()
                        bala.hit()
                else:
                    if bala.owner != self.player:
                        if bala.rect_kill_collition.colliderect(self.player.rect_death_collition):
                            bala.hit()
                            self.player.hit()

        for trampa in self.lista_trampas:
            if trampa.rect_daño_jugador.colliderect(self.player.rect_death_collition):
                self.player.hit()

        for teleport in self.lista_metas:
            if teleport.rect_teleport.colliderect(self.player.rect_death_collition):
                teleport.hit()
                self.endgame = True
                self.cargar_endgame()

    
    def add_bullet(self, owner, x, y, w , h, 
                    direction,
                    velocity, 
                    move_rate_ms, 
                    frame_rate_ms, 
                    type, lives, f_get_game_volume):
            
            config = self.get_item_listdicts("Piedra", self.game_config["Arrojables"])

            bala = Bullet(self, owner=owner, x=x+25, y=y+25, direction=direction, config=config, f_get_game_volume=f_get_game_volume)

            self.balas_controller.add_bullet(bala)
            self.lista_widget.append(bala)
            self.lista_game_objects.append(bala)

    def get_item_listdicts(self, id, lista):
        config = list(filter(lambda dict: dict["id"] == id, lista))
        if len(config) > 0:
            retorno = config[0]
        else:
            retorno = False
        return retorno

    def remove_winget(self, item):
        self.lista_widget.remove(item)

    #GAME CONTROLLER
    def add_points(self, points):
        self.points += points

    def get_points(self):
        return self.points
        
        