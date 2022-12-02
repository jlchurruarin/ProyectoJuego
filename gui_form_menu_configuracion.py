import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_item_imagen import Imagen
from gui_item_button import Button
from gui_item_textbox import TextBox
from gui_item_checkbutton import CheckButton
from gui_item_rangebar import RangeBar


class FormMenuConfiguracion(Form):
    def __init__(self,config, master_surface,
                    f_get_value_chk_sounds, f_get_value_chk_music, f_get_value_volume_sounds, f_get_value_volume_music,
                    f_set_volumen, f_game_draw_bg,
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
                        f_game_draw_bg=f_game_draw_bg,
                        background_color=None, color_border=None,
                        background_image_path=self.background_image_path, 
                        active=active, background_sound_path=self.background_sound_path)


        ANCHO_BOTON = self.botones_ancho
        ALTO_BOTON = self.botones_alto
        ANCHO_FORM = self.width
        ALTO_FORM = self.heigth
        ANCHO_SLIDER = self.slider_ancho
        ALTO_SLIDER = self.slider_alto

        self.f_get_value_chk_sounds = f_get_value_chk_sounds
        self.f_get_value_chk_music = f_get_value_chk_music
        self.f_get_value_volume_sounds = f_get_value_volume_sounds
        self.f_get_value_volume_music = f_get_value_volume_music
        self.f_set_volumen = f_set_volumen

        self.chk_music = CheckButton(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=75,w=ANCHO_BOTON,h=ALTO_BOTON, 
                                        f_chk_value=self.f_get_value_chk_music,
                                        image_on_path= "images/menu/checkbox/chk_on.png",
                                        image_off_path= "images/menu/checkbox/chk_off.png",
                                        color_background=None,color_border=None,
                                        on_click=self.chk_music_click,text="Musica",font="Verdana",font_size=30,font_color=C_WHITE)

        self.chk_sounds = CheckButton(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=150,w=ANCHO_BOTON,h=ALTO_BOTON, 
                                        f_chk_value=self.f_get_value_chk_sounds,
                                        image_on_path= "images/menu/checkbox/chk_on.png",
                                        image_off_path= "images/menu/checkbox/chk_off.png",
                                        color_background=None,color_border=None,
                                        on_click=self.chk_sounds_click,text="Sonidos",font="Verdana",font_size=30,font_color=C_WHITE)

        self.range_sounds = RangeBar(master=self, x=ANCHO_FORM/2-ANCHO_SLIDER/2, y=225, w=ANCHO_SLIDER, h=ALTO_SLIDER, 
                                        f_set_value=self.set_volume_sounds, 
                                        f_get_value=self.f_get_value_volume_sounds,
                                        image_background="images/menu/slider/background.png",
                                        image_dot="images/menu/slider/dot.png",
                                        image_progress="images/menu/slider/progress.png",
                                        value_min=1, value_max=100, text="Volumen de sonidos",font="Verdana",font_size=25,font_color=C_WHITE)

        self.range_music = RangeBar(master=self, x=ANCHO_FORM/2-ANCHO_SLIDER/2, y=300, w=ANCHO_SLIDER, h=ALTO_SLIDER, 
                                        f_set_value=self.set_volume_music, 
                                        f_get_value=self.f_get_value_volume_music,
                                        image_background="images/menu/slider/background.png",
                                        image_dot="images/menu/slider/dot.png",
                                        image_progress="images/menu/slider/progress.png",
                                        value_min=1, value_max=100, text="Volumen de música",font="Verdana",font_size=25,font_color=C_WHITE)

        self.btn_guardar = Button(master=self,x=ANCHO_FORM/2-ALTO_BOTON-20,y=ALTO_FORM-45-ALTO_BOTON,w=ALTO_BOTON,h=ALTO_BOTON,color_background=None,color_border=None,
                                    image_background="images/menu/icons/ok.png",on_click=self.guardar)

        self.btn_cancelar = Button(master=self,x=ANCHO_FORM/2+20,y=ALTO_FORM-45-ALTO_BOTON,w=ALTO_BOTON,h=ALTO_BOTON,color_background=None,
                                    color_border=None,image_background="images/menu/icons/cancel.png",on_click=self.cancelar)
        
        self.lista_widget = [
                            self.chk_sounds, 
                            self.chk_music, 
                            self.range_sounds, 
                            self.range_music, 
                            self.btn_guardar, 
                            self.btn_cancelar
                            ]


    def update(self, lista_eventos, keys_pressed=None, delta_ms=None):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()

    def cancelar(self, param=None):
        self.f_set_volumen(music_onoff=self.old_value_chk_music, 
                            sounds_onoff=self.old_value_chk_sounds, 
                            music_volume=self.old_value_volume_music, 
                            sounds_volume=self.old_value_volume_sounds)
        self.set_active("MenuPrincipal")

    def guardar(self, param=None):
        self.set_active("MenuPrincipal")

    def chk_sounds_click(self):
        sounds = self.f_get_value_chk_sounds()
        sounds = not sounds
        self.f_set_volumen(sounds_onoff=sounds)
        self.active = True

    def chk_music_click(self):
        music = self.f_get_value_chk_music()
        music = not music
        self.f_set_volumen(music_onoff=music)
        self.active = True

    def set_volume_sounds(self, value):
        self.f_set_volumen(sounds_volume=value/100)

    def set_volume_music(self, value):
        self.f_set_volumen(music_volume=value/100)