import pygame
from pygame.locals import *
from constantes import *
from gui_item_widget import Widget

class CheckButton(Widget):
    def __init__(self,master,x,y,w,h, f_chk_value, image_on_path=None, image_off_path=None, color_background=C_GREEN,color_border=C_RED,text="",font="Arial",font_size=14,font_color=C_BLUE,on_click=None):
        
        self.image_on_path = image_on_path
        self.image_off_path = image_off_path
        self.f_chk_value = f_chk_value
        self.chk_value = f_chk_value()
        self.state = M_STATE_NORMAL
        self.on_click = on_click
        self.flag_click = False

        if self.chk_value:
            self.image_background_path = self.image_on_path
        else:
            self.image_background_path = self.image_off_path

        super().__init__(master_form=master,x=x,y=y,w=w,h=h, color_background=color_background,color_border=color_border,text=text,font=font,font_size=font_size,font_color=font_color, text_offset_x=0, text_offset_y=0)        

        if text != "":
            #tamaño imagenes original: 200x70
            #Calculamos variación de tamaño de la imagen
            delta_h = 70 / self.h
            self.image_h = self.h
            self.image_w = 150 / delta_h
            #Posicionamos la imagen en la posición de la derecha (super.render lo realiza)
            self.img_coord_x = self.w - self.image_w
            self.img_coord_y = 0
            self.text_offset_x = -self.image_w + 40
        else:
            self.image_h = self.h
            self.image_w = self.w
            self.img_coord_y = 0
            self.img_coord_x = 0
        

        self.image_background = pygame.image.load("{0}{1}".format(GAME_PATH, self.image_background_path))
        self.image_background = pygame.transform.scale(self.image_background, (self.image_w, self.image_h))


        self.render()
        
    def render(self):
        super().render()

        if self.state == M_STATE_HOVER: # Se aclara la imagen
            self.slave_surface.fill(M_BRIGHT_HOVER, special_flags=pygame.BLEND_RGB_ADD) 

    def update(self, lista_eventos, delta_ms=None):
        mousePos = pygame.mouse.get_pos()
        self.state = M_STATE_NORMAL
        if self.slave_rect_collide.collidepoint(mousePos):
            if(pygame.mouse.get_pressed()[0]):
                if not self.flag_click: 
                    self.flag_click = True
                    self.state = M_STATE_CLICK
                    self.click()
            else:
                self.flag_click = False
                self.state = M_STATE_HOVER        
        self.actualizar_imagen()
        self.render()

    def cambiar_valor_chk(self):
        self.chk_value = not self.chk_value
    
    def actualizar_imagen(self):
        if self.f_chk_value():
            self.image_background = pygame.image.load("{0}{1}".format(GAME_PATH, self.image_on_path))
        else:
            self.image_background = pygame.image.load("{0}{1}".format(GAME_PATH, self.image_off_path))

        self.image_background = pygame.transform.scale(self.image_background, (self.image_w, self.image_h))

    def click(self):
        if self.on_click != None:
            self.on_click()
        self.cambiar_valor_chk()
