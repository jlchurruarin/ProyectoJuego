import pygame
import sys
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_item_button import Button
from gui_item_checkbutton import CheckButton


class FormMenuPrincipal(Form):
    def __init__(self,config,master_surface,
                    f_game_draw_bg,
                    f_game_set_player_id,
                    active=False):

        for item in config:
            setattr(self, item, config[item])

        x=ANCHO_VENTANA/2 - self.width/2
        y=ALTO_VENTANA/2 - self.heigth/2

        super().__init__(name=self.name,master_surface=master_surface,x=x,y=y,w=self.width,h=self.heigth,
                        f_game_draw_bg=f_game_draw_bg,
                        background_color = None,
                        color_border = None,
                        background_image_path=self.background_image_path, 
                        active=active, 
                        background_sound_path=self.background_sound_path)


        self.ninjagirl_value = True
        self.cowgirl_value = False
        ANCHO_BOTON = self.botones_ancho
        ALTO_BOTON = self.botones_alto
        ANCHO_FORM = self.width
        ALTO_FORM = self.heigth

        self.btn_continuar = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=75,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/menu/button/Button_M_02.png",on_click=self.continuar_nivel,on_click_param="",text="Continuar",font="Verdana",font_size=30,font_color=C_WHITE)
        self.btn_clasificacion = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=150,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/menu/button/Button_M_02.png",on_click=self.mostrar_clasificacion,text="Clasificación",font="Verdana",font_size=30,font_color=C_WHITE)

        self.ckh_ninjagirl = CheckButton(master=self, x=ANCHO_FORM/2-20-75, y=220,w=75, h=75, f_chk_value=self.ninjagirl_is_on, image_on_path="images/menu/icons/ninjagirl.png", image_off_path="images/menu/icons/ninjagirl-byn.png", color_background=None,color_border=None, on_click=self.personaje_click)
        self.ckh_cowgirl = CheckButton(master=self, x=ANCHO_FORM/2+20, y=220,w=75, h= 75, f_chk_value=self.cowgirl_is_on, image_on_path="images/menu/icons/cowgirl.png", image_off_path="images/menu/icons/cowgirl-byn.png", color_background=None,color_border=None, on_click=self.personaje_click)

        self.btn_configuracion = Button(master=self,x=ANCHO_FORM/2-75-40,y=ALTO_FORM-100-ALTO_BOTON,w=69,h=68,color_background=None,color_border=None,image_background="images/menu/icons/settings.png",on_click=self.mostrar_configuracion)
        self.btn_ayuda = Button(master=self,x=ANCHO_FORM/2+40,y=ALTO_FORM-100-ALTO_BOTON,w=69,h=68,color_background=None,color_border=None,image_background="images/menu/icons/help.png",on_click=self.mostrar_ayuda)

        #self.btn_nivel_2 = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=225,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/menu/button/Button_M_02.png",on_click=self.cargar_nivel,on_click_param="Nivel2",text="Nivel 2",font="Verdana",font_size=30,font_color=C_WHITE)
        #self.btn_nivel_3 = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=300,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/menu/button/Button_M_02.png",on_click=self.cargar_nivel,on_click_param="Nivel3",text="Nivel 2",font="Verdana",font_size=30,font_color=C_WHITE)

        self.btn_salir = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=375,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/menu/button/Button_M_02.png",on_click=self.salir,text="Salir",font="Verdana",font_size=30,font_color=C_WHITE)
        
        self.lista_widget_menu = [self.btn_clasificacion, self.btn_configuracion, self.btn_ayuda, self.btn_salir, self.ckh_ninjagirl, self.ckh_cowgirl]
        self.lista_widget_pausa = [self.btn_clasificacion, self.btn_configuracion, self.btn_ayuda, self.btn_salir, self.btn_continuar]

        if LEVEL_DEBUG:
            self.btn_nivel_1 = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=75,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/menu/button/Button_M_02.png",on_click=self.cargar_nivel,on_click_param="Nivel1",text="Nivel 1",font="Verdana",font_size=30,font_color=C_WHITE)
            self.lista_widget_menu.append(self.btn_nivel_1)
            self.btn_nivel_2 = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=225,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/menu/button/Button_M_02.png",on_click=self.cargar_nivel,on_click_param="Nivel2",text="Nivel 2",font="Verdana",font_size=30,font_color=C_WHITE)
            self.lista_widget_menu.append(self.btn_nivel_2)
            self.btn_nivel_3 = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=300,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/menu/button/Button_M_02.png",on_click=self.cargar_nivel,on_click_param="Nivel3",text="Nivel 3",font="Verdana",font_size=30,font_color=C_WHITE)
            self.lista_widget_menu.append(self.btn_nivel_3)
        else:
            self.btn_comenzar = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=75,w=ANCHO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,image_background="images/menu/button/Button_M_02.png",on_click=self.cargar_nivel,on_click_param="Nivel1",text="Comenzar Juego",font="Verdana",font_size=30,font_color=C_WHITE)
            self.lista_widget_menu.append(self.btn_comenzar)

        self.f_game_set_player_id = f_game_set_player_id
        

    def update(self, lista_eventos, keys_pressed=None, delta_ms=None):
        if not self.form_data["pause"]:
            for aux_widget in self.lista_widget_menu:    
                aux_widget.update(lista_eventos)
        else:
            for aux_widget in self.lista_widget_pausa:    
                aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        if not self.form_data["pause"]:
            for aux_widget in self.lista_widget_menu:    
                aux_widget.draw()
        else:
            for aux_widget in self.lista_widget_pausa:    
                aux_widget.draw()

    def cargar_nivel(self, parametro):
        if parametro == "Nivel1":
            self.form_data["nivel_puntuacion"] = 0
            #self.form_data["vidas_restantes"]
            self.form_data["total_tiempo_restante"] = 0
        self.cargar_player_id()
        self.set_active(parametro)
            
    def cargar_player_id(self):
        if self.ninjagirl_value and not self.form_data["pause"]:
            self.f_game_set_player_id("ninjagirl")
        elif self.cowgirl_value and not self.form_data["pause"]:
            self.f_game_set_player_id("cowgirl")

    def continuar_nivel(self, parametro):
        self.set_active(self.form_data["last_form"])

    def mostrar_clasificacion(self, parametro):
        self.cargar_player_id()
        self.set_active("MenuHighscore")

    def mostrar_configuracion(self, parametro):
        self.cargar_player_id()
        self.set_active("MenuConfiguracion")

    def mostrar_ayuda(self, parametro):
        self.cargar_player_id()
        self.set_active("MenuAyuda")

    def salir(self, parametro):
        pygame.quit()
        sys.exit()
        
    def ninjagirl_is_on(self):
        return self.ninjagirl_value

    def cowgirl_is_on(self):
        return self.cowgirl_value

    def personaje_click(self):
        self.ninjagirl_value = not self.ninjagirl_value
        self.cowgirl_value = not self.cowgirl_value