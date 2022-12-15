from constantes import *
import math
import json
import pygame
import sqlite3

class Game():

    def __init__(self, screen):

        '''
        Clase que representa a la partida,

        Recibe por parametro la pantalla
        '''

        self.points = 0
        self.total_time = 0
        self.lista_forms = []
        self.config_path = "resourses/game_config.json"

        self.screen = screen

        self.vidas_restantes = 0
        
        self.load_config()

        self.load_ranking()

        self.draw_bg()


    def add_points(self, points)-> None:
        '''
        Metodo que agrega puntos al juego

        Recibe por parametros los puntos a agregar
        '''
        self.points += points

    def add_time(self, segundos)-> None:
        '''
        Metodo que acumula el tiempo total de partida

        Recibe los segundos que se debe sumar al valor total
        '''
        self.total_time += segundos

    def get_total_time(self)-> int:
        '''
        Metodo que devuelve la cantidad de segundos que acumula la partida
        '''
        return self.total_time

    def get_points(self)-> int:
        '''
        Metodo que devuelve la cantidad de puntos que acumula la partida
        '''
        return self.points

    def add_form(self, form)-> None:
        '''
        Metodo que agrega a la lista de formularios un formulario

        Recibe por parametro el formulario a agregar
        '''
        self.lista_forms.append(form)

    def get_forms(self)-> list:
        '''
        Metodo que devuelve la lista de formularios del juego
        '''
        return self.lista_forms

    def get_vidas_restantes(self)-> int:
        '''
        Metodo que devuelve la cantidad de vidas restantes del juegador en la partida
        '''
        return self.vidas_restantes

    def set_vidas_restantes(self, vidas:int)->None:
        '''
        Método que setea la cantidad de vidas restantes del jugador en la partida

        Recibe por parametro la cantidad de vidas
        '''
        self.vidas_restantes = vidas

    def set_player_id(self, id: str)-> None:
        '''
        Método que configura el personaje a utilizar en la partida

        Recibe el id del personaje a configurar
        '''
        config = list(filter(lambda dict: dict["id"] == id, self.config["Personajes"]))
        self.player_id = id
        self.vidas_restantes = config[0]["lives"]
        self.points = 0
        self.total_time = 0

    def get_player_id(self)-> str:
        '''
        Método que devuelve el id del personaje actual utilizado en la partida
        '''
        return self.player_id

    def get_game_min_top_item(self)->dict:
        '''
        Método que devuelve un diccionario con la última posición del ranking con las siguientes claves:
        "nombre", "puntaje", "tiempo_restante"
        '''
        if len(self.ranking) < 10:
            self.ranking = [{
                    "nombre": "",
                    "puntaje": 0,
                    "tiempo_restante": 0
                }]
        return self.ranking[-1]

    def get_raking(self)->list:
        '''
        Método que devuelve una lista de diccionarios con la información del ranking actualizada
        claves de cada item de la lista: "nombre", "puntaje", "tiempo_restante"
        '''
        self.load_ranking()
        return self.ranking

    def get_menu_config(self, name:str)->dict:
        '''
        Método que devuelve un diccionario con la configuración del menu indicado desde game_config.json

        Recibe por parametro el nombre del menu a buscar, en caso de no encontrarlo devuelve False
        '''
        config = list(filter(lambda dict: dict["name"] == name, self.config["Menus"]))
        if len(config) > 0:
            retorno = config[0]
        else:
            retorno = False
        return retorno

    def load_config(self)->None:
        '''
        Método que guarda la configuración del juego atributo "config" del objeto
        '''
        config_path = "{0}{1}".format(GAME_PATH,self.config_path)
        self.config = self.leerJSON(nombre_archivo=config_path, clave_principal="Config")

    def leerJSON(self, nombre_archivo:str, clave_principal:str) -> dict:
        '''
        Método que leer el archivo config y devuelve un diccionario con la información obtenida

        Recibe por parametro la ruta/nombre del archivo y la clave principal del archivo json
        '''
        with open(nombre_archivo, "r") as archivo:
            dict_json = json.load(archivo)
        return dict_json[clave_principal]

    def draw_bg(self)->None:
        '''
        Método que dibuja el fondo de los menus sobre la pantalla
        '''
        bg_game = pygame.image.load("{0}{1}".format(GAME_PATH,"images/Background/Blue.png")).convert_alpha()
        bg_game_rect = bg_game.get_rect()
        cant_img_bg_h = math.ceil(ANCHO_VENTANA / bg_game_rect.width)
        cant_img_bg_y = math.ceil(ALTO_VENTANA / bg_game_rect.height)

        for img_y in range(cant_img_bg_y):
            for img_h in range(cant_img_bg_h):
                self.screen.blit(bg_game, (img_h * bg_game_rect.width, img_y * bg_game_rect.height))

    def load_ranking(self)->None:
        '''
        Método que busca la información del ranking en la base de datos y la guarda en el atributo ranking
        
        En el caso que la base de datos no exista la genera
        '''
        try:
            ranking = []
            conexion=sqlite3.connect("ranking.db")
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

        finally:
            conexion.close()
            self.ranking = ranking


    def insert_ranking(self, nombre:str, puntaje:int, tiempo_restante:int):
        '''
        Método que inserta en la base de datos un nuevo registro

        Recibe por parametro el nombre del jugador, el puntaje hecho y el tiempo restante acumulado
        '''
        try:
            conexion=sqlite3.connect("ranking.db")
            conexion.execute("INSERT INTO ranking(nombre, puntaje, tiempo_restante) values (?,?,?)", (nombre, puntaje, tiempo_restante))
            conexion.commit()
        except:
            print("Error al intentar cargar datos a la base de datos")
            conexion.close()
            exit()
        finally:
            conexion.close()