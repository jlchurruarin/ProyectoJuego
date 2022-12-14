import pygame
from constantes import *
from game_object import GameObject

class Platform(GameObject):
    
    lista_plataformas = []

    def __init__(self, master_form, x, y, config, flip=False):

        '''
        Clase que representa a las plataformas

        Recibe por parametro el formulario padre, la posición x, la posición y, 
        la configuración del objeto (desde game_config.json) y parametro flip que indica si la imagen debe espejarse en el eje x
        '''
        
        for item in config:
            setattr(self, item, config[item])

        super().__init__(master_form=master_form, x=x, y=y, w=self.width, h=self.heigth, image_background=self.image)
        
        if flip and self.image_background != None:
            self.image_background = pygame.transform.flip(self.image_background, True, False)

        self.render()

        self.rect_ground_collition = pygame.Rect(self.slave_rect.x + 10, self.slave_rect.y, self.slave_rect.w - 20, GROUND_RECT_H)
        self.rect_proyectil_collition = pygame.Rect(self.slave_rect.x + 5, self.slave_rect.y + GROUND_RECT_H/4, self.slave_rect.w - 10, self.slave_rect.h - GROUND_RECT_H/4)
        self.rects = [self.rect_ground_collition, self.rect_proyectil_collition]
        
        self.lista_plataformas.append(self)

    def add_x(self,delta_x)->None:
        '''
        Método que agrega un valor a la posición x del objeto, se utiliza cuando el jugador se mueve

        Recibe por parametro el valor de x a sumar a la posición del objeto
        '''
        super().add_x(delta_x)
        for rect in self.rects:
            rect.x += delta_x
        

