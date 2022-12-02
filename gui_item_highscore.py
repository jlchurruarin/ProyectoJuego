import pygame
from gui_item_widget import Widget
from constantes import *

class HighscoreTable(Widget):
    
    def __init__(self,master_form,x,y,w,h,data,image_background=None):
        super().__init__(master_form,x,y,w,h,None,None,image_background)

        data = [
            
        ]

        
        self.render()

    def update(self, delta_ms=None):
        self.render()

    
