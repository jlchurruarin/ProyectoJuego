from controller import Controller
from constantes import *

class BalasController(Controller):

    def __init__(self, f_remove_widwet):
        super().__init__(lista=[])

        self.controllers["balas"] = self
        self.f_remove_widwet = f_remove_widwet
        
    def get_my_bullets_quantity(self, owner):
        return len(list(filter(lambda item: item.owner == owner, self.lista )))

    def add_bullet(self, bala):
        self.lista.append(bala)

    def update_items(self, delta_ms):
        for item in self.lista:
            if item.x + item.w < 0 or item.x > ANCHO_VENTANA or item.y + item.w < 0 or item.y > ALTO_VENTANA:
                item.muerto = True

            if item.muerto == True:
                self.lista.remove(item)
                self.f_remove_widwet(item)
        super().update_items(delta_ms=delta_ms)

    def update_list(self, delta_ms=None):
        death_items = list(filter(lambda item: (item.muerto == True), self.lista))

        for item in death_items:
            self.f_remove_widwet(item)

        super().update_list(delta_ms)