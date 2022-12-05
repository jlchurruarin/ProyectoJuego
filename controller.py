
class Controller():

    controllers = {}
    
    def __init__(self, lista):
        self.lista = lista


    def update_list(self, delta_ms=None):
        self.lista = list(filter(lambda item: (item.muerto == False), self.lista))

    def get_list(self):
        return self.lista


    def update_items(self, delta_ms):
        for item in self.get_list():
            item.update(delta_ms=delta_ms)


    def draw_items(self):
        for item in self.get_list():
            item.draw()