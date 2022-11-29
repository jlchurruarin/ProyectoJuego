from gui_item_widget import Widget

class Cronometro(Widget):
    
    def __init__(self, master_form, config, segundos):
        
        for item in config:
            setattr(self, item, config[item])

        super().__init__(master_form=master_form, x=self.pos_x, y=self.pos_y, w=self.width, h=self.heigth, image_background=self.image, text=self.text, font=self.font, font_size=self.font_size, font_color=self.font_color, text_offset_x=self.text_offset_x, text_offset_y=self.text_offset_y)

        self.tiempo_ms = segundos * 1000
        self.tiempo_transcurrido_actualizacion = 0
        self.timeout = False
        self.render()
        

    def update(self, delta_ms):
        self.tiempo_transcurrido_actualizacion += delta_ms
        if self.tiempo_transcurrido_actualizacion > 100 and not self.timeout:
            self.tiempo_ms -= self.tiempo_transcurrido_actualizacion

            if self.tiempo_ms < 0:
                self.tiempo_ms = 0
                self.timeout = True

            self.tiempo_transcurrido_actualizacion = 0
            minutos = int(self.tiempo_ms/ 1000 / 60)
            segundos = int(self.tiempo_ms/ 1000)
            minutos_str = str(minutos).zfill(2)
            segundos_str = str(segundos - minutos*60).zfill(2)
            self._text = "{0}:{1}".format(minutos_str, segundos_str)
            self.render()

