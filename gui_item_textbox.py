import pygame
from pygame.locals import *
from gui_item_widget import Widget
from constantes import *


class TextBox(Widget):
    def __init__(self,master,x=0,y=0,w=200,h=50,color_background=C_GREEN,color_border=C_RED,image_background=None,text="",font="Arial",font_size=14,font_color=C_BLUE,on_click=None,on_click_param=None):
        super().__init__(master,x,y,w,h,color_background,color_border,image_background,text,font,font_size,font_color)
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.state = M_STATE_NORMAL
        self.writing_flag = False
        self.blink = False
        self.blink_time = 300
        self.acumulador_time_blink = 0
        self.texto = ""
        self.render()
        
    def render(self):
        super().render()
        if self.state == M_STATE_HOVER: # Se aclara la imagen
            self.slave_surface.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD) 
        elif self.state == M_STATE_CLICK: # Se oscurece la imagen
            self.slave_surface.fill(M_BRIGHT_CLICK, special_flags=pygame.BLEND_RGB_SUB) 

    def update(self, lista_eventos, delta_ms=None):

        self.acumulador_time_blink += delta_ms
        if self.acumulador_time_blink > self.blink_time:
            self.acumulador_time_blink = 0
            self.blink = not self.blink
        else:
            if self.blink and self.writing_flag:
                self._text = self.texto + "l"
                self.text_offset_x = 0
            else:
                self._text = self.texto
                self.text_offset_x = -1


        mousePos = pygame.mouse.get_pos()
        self.state = M_STATE_NORMAL
        if self.slave_rect_collide.collidepoint(mousePos):
            if(self.writing_flag):
                self.state = M_STATE_CLICK
            else:
                self.state = M_STATE_HOVER

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN :
                self.writing_flag = self.slave_rect_collide.collidepoint(evento.pos)
            if evento.type == pygame.KEYDOWN and self.writing_flag:
                if evento.key == pygame.K_ESCAPE:
                    self.writing_flag = False
                elif evento.key == pygame.K_RETURN:
                    self.writing_flag = False
                elif evento.key == pygame.K_BACKSPACE:
                    self.texto = self.texto[:-1]
                else:
                    self.texto += evento.unicode

        self.render()

    

