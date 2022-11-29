from gui_item_widget import Widget

class Puntuación(Widget):
    
    def __init__(self, master_form, config,  f_get_points):

        for item in config:
            setattr(self, item, config[item])
        
        super().__init__(master_form=master_form, x=self.pos_x, y=self.pos_y, w=self.width, h=self.heigth, 
                            image_background=self.image, text=self.text, font=self.font, font_size=self.font_size, font_color=self.font_color, 
                            text_offset_x=self.text_offset_x, text_offset_y=self.text_offset_y)

        self.f_get_points = f_get_points
        self.render()
        

    def update(self, delta_ms=None):
        self._text = "{0}".format(self.f_get_points()).zfill(7)
        self.render()

