from gui_item_widget import Widget

class Vida(Widget):

    lista_vidas = []

    def __init__(self, master_form, value, config, player_lives):


        for item in config:
            setattr(self, item, config[item])

        x = self.pos_x + (self.width + 5) * value
        y = self.pos_y

        super().__init__(master_form=master_form, x=x, y=y, w=self.width, h=self.heigth, image_background=self.image)

        self.player_get_lives = player_lives
        self.value = value

        self.render()
        

    def update(self, delta_ms=None):
        
        self.render()

    def draw(self):
        player_lives = self.player_get_lives()
        if self.value <= player_lives:
            super().draw()
