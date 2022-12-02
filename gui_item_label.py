import pygame
from gui_item_widget import Widget
from constantes import *

class Label(Widget):
    
    def __init__(self,master_form,x,y,w,h, text, font, font_size, font_color, color_background=None,color_border=None,image_background=None):
        super().__init__(master_form,x,y,w,h,color_background,color_border,image_background, text, font, font_size, font_color)
        

        self.render()

    def update(self, delta_ms=None):
        self.render()

    
