from controller import Controller
from constantes import *

class EnemyController(Controller):

    def __init__(self, lista_enemigos, lista_plataformas):
        super().__init__(lista_enemigos)
        self.tiempo_ultima_colision = 0

        self.controllers["enemy"] = self
        
    def verificar_colisiones(self, lista_balas, player):
        pass

    def update_list(self, delta_ms):
        pass
        
    def generar_enemigo(self, enemigo):
        pass

    def verificar_triggers(self, f_player_get_coords):
        coords = f_player_get_coords()
        for enemy in self.get_list():
            
            if not enemy.muerto:
                min_range_x = enemy.x - enemy.trigger_range
                max_range_x = enemy.x + enemy.trigger_range
                min_range_y = enemy.y - enemy.trigger_range
                max_range_y = enemy.y + enemy.trigger_range

                if (min_range_x < coords[0] and max_range_x > coords[0] and
                    min_range_y < coords[1] and max_range_y > coords[1]):
                    
                    enemy.trigger()
                

                