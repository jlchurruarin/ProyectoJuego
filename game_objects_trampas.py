from game_object_trampa import Trampa

class Trampas(Trampa):

    lista_trampas = []

    def __init__(self, master_form, x, y, config):

        for item in config:
            setattr(self, item, config[item])

        super().__init__(master_form, x, y, self.width, self.heigth, 
                            self.animations_dict["idle"], self.frame_rate_ms, self.move_rate_ms )

        self.lista_trampas.append(self)
