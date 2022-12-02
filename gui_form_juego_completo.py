import pygame
import sys
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_item_label import Label
from gui_item_button import Button
from gui_item_progressbar import ProgressBar


class FormJuegoCompleto(Form):
    def __init__(self,config,master_surface,
                    f_get_value_chk_sounds,
                    f_get_value_chk_music,
                    f_get_value_volume_sounds,
                    f_get_value_volume_music,
                    f_get_game_min_top_item,
                    f_game_draw_bg,
                    active=False):

        for item in config:
            setattr(self, item, config[item])

        self.f_get_game_min_top_item = f_get_game_min_top_item

        x=ANCHO_VENTANA/2 - self.width/2
        y=ALTO_VENTANA/2 - self.heigth/2

        super().__init__(name=self.name,master_surface=master_surface,x=x,y=y,w=self.width,h=self.heigth,
                        f_get_value_chk_sounds=f_get_value_chk_sounds,
                        f_get_value_chk_music=f_get_value_chk_music,
                        f_get_value_volume_sounds=f_get_value_volume_sounds,
                        f_get_value_volume_music=f_get_value_volume_music,
                        f_game_draw_bg=f_game_draw_bg,
                        background_color = None,
                        color_border = None,
                        background_image_path=self.background_image_path, 
                        active=active, 
                        background_sound_path=self.background_sound_path)

        ANCHO_BOTON = self.boton_ancho
        ALTO_BOTON = self.boton_alto
        ANCHO_FORM = self.width
        ALTO_FORM = self.heigth
        ANCHO_LABEL = 300
        ALTO_LABEL = 50

        self.btn_continuar = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=ALTO_FORM-100-ALTO_BOTON,w=69,h=68,color_background=None,color_border=None,image_background="images/menu/icons/ok.png",on_click=self.cargar_siguiente_nivel)
        self.puntaje = Label(master_form=self, x=ANCHO_FORM/2-ANCHO_LABEL/2, y=100, w=ANCHO_LABEL, h=ALTO_LABEL, color_background=C_WHITE, text="Puntaje: ", font= "Arial", font_size=25, font_color=C_BLACK)
        self.vidas_restantes = Label(master_form=self, x=ANCHO_FORM/2-ANCHO_LABEL/2, y=175, w=ANCHO_LABEL, h=ALTO_LABEL, color_background=C_WHITE, text="Vidas restantes: ", font= "Arial", font_size=25, font_color=C_BLACK)
        self.tiempo_restante = Label(master_form=self, x=ANCHO_FORM/2-ANCHO_LABEL/2, y=250, w=ANCHO_LABEL, h=ALTO_LABEL, color_background=C_WHITE, text="Tiempo restante: ", font= "Arial", font_size=25, font_color=C_BLACK)
        
        self.lista_widget = [self.btn_continuar, self.puntaje, self.vidas_restantes, self.tiempo_restante]

    def activate_form(self):
        super().activate_form()
        min_top_item = self.f_get_game_min_top_item()
        if self.form_data["nivel_puntuacion"] == min_top_item["puntaje"] and self.form_data["total_tiempo_restante"] > min_top_item["tiempo_restante"]:
            #Puntuación igual, mejor tiempo
            pass
        elif self.form_data["nivel_puntuacion"] > min_top_item["puntaje"]:
            #Mejor puntuación que el ultimo del top
            pass
        else:
            #No entra en el top, indicar en el form
            pass

    def update(self, lista_eventos, keys_pressed=None, delta_ms=None):

        self.puntaje.set_text("Puntuación: {0}".format(self.form_data["nivel_puntuacion"]))
        self.vidas_restantes.set_text("Vidas restantes: {0}".format(self.form_data["vidas_restantes"]))
        self.tiempo_restante.set_text("Tiempo restante: {0}".format(self.form_data["total_tiempo_restante"]))

        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)


    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget: 
            aux_widget.draw()

    def cargar_siguiente_nivel(self, parametro):
        self.set_active(self.form_data["last_form"])
