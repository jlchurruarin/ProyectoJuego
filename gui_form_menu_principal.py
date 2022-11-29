import pygame
import sys
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_item_imagen import Imagen
from gui_item_button import Button
from gui_item_textbox import TextBox
from gui_item_progressbar import ProgressBar


class FormMenuPrincipal(Form):
    def __init__(self,config,master_surface,
                    f_get_value_chk_sounds,
                    f_get_value_chk_music,
                    f_get_value_volume_sounds,
                    f_get_value_volume_music,
                    active=False):

        for item in config:
            setattr(self, item, config[item])

        x=ANCHO_VENTANA/2 - self.width/2
        y=ALTO_VENTANA/2 - self.heigth/2

        super().__init__(name=self.name,master_surface=master_surface,x=x,y=y,w=self.width,h=self.heigth,
                        f_get_value_chk_sounds=f_get_value_chk_sounds,
                        f_get_value_chk_music=f_get_value_chk_music,
                        f_get_value_volume_sounds=f_get_value_volume_sounds,
                        f_get_value_volume_music=f_get_value_volume_music,
                        background_color = None,
                        color_border = None,
                        background_image_path=self.background_image_path, 
                        active=active, 
                        background_sound_path=self.background_sound_path)

        ANCHO_BOTON = self.botones_ancho
        ALTO_BOTON = self.botones_alto
        ANCHO_FORM = self.width
        ALTO_FORM = self.heigth

        self.btn_comenzar = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=75,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.cargar_nivel,on_click_param="Nivel1",text="Comenzar Juego",font="Verdana",font_size=30,font_color=C_WHITE)
        self.btn_clasificacion = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=150,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.mostrar_clasificacion,text="Clasificación",font="Verdana",font_size=30,font_color=C_WHITE)

        self.btn_configuracion = Button(master=self,x=ANCHO_FORM/2-75-40,y=ALTO_FORM-100-ALTO_BOTON,w=69,h=68,color_background=None,color_border=None,image_background="images/menu/icons/settings.png",on_click=self.mostrar_configuracion)
        self.btn_ayuda = Button(master=self,x=ANCHO_FORM/2+40,y=ALTO_FORM-100-ALTO_BOTON,w=69,h=68,color_background=None,color_border=None,image_background="images/menu/icons/help.png",on_click=self.mostrar_ayuda)

        self.btn_nivel_2 = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=225,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.cargar_nivel,on_click_param="Nivel2",text="Nivel 2",font="Verdana",font_size=30,font_color=C_WHITE)
        self.btn_nivel_3 = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=300,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.cargar_nivel,on_click_param="Nivel3",text="Nivel 2",font="Verdana",font_size=30,font_color=C_WHITE)

        self.btn_salir = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=375,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.salir,text="Salir",font="Verdana",font_size=30,font_color=C_WHITE)
        
        self.lista_widget = [self.btn_clasificacion, self.btn_configuracion, self.btn_ayuda, self.btn_salir]

        if LEVEL_DEBUG:
            self.btn_nivel_1 = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=75,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.cargar_nivel,on_click_param="Nivel1",text="Comenzar Juego",font="Verdana",font_size=30,font_color=C_WHITE)
            self.lista_widget.append(self.btn_nivel_1)
            self.btn_nivel_2 = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=225,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.cargar_nivel,on_click_param="Nivel2",text="Nivel 2",font="Verdana",font_size=30,font_color=C_WHITE)
            self.lista_widget.append(self.btn_nivel_2)
            self.btn_nivel_3 = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=300,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.cargar_nivel,on_click_param="Nivel3",text="Nivel 3",font="Verdana",font_size=30,font_color=C_WHITE)
            self.lista_widget.append(self.btn_nivel_3)
        else:
            self.btn_comenzar = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=75,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.cargar_nivel,on_click_param="Nivel1",text="Comenzar Juego",font="Verdana",font_size=30,font_color=C_WHITE)
            self.lista_widget.append(self.btn_comenzar)

    def update(self, lista_eventos, keys_pressed=None, delta_ms=None):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()

    def cargar_nivel(self, parametro):
        self.set_active(parametro)

    def mostrar_clasificacion(self, parametro):
        pass

    def mostrar_configuracion(self, parametro):
        self.set_active("MenuConfiguracion")

    def mostrar_ayuda(self, parametro):
        pass

    def salir(self, parametro):
        pygame.quit()
        sys.exit()
        