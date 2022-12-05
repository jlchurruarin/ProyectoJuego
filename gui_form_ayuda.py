from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_item_label import Label
from gui_item_button import Button
from gui_item_imagen import Imagen


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


        self.titulo = Label(master_form=self, x=0, y=30, w=self.w, h=ALTO_LABEL, text="Menu de ayuda", font= "Arial", font_size=40, font_color=C_TEXT)
        self.subtitulo = Label(master_form=self, x=0, y=100, w=self.w, h=ALTO_LABEL, text="", font= "Arial", font_size=24, font_color=C_TEXT)

        self.btn_historia = Button(master=self,x=50,y=self.alto_titulo+20,w=self.sidebar_width,h=self.boton_alto,color_background=None,color_border=None,image_background="images/menu/button/Button_M_02.png",on_click=self.mostrar_historia,text="Historia",font="Verdana",font_size=30,font_color=C_WHITE)
        self.btn_personajes = Button(master=self,x=50,y=self.alto_titulo+40+self.boton_alto,w=self.sidebar_width,h=self.boton_alto,color_background=None,color_border=None,image_background="images/menu/button/Button_M_02.png",on_click=self.mostrar_personajes,text="Personajes",font="Verdana",font_size=30,font_color=C_WHITE)
        self.btn_enemigos = Button(master=self,x=50,y=self.alto_titulo+60+self.boton_alto*2,w=self.sidebar_width,h=self.boton_alto,color_background=None,color_border=None,image_background="images/menu/button/Button_M_02.png",on_click=self.mostrar_enemigos,text="Enemigos",font="Verdana",font_size=30,font_color=C_WHITE)
        
        #self.descripción = Label(master_form=self, x=self.width/2-self.label_ancho*2, y=100+(50*pos), w=self.label_ancho, h=self.label_alto, text="{}".format(pos+1), font="Arial", font_size=20, font_color=C_BLACK, image_background=self.label_bg)

        self.players = []
        for linea, texto in enumerate(self.rose.split("\n")):
            label = Label(master_form=self, x=310, y=150+70+(50*linea), w=(ANCHO_FORM-300)/2-100, h=50, text=texto, font="Arial", font_size=20, font_color=C_BLACK, image_background=self.label_bg)
            self.players.append(label)
        for linea, texto in enumerate(self.katie.split("\n")):
            label = Label(master_form=self, x=310+(ANCHO_FORM-300)/2, y=150+70+(50*linea), w=(ANCHO_FORM-300)/2-100, h=50, text=texto, font="Arial", font_size=20, font_color=C_BLACK, image_background=self.label_bg)
            self.players.append(label)
        
        imagen = Imagen(master_form=self, x=450, y=150+20, w=50, h=50, image_background="images/menu/icons/cowgirl.png")
        self.players.append(imagen)
        imagen = Imagen(master_form=self, x=900, y=150+20, w=50, h=50, image_background="images/menu/icons/ninjagirl.png")
        self.players.append(imagen)


        self.enemigos = []
        for linea, texto in enumerate(self.cactus.split("\n")):
            label = Label(master_form=self, x=310, y=150+70+(50*linea), w=(ANCHO_FORM-300)/2-100, h=50, text=texto, font="Arial", font_size=20, font_color=C_BLACK, image_background=self.label_bg)
            self.enemigos.append(label)
        for linea, texto in enumerate(self.dust.split("\n")):
            label = Label(master_form=self, x=310+(ANCHO_FORM-300)/2, y=150+70+(50*linea), w=(ANCHO_FORM-300)/2-100, h=50, text=texto, font="Arial", font_size=20, font_color=C_BLACK, image_background=self.label_bg)
            self.enemigos.append(label)
        
        imagen = Imagen(master_form=self, x=450, y=150+20, w=50, h=50, image_background="images/menu/icons/cactus.png")
        self.enemigos.append(imagen)
        imagen = Imagen(master_form=self, x=900, y=150+20, w=50, h=50, image_background="images/menu/icons/dust.png")
        self.enemigos.append(imagen)

        self.historia_labels = []
        for linea, texto in enumerate(self.historia.split("\n")):
            label = Label(master_form=self, x=310, y=150+70+(50*linea), w=ANCHO_FORM-400, h=50, text=texto, font="Arial", font_size=20, font_color=C_BLACK, image_background=self.label_bg)
            self.historia_labels.append(label)


        self.btn_continuar = Button(master=self,x=ANCHO_FORM/2-ANCHO_BOTON/2,y=ALTO_FORM-20-ALTO_BOTON,w=69,h=68,color_background=None,color_border=None,image_background="images/menu/icons/ok.png",on_click=self.cargar_menu_principal)
        self.lista_widget = [self.titulo, self.subtitulo, self.btn_historia, self.btn_personajes, self.btn_enemigos, self.btn_continuar]
        self.lista_widget_original = [self.titulo, self.subtitulo, self.btn_historia, self.btn_personajes, self.btn_enemigos, self.btn_continuar]

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
        self.set_active("MenuPrincipal")

    def mostrar_personajes(self, parametro):
        self.lista_widget = self.lista_widget_original.copy()
        for label in self.players:
            self.lista_widget.append(label)
        self.render()
        
    def mostrar_historia(self, parametro):
        self.lista_widget = self.lista_widget_original.copy()
        for label in self.historia_labels:
            self.lista_widget.append(label)
        self.render()
    def mostrar_enemigos(self, parametro):
        self.lista_widget = self.lista_widget_original.copy()
        for label in self.enemigos:
            self.lista_widget.append(label)
        self.render()