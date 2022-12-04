from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_item_label import Label
from gui_item_button import Button


class FormMenuAyuda(Form):
    def __init__(self,config,master_surface,
                    f_game_draw_bg,
                    active=False):

        ####
        #self.form_data["last_form"] = "JuegoCompleto"
        #self.form_data["nivel_puntuacion"] = 0
        #self.form_data["total_tiempo_restante"] = 0
        #self.form_data["vidas_restantes"] = 5
        ####


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

        ANCHO_BOTON = self.boton_ancho
        ALTO_BOTON = self.boton_alto
        ANCHO_FORM = self.width
        ALTO_FORM = self.heigth
        ANCHO_LABEL = 350
        ALTO_LABEL = 50


        self.titulo = Label(master_form=self, x=ANCHO_FORM/2-ANCHO_LABEL/2, y=30, w=ANCHO_LABEL, h=ALTO_LABEL, text="Menu de ayuda", font= "Arial", font_size=40, font_color=C_TEXT)
        self.subtitulo = Label(master_form=self, x=ANCHO_FORM/2-ANCHO_LABEL/2, y=100, w=ANCHO_LABEL, h=ALTO_LABEL, text="", font= "Arial", font_size=24, font_color=C_TEXT)

        self.mensaje = Label(master_form=self, x=ANCHO_FORM/2-ANCHO_LABEL/2, y=225, w=ANCHO_LABEL, h=25, text="Ingresa tu nombre y preciona el boton verde", font= "Arial", font_size=18, font_color=C_TEXT)
        self.mensaje2 = Label(master_form=self, x=ANCHO_FORM/2-ANCHO_LABEL/2, y=250, w=ANCHO_LABEL, h=25, text="para registrate en el hall de la fama", font= "Arial", font_size=18, font_color=C_TEXT)

        self.btn_continuar = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=ALTO_FORM-20-ALTO_BOTON,w=69,h=68,color_background=None,color_border=None,image_background="images/menu/icons/ok.png",on_click=self.cargar_menu_principal)
        
        self.lista_widget = [self.titulo, self.subtitulo, self.btn_continuar]

    def activate_form(self):
        super().activate_form()
        self.f_game_draw_bg()

    def update(self, lista_eventos, keys_pressed=None, delta_ms=None):

        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos, delta_ms)


    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget: 
            aux_widget.draw()

    def cargar_menu_principal(self, parametro):
        self.set_active(self.form_data["MenuPrincipal"])

        