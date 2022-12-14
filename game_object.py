from gui_item_widget import Widget
from constantes import *
import pygame

class GameObject(Widget):
    
    def __init__(self, master_form, x, y, w, h, frame_rate_ms=0, move_rate_ms=0, image_background=None):
        super().__init__(master_form, x, y, w, h)
        self.animations = []
        self.sounds = []
        self.tiempo_transcurrido_animation = 0
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_muerto = 0
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        
        if getattr(self, "lives", 0) == 0:
            self.lives = 0

        if image_background != None:
            self.image_background = pygame.image.load("{0}{1}".format(GAME_PATH, image_background))
            self.image_background = pygame.transform.scale(self.image_background,(w, h)).convert_alpha()
        else:
            self.image_background = None

        self.rects = []

    @property
    def animation(self):
        return self._animation

    @animation.setter
    def animation(self, new_animation):
        '''
        Setter de animation el cual vuelve a 0 el frame cuando la animación cambia
        '''
        for item_animation in self.animations:
            item_animation.reset_frame()
        self._animation = new_animation

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            self.image_background = self.animation.next_frame()
        self.render()

    def add_x(self,delta_x)->None:
        '''
        Método que mueve el objeto sobre el eje x

        Recibe la cantidad de pixeles que se debe mover el objeto (admite positivos -> y negativos <-)
        '''
        self.x += delta_x

    def add_y(self,delta_y)->None:
        '''
        Método que mueve el objeto sobre el eje y

        Recibe la cantidad de pixeles que se debe mover el objeto (admite positivos para mover hacia abajo y negativos para mover hacia arriba)
        '''
        self.last_y = self.y
        self.y += delta_y

    def render(self)->None:
        '''
        Método que realiza el render del objeto
        '''

        self.slave_surface = pygame.Surface((self.w,self.h), pygame.SRCALPHA)
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = self.x
        self.slave_rect.y = self.y
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self.master_form.x
        self.slave_rect_collide.y += self.master_form.y
        
        if self.image_background:
            self.slave_surface.blit(self.image_background,(0,0))
            
        if self.color_border:
            pygame.draw.rect(self.slave_surface, self.color_border, self.slave_surface.get_rect(), 2)

    def draw(self)-> None:
        '''
        Método que dibuja en pantalla el objeto y sus rects en el caso que DEBUG este activo
        '''
        super().draw()
        if DEBUG:
            for numero,rect in enumerate(self.rects):
                pygame.draw.rect(self.master_form.surface,C_RECTS[numero],rect)
    
    def hit(self)-> None:
        '''
        Método que es llamada al golpear el objeto, le resta vidas y cambia de estado a muerto en el caso que las vidas sean 0
        '''
        if not self.muerto:
            self.lives -= 1
            if self.lives <= 0:
                self.muerto = True
                self.tiempo_transcurrido_muerto = 0

    def actualizar_volumen(self, music_onoff, sounds_onoff, volumen_music, volumen_sounds)-> None:
        '''
        Método que actualzia el volumen de los sonidos del objeto
        '''
        if not sounds_onoff:
            volumen_sounds = 0

        for sound in self.sounds:
            self.sounds[sound].set_volume(volumen_sounds)


    def update(self, delta_ms=None)-> None:
        '''
        Método que realiza el update del objeto
        '''
        self.render()