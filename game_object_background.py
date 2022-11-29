
import pygame
from game_object import GameObject
from constantes import *

#"/images/assets/toy_star_1/toy_star_1__x1_glow_png_1354840045.png"

class Background(GameObject):



    def __init__(self,master_form, x, y, 
                    config):

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
        for layer in self.imagenes:
            layer["rect"].x += int(delta_x * layer["velocity"])

    def update(self, delta_ms=None):
        self.image_background = pygame.Surface((self.w,self.h), pygame.SRCALPHA)
        for layer in self.imagenes:
            if layer["rect"].x < 0:
                layer["rect"].x += ANCHO_VENTANA
            elif layer["rect"].x > ANCHO_VENTANA:
                layer["rect"].x -= ANCHO_VENTANA

            self.image_background.blit(layer["image"],layer["rect"])
            self.image_background.blit(layer["image"],(layer["rect"].x-ANCHO_VENTANA, layer["rect"].y))

        super().update()
        

