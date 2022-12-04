import pygame
from gui_item_widget import Widget
from constantes import *

class Imagen(Widget):
    
    def __init__(self,master_form,x,y,w,h,color_background=None,color_border=None,image_background=None):
        super().__init__(master_form,x,y,w,h,color_background,color_border,image_background)

        self.render()

    def update(self, lista_eventos=None, delta_ms=None):
        self.render()

    
