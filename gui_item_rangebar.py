import pygame
from pygame.locals import *
from gui_item_widget import Widget
from constantes import *


class RangeBar(Widget):
    def __init__(self,master,x,y,w,h,
                f_set_value,
                f_get_value,
                value_min=1, value_max=5,image_background=None,image_dot=None,image_progress=None, 
                text="",font="Verdana",font_size=30,font_color=C_WHITE):

        super().__init__(master,x,y,w,h,None,None,image_background,text,font,font_size,font_color, text_offset_y=-15, img_coord_y=h/2)

        self.f_get_value = f_get_value 
        self.value = int(f_get_value() * 100)

        if image_progress != None:
            self.surface_element = pygame.image.load("{0}{1}".format(GAME_PATH,image_progress))
            self.surface_element = pygame.transform.scale(self.surface_element,(w/value_max, h/2)).convert_alpha()
        else:
            self.surface_element = pygame.Surface((w/self.value, h/4), pygame.SRCALPHA, 32)
            self.surface_element.fill((125, 125, 0))

        if image_dot != None:
            self.surface_dot = pygame.image.load("{0}{1}".format(GAME_PATH,image_dot))
            self.surface_dot = pygame.transform.scale(self.surface_dot,(h/2, h/2)).convert_alpha()
        else:
            self.surface_dot = pygame.Surface((h/2, h/2), pygame.SRCALPHA, 32)
            self.surface_dot.fill((0, 125, 125))

        self.value_min = value_min
        self.value_max = value_max

        self.f_set_value = f_set_value

        self.render()
        
    def render(self):
        super().render()
        for x in range(int(self.value)):
            self.slave_surface.blit(self.surface_element, (x*self.w/self.value_max, self.h/4*3 - self.surface_element.get_rect().height/2))
        self.slave_surface.blit(self.surface_dot, ((self.w/self.value_max * self.value) - self.surface_dot.get_rect().width/2 , self.h/2))
        

    def update(self, lista_eventos, delta_ms=None):
        self.value = int(self.f_get_value() * 100)
        mousePos = pygame.mouse.get_pos()
        if self.slave_rect_collide.collidepoint(mousePos):
            if(pygame.mouse.get_pressed()[0]):
                self.set_volume((mousePos[0]-self.x-self.master_form.x))

        self.render()
    
    def set_volume(self, pos_click_x):
        ancho_value = self.w/self.value_max
        self.value = int(pos_click_x / ancho_value)
        self.f_set_value(self.value)

