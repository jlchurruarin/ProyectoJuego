from controller import Controller
from constantes import *
import math
import json
import pygame
from game_object_proyectil import Bullet

class Game():

    def __init__(self, screen):
        self.points = 0
        self.total_time = 0
        self.lista_forms = []
        self.config_path = "resourses/game_config.json"

        self.music_onoff = True
        self.music_volume = 1
        self.sounds_onoff = True
        self.sounds_volume = 1
        
        self.load_config()

        self.draw_bg(screen)

        #pygame.mixer.music.load("{0}".format(GAME_PATH))
        #pygame.mixer.music.set_volume(0)
        #pygame.mixer.music.play(-1)


    def add_points(self, points):
        self.points += points

    def add_time(self, segundos):
        self.total_time = segundos

    def get_points(self):
        return self.points

    def add_form(self, form):
        self.lista_forms.append(form)

    def get_forms(self):
        return self.lista_forms

    def get_chk_sounds(self):
        return self.sounds_onoff

    def get_chk_music(self):
        return self.music_onoff

    def get_volume_sounds(self):
        return self.sounds_volume

    def get_volume_music(self):
        return self.music_volume

    def get_menu_config(self, name):
        config = list(filter(lambda dict: dict["name"] == name, self.config["Menus"]))
        if len(config) > 0:
            retorno = config[0]
        else:
            retorno = False
        return retorno

    def set_volumen(self, music_onoff=None, sounds_onoff=None, music_volume=None, sounds_volume=None):
        if music_onoff == None:
            self.music_onoff = self.get_chk_music()
        else:
            self.music_onoff = music_onoff
        
        if music_volume == None:
            self.music_volume = self.get_volume_music()
        else:
            self.music_volume = music_volume

        if sounds_onoff == None:
            self.sounds_onoff = self.get_chk_sounds()
        else:
            self.sounds_onoff = sounds_onoff

        if sounds_volume == None:
            self.sounds_volume = self.get_volume_sounds()
        else:
            self.sounds_volume = sounds_volume

        for form in self.lista_forms:
            form.actualizar_volumen(self.music_onoff, self.sounds_onoff, self.music_volume, self.sounds_volume)
        Bullet.actualizar_volumen(Bullet, self.music_onoff, self.sounds_onoff, self.music_volume, self.sounds_volume)

    def load_config(self):
        config_path = "{0}{1}".format(GAME_PATH,self.config_path)
        self.config = self.leerJSON(nombre_archivo=config_path, clave_principal="Config")

    def leerJSON(self, nombre_archivo, clave_principal) -> None:
        with open(nombre_archivo, "r") as archivo:
            dict_json = json.load(archivo)
        return dict_json[clave_principal]

    def draw_bg(self, screen):
        bg_game = pygame.image.load("{0}{1}".format(GAME_PATH,"images/Background/Blue.png"))
        bg_game_rect = bg_game.get_rect()
        cant_img_bg_h = math.ceil(ANCHO_VENTANA / bg_game_rect.width)
        cant_img_bg_y = math.ceil(ALTO_VENTANA / bg_game_rect.height)

        for img_y in range(cant_img_bg_y):
            for img_h in range(cant_img_bg_h):
                screen.blit(bg_game, (img_h * bg_game_rect.width, img_y * bg_game_rect.height))