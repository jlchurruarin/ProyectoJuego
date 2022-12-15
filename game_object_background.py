
import pygame
from game_object import GameObject
from constantes import *

class Background(GameObject):



    def __init__(self,master_form, x, y, 
                    config):

        '''
        Clase background, la cual contiene las imagenes del fondo para el efecto parallax

        Recibe por parametro el formulario padre, la posición x y la posición y, y un diccionario con la configuración del objeto
        '''            

        super().__init__(master_form=master_form, x=x, y=y, w=ANCHO_VENTANA, h=ALTO_VENTANA)

        self.sounds = []
        self.imagenes = []
        
        for item in config:
            imagen = {}
            imagen["velocity"] = item["velocity"]
            imagen["tiempo_transcurrido"] = 0
            imagen["image"] = pygame.image.load("{0}{1}".format(GAME_PATH, item["image"]))
            imagen["image"] = pygame.transform.scale(imagen["image"],(ANCHO_VENTANA, ALTO_VENTANA)).convert_alpha()
            imagen["rect"] = imagen["image"].get_rect()
            self.imagenes.append(imagen)

        self.render()

    def do_movement(self, delta_ms):
        pass

    def add_x(self,delta_x):
        '''
        Método que mueve el fondo segun la velocidad de cada capa

        Recibe por parametro la variación de la posición x y desplaza las capas del fondo
        '''
        for layer in self.imagenes:
            layer["rect"].x += int(delta_x * layer["velocity"])

    def update(self, delta_ms=None):
        '''
        Método que realiza una actualización del objeto en pantalla

        Recibe por parametro los misilegundos que transcurrieron desde el ultimo update
        '''

        self.image_background = pygame.Surface((self.w,self.h), pygame.SRCALPHA)
        for layer in self.imagenes:
            if layer["rect"].x < 0:
                layer["rect"].x += ANCHO_VENTANA
            elif layer["rect"].x > ANCHO_VENTANA:
                layer["rect"].x -= ANCHO_VENTANA

            self.image_background.blit(layer["image"],layer["rect"])
            self.image_background.blit(layer["image"],(layer["rect"].x-ANCHO_VENTANA, layer["rect"].y))

        super().update()
        

