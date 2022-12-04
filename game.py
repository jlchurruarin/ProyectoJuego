from controller import Controller
from constantes import *
import math
import json
import pygame
import sqlite3
from game_object_proyectil import Bullet

class Game():

    def __init__(self, screen):
        self.points = 0
        self.total_time = 0
        self.lista_forms = []
        self.config_path = "resourses/game_config.json"

        self.screen = screen

        self.vidas_restantes = 0
        
        self.load_config()

        self.load_ranking()

        self.draw_bg()

        #pygame.mixer.music.load("{0}".format(GAME_PATH))
        #pygame.mixer.music.set_volume(0)
        #pygame.mixer.music.play(-1)


    def add_points(self, points):
        self.points += points

    def add_time(self, segundos):
        self.total_time += segundos

    def get_total_time(self):
        return self.total_time

    def get_points(self):
        return self.points

    def add_form(self, form):
        self.lista_forms.append(form)

    def get_forms(self):
        return self.lista_forms

    def get_vidas_restantes(self):
        return self.vidas_restantes

    def set_vidas_restantes(self, vidas):
        self.vidas_restantes = vidas

    def set_player_id(self, id):
        config = list(filter(lambda dict: dict["id"] == id, self.config["Personajes"]))
        self.player_id = id
        self.vidas_restantes = config[0]["lives"]
        self.points = 0
        self.total_time = 0

    def get_player_id(self):
        return self.player_id

    def get_game_min_top_item(self):
        if len(self.ranking) < 10:
            print(len(self.ranking))
            self.ranking = [{
                    "nombre": "",
                    "puntaje": 0,
                    "tiempo_restante": 0
                }]
        return self.ranking[-1]

    def get_raking(self):
        self.load_ranking()
        return self.ranking

    def get_menu_config(self, name):
        config = list(filter(lambda dict: dict["name"] == name, self.config["Menus"]))
        if len(config) > 0:
            retorno = config[0]
        else:
            retorno = False
        return retorno

    def load_config(self):
        config_path = "{0}{1}".format(GAME_PATH,self.config_path)
        self.config = self.leerJSON(nombre_archivo=config_path, clave_principal="Config")

    def leerJSON(self, nombre_archivo, clave_principal) -> None:
        with open(nombre_archivo, "r") as archivo:
            dict_json = json.load(archivo)
        return dict_json[clave_principal]

    def draw_bg(self):
        bg_game = pygame.image.load("{0}{1}".format(GAME_PATH,"images/Background/Blue.png")).convert_alpha()
        bg_game_rect = bg_game.get_rect()
        cant_img_bg_h = math.ceil(ANCHO_VENTANA / bg_game_rect.width)
        cant_img_bg_y = math.ceil(ALTO_VENTANA / bg_game_rect.height)

        for img_y in range(cant_img_bg_y):
            for img_h in range(cant_img_bg_h):
                self.screen.blit(bg_game, (img_h * bg_game_rect.width, img_y * bg_game_rect.height))

    def load_ranking(self):
        try:
            ranking = []
            conexion=sqlite3.connect("prueba.db")
            sentencia = "SELECT * FROM ranking ORDER BY puntaje DESC, tiempo_restante DESC LIMIT 10"
            cursor=conexion.execute(sentencia)
            for fila in cursor:
            #    print(fila)
                dict = {
                    "nombre": fila[1],
                    "puntaje": fila[2],
                    "tiempo_restante": fila[3]
                }
                ranking.append(dict)

        except:
            sentencia = ''' create  table ranking
                   (
                           id integer primary key autoincrement,
                           nombre text,
                           puntaje integer,
                           tiempo_restante integer
                   )
               '''

            conexion.execute(sentencia)
            #print("Generamos BD")
        finally:
            conexion.close()
            self.ranking = ranking
            #print("Cerramos la conexión")

            #self.insert_ranking("jose", 123, 200)
            #self.insert_ranking("jose2", 1, 1)
            #self.insert_ranking("JLC151", 400000, 151)
            #self.insert_ranking("JLC149", 400000, 149)


    def insert_ranking(self, nombre, puntaje, tiempo_restante):
        try:
            conexion=sqlite3.connect("prueba.db")
            conexion.execute("INSERT INTO ranking(nombre, puntaje, tiempo_restante) values (?,?,?)", (nombre, puntaje, tiempo_restante))
            conexion.commit()
        except:
            print("Error al intentar cargar datos a la base de datos")
        finally:
            conexion.close()