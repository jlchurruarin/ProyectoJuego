from game_object_trampa import Trampa

class Trampas(Trampa):

    lista_trampas = []

    def __init__(self, master_form, x, y, config):

        '''
        Clase que representa a las trampas del juego

        Recibe por parametro el formulario padre, la posición x, la posición y y la configuración de la trampa (desde game_config.json)
        '''

        for item in config:
            setattr(self, item, config[item])

        super().__init__(master_form, x, y, self.width, self.heigth, 
                            self.animations_dict["idle"], self.frame_rate_ms, self.move_rate_ms )

        self.lista_trampas.append(self)
