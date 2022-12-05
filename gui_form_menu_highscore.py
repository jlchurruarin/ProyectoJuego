from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_item_label import Label
from gui_item_button import Button
from gui_item_textbox import TextBox

class FormMenuHighscore(Form):
    def __init__(self,config,master_surface,
                    f_game_draw_bg,
                    f_game_get_ranking,
                    active=False):

        for item in config:
            setattr(self, item, config[item])

        self.f_game_get_ranking = f_game_get_ranking

        x=ANCHO_VENTANA/2 - self.width/2
        y=ALTO_VENTANA/2 - self.heigth/2

        super().__init__(name=self.name,master_surface=master_surface,x=x,y=y,w=self.width,h=self.heigth,
                        f_game_draw_bg=f_game_draw_bg,
                        background_color = None,
                        color_border = None,
                        background_image_path=self.background_image_path, 
                        active=active, 
                        background_sound_path=self.background_sound_path)

        self.titulo_posicion = Label(master_form=self, x=self.width/2-self.label_ancho*2, y=50, w=self.label_ancho, h=self.label_alto, text="Posición", 
                                        font="Arial", font_size=20, font_color=C_BLACK, image_background=self.label_bg)

        self.titulo_nombre = Label(master_form=self, x=self.width/2-self.label_ancho*1, y=50, w=self.label_ancho, h=self.label_alto, text="Nombre", 
                                        font="Arial", font_size=20, font_color=C_BLACK, image_background=self.label_bg)

        self.titulo_puntaje = Label(master_form=self, x=self.width/2, y=50, w=self.label_ancho, h=self.label_alto, text="Puntaje", 
                                        font="Arial", font_size=20, font_color=C_BLACK, image_background=self.label_bg)

        self.titulo_tiempo = Label(master_form=self, x=self.width/2+self.label_ancho, y=50, w=self.label_ancho, h=self.label_alto, text="Tiempo restante", 
                                        font="Arial", font_size=20, font_color=C_BLACK, image_background=self.label_bg)

        self.btn_ok = Button(master=self,x=self.width/2-self.boton_ancho/2,y=self.heigth-100-self.boton_alto,w=self.boton_ancho,h=self.boton_alto,
                                    color_background=None,color_border=None, image_background="images/menu/icons/ok.png",on_click=self.volver_atras)

        self.lista_widget = []
        
    def activate_form(self):
        self.lista_widget = []

        self.lista_widget = [self.titulo_posicion,
                            self.titulo_nombre,
                            self.titulo_puntaje,
                            self.titulo_tiempo,
                            self.btn_ok]

        for pos, item in enumerate(self.f_game_get_ranking()):
            self.titulo_posicion = Label(master_form=self, x=self.width/2-self.label_ancho*2, y=100+(50*pos), w=self.label_ancho, h=self.label_alto, text="{}".format(pos+1), font="Arial", font_size=20, font_color=C_BLACK, image_background=self.label_bg)
            self.titulo_nombre = Label(master_form=self, x=self.width/2-self.label_ancho*1, y=100+(50*pos), w=self.label_ancho, h=self.label_alto, text=item["nombre"], font="Arial", font_size=20, font_color=C_BLACK, image_background=self.label_bg)
            self.titulo_puntaje = Label(master_form=self, x=self.width/2, y=100+(50*pos), w=self.label_ancho, h=self.label_alto, text=str(item["puntaje"]), font="Arial", font_size=20, font_color=C_BLACK, image_background=self.label_bg)
            self.titulo_tiempo = Label(master_form=self, x=self.width/2+self.label_ancho, y=100+(50*pos), w=self.label_ancho, h=self.label_alto, text=str(item["tiempo_restante"]), font="Arial", font_size=20, font_color=C_BLACK, image_background=self.label_bg)

            self.lista_widget.append(self.titulo_posicion)
            self.lista_widget.append(self.titulo_nombre)
            self.lista_widget.append(self.titulo_puntaje)
            self.lista_widget.append(self.titulo_tiempo)
            
        return super().activate_form()

    def update(self, lista_eventos, keys_pressed=None, delta_ms=None):
        if self.tiempo_evita_doble_click >= 0:
            self.tiempo_evita_doble_click -= delta_ms
            lista_eventos = []

        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos, delta_ms)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()

    def cargar_nivel(self, parametro):
        self.set_active(parametro)

    def volver_atras(self, on_click_param):
        self.set_active("MenuPrincipal")