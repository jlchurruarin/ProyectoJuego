from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_item_label import Label
from gui_item_button import Button
from gui_item_textbox import TextBox


class FormJuegoCompleto(Form):
    def __init__(self,config,master_surface,
                    f_get_game_min_top_item,
                    f_game_draw_bg,
                    f_game_add_ranking,
                    active=False):

        ####
        #self.form_data["last_form"] = "JuegoCompleto"
        #self.form_data["nivel_puntuacion"] = 0
        #self.form_data["total_tiempo_restante"] = 0
        #self.form_data["vidas_restantes"] = 5
        ####


        for item in config:
            setattr(self, item, config[item])

        self.f_get_game_min_top_item = f_get_game_min_top_item
        self.f_game_add_ranking = f_game_add_ranking

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


        self.titulo = Label(master_form=self, x=ANCHO_FORM/2-ANCHO_LABEL/2, y=30, w=ANCHO_LABEL, h=ALTO_LABEL, text="", font= "Arial", font_size=40, font_color=C_TEXT)
        self.subtitulo = Label(master_form=self, x=ANCHO_FORM/2-ANCHO_LABEL/2, y=100, w=ANCHO_LABEL, h=ALTO_LABEL, text="", font= "Arial", font_size=24, font_color=C_TEXT)

        self.mensaje = Label(master_form=self, x=ANCHO_FORM/2-ANCHO_LABEL/2, y=225, w=ANCHO_LABEL, h=25, text="Ingresa tu nombre y preciona el boton verde", font= "Arial", font_size=18, font_color=C_TEXT)
        self.mensaje2 = Label(master_form=self, x=ANCHO_FORM/2-ANCHO_LABEL/2, y=250, w=ANCHO_LABEL, h=25, text="para registrate en el hall de la fama", font= "Arial", font_size=18, font_color=C_TEXT)
        self.error_msg = Label(master_form=self, x=ANCHO_FORM/2-ANCHO_LABEL/2, y=400, w=ANCHO_LABEL, h=25, text="Debes ingresar un nombre", color_background=(99,99,99),  font= "Arial", font_size=18, font_color=C_RED)
        self.btn_cargar_record = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=ALTO_FORM-20-ALTO_BOTON,w=69,h=68,color_background=None,color_border=None,image_background="images/menu/icons/ok.png",on_click=self.cargar_record)

        self.btn_continuar = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=ALTO_FORM-20-ALTO_BOTON,w=69,h=68,color_background=None,color_border=None,image_background="images/menu/icons/ok.png",on_click=self.cargar_siguiente_nivel)
        self.puntaje = Label(master_form=self, x=ANCHO_FORM/2-ANCHO_LABEL/2, y=225, w=ANCHO_LABEL, h=ALTO_LABEL, color_background=C_WHITE, text="Puntaje: ", font= "Arial", font_size=25, font_color=C_BLACK)
        self.vidas_restantes = Label(master_form=self, x=ANCHO_FORM/2-ANCHO_LABEL/2, y=300, w=ANCHO_LABEL, h=ALTO_LABEL, color_background=C_WHITE, text="Vidas restantes: ", font= "Arial", font_size=25, font_color=C_BLACK)
        self.tiempo_restante = Label(master_form=self, x=ANCHO_FORM/2-ANCHO_LABEL/2, y=375, w=ANCHO_LABEL, h=ALTO_LABEL, color_background=C_WHITE, text="Tiempo restante: ", font= "Arial", font_size=25, font_color=C_BLACK)


        self.text_name = TextBox(master=self, x=ANCHO_FORM/2-ANCHO_LABEL/2, y=300, w=ANCHO_LABEL, h=ALTO_LABEL, color_background=C_WHITE, color_border=C_BLACK)
        
        self.lista_widget_nuevo_record = [self.titulo, self.subtitulo, self.text_name, self.mensaje, self.mensaje2, self.btn_cargar_record]
        self.lista_widget_fin_partida = [self.titulo, self.subtitulo, self.btn_continuar, self.puntaje, self.vidas_restantes, self.tiempo_restante]

    def activate_form(self):
        super().activate_form()
        self.f_game_draw_bg()
        self.text_name.texto = ""
        min_top_item = self.f_get_game_min_top_item()
        if self.form_data["nivel_puntuacion"] == min_top_item["puntaje"] and self.form_data["total_tiempo_restante"] > min_top_item["tiempo_restante"]:
            self.titulo.set_text("Partida finalizada")
            self.subtitulo.set_text("Nuevo record!")
            self.lista_widget = self.lista_widget_nuevo_record                

        elif self.form_data["nivel_puntuacion"] > min_top_item["puntaje"]:
            self.titulo.set_text("Partida finalizada")
            self.subtitulo.set_text("Nuevo record!")
            self.lista_widget = self.lista_widget_nuevo_record
            #Mejor puntuación que el ultimo del top

        else:
            self.titulo.set_text("Partida finalizada")
            self.subtitulo.set_text("Resumen de la partida:")
            self.lista_widget = self.lista_widget_fin_partida
            #No entra en el top, indicar en el form


    def update(self, lista_eventos, keys_pressed=None, delta_ms=None):

        self.puntaje.set_text("Puntuación: {0}".format(self.form_data["nivel_puntuacion"]))
        self.vidas_restantes.set_text("Vidas restantes: {0}".format(self.form_data["vidas_restantes"]))
        self.tiempo_restante.set_text("Tiempo restante: {0}".format(self.form_data["total_tiempo_restante"]))

        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos, delta_ms)


    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget: 
            aux_widget.draw()

    def cargar_siguiente_nivel(self, parametro):
        self.set_active(self.form_data["last_form"])

    def cargar_record(self, param):
        if len(self.text_name.texto) == 0:
            if self.error_msg not in self.lista_widget:
                self.lista_widget.append(self.error_msg)
        else:
            self.f_game_add_ranking(nombre=self.text_name.texto, puntaje=self.form_data["nivel_puntuacion"], tiempo_restante=self.form_data["total_tiempo_restante"])
            self.form_data["last_form"] = "MenuPrincipal"
            self.set_active("MenuHighscore")
        