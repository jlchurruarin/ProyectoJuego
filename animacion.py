import pygame
from constantes import *
import re

class Animaciones:
    def __init__(self):
        self.animations = []

    def add_animation(self, name_animation, direccion, animacion):
        dict_animation = {  'name': name_animation,
                            'direction': direccion,
                            'animation': animacion
                            }
        self.animations.append(dict_animation)


    def get_animation(self, name_animation, direccion):

        return self.animations[name_animation][direccion]


    def is_same_animation(self, name_animation, animation):

        retorno = False
        if (animation == self.animations[name_animation][0] or animation == self.animations[name_animation][1]):
            retorno = True
        
        return retorno


class Animacion:
    
    def __init__(self, path, w, h, columnas=0, filas=0, quantity=0, flip=False, step = 1, start_frame=0, end_frame=0, normal_loop=True, inverted_loop=False, last_frame_loop=False):

        self.frames_list = []
        self.frame = 0

        #Propiedades de la animación
        if last_frame_loop:
            self.normal_loop = False
            self.inverted_loop = False
            self.last_frame_loop = True
        elif inverted_loop:
            self.normal_loop = False
            self.inverted_loop = True
            self.last_frame_loop = False
            self.frame_variacion = 1
        elif normal_loop:
            self.normal_loop = True
            self.inverted_loop = False
            self.last_frame_loop = False
        else:
            self.normal_loop = False
            self.inverted_loop = False
            self.last_frame_loop = False

        if re.search(r"\{0\}",path) is not None:
            path = "{0}{1}".format(GAME_PATH, path)
            self.frames_list = self.__getSpritesListFromSeparateFiles(path_format=path, w=w, h=h, quantity=quantity, flip=flip, repeat_frame=1)
        else:
            path = "{0}{1}".format(GAME_PATH, path)
            self.frames_list = self.__getSpritesListFromSpriteSheet(path=path, w=w, h=h, columnas=columnas, filas=filas, step=step, flip=flip)


        """         
        
        if end_frame > start_frame:
            self.frames_list = self.frames_list[start_frame:end_frame]
        else:
            self.frames_list = self.frames_list[start_frame:end_frame:-1]
        """
        if end_frame == 0:
            end_frame = len(self.frames_list)

        self.frames_list = self.frames_list[start_frame:end_frame]
        

    def next_frame(self):

        if self.normal_loop:        # Cuando llega al final de la animación vuelve al primer fotograma
            if(len(self.frames_list) != self.frame):
                self.frame += 1
                retorno = self.frames_list[self.frame - 1]
            else:
                self.frame = 0
                retorno = self.frames_list[-1]
        elif self.inverted_loop:    # Cuando llega al final de la animación los vuelve a mostrar pero en orden inverso
            if(len(self.frames_list) != self.frame and self.frame != 0):
                self.frame += self.frame_variacion
                retorno = self.frames_list[self.frame - 1]
            else:
                self.frame_variacion = -1 * self.frame_variacion
                self.frame += self.frame_variacion
                retorno = self.frames_list[self.frame - 1]
        elif self.last_frame_loop:  # Cuando llega al final de la animación muestra el ultimo fotoframa indefinidamente
            retorno = self.frames_list[self.frame - 1]
        else:
            retorno = False         # La animación no tiene mas fotogramas y no debe repetirse

        return retorno

    def reset_frame(self):
        self.frame = 0

    def __getSpritesListFromSeparateFiles(self, path_format, w, h, quantity,flip=False,scale=1,repeat_frame=1):
        lista = []
        for i in range(1,quantity+1):
            path = path_format.format(i)
            surface_fotograma = pygame.image.load(path)
            if(w != 0 and h != 0):
                surface_fotograma = pygame.transform.scale(surface_fotograma,(w, h)).convert_alpha()
            if(flip):
                surface_fotograma = pygame.transform.flip(surface_fotograma,True,False).convert_alpha() 
            
            for i in range(repeat_frame):
                lista.append(surface_fotograma)
        return lista

    def __getSpritesListFromSpriteSheet(self, path, w, h, columnas,filas,flip=False, step= 1):
        lista_frames = []
        surface_imagen = pygame.image.load(path)

        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
        
        for fila in range(filas):
            for columna in range(0,columnas,step):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto).convert_alpha()
                if(flip):
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False)
                if(w != 0 and h != 0):
                    surface_fotograma = pygame.transform.scale(surface_fotograma, (w, h))
                lista_frames.append(surface_fotograma)

        return lista_frames