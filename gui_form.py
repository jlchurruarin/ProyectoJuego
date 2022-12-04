import pygame
from constantes import *
from pygame.locals import *
from gui_item_widget import Widget
from gui_item_button import Button

class Form():
    forms_dict = {}
    form_data = {}
    form_sounds = {}

    def __init__(self,name,master_surface,x,y,w,h,
                f_game_draw_bg,
                background_image_path, 
                background_color,color_border,active, background_sound_path=None):

        self.form_sounds["music_state"] = True
        self.form_sounds["effects_state"] = True
        self.form_sounds["music_volumen"] = 1.0
        self.form_sounds["effects_volumen"] = 1.0

        self.forms_dict[name] = self
        self.form_data["pause"] = False
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.color_background = background_color
        self.color_border = color_border
        self.background_sound = pygame.mixer.music
        self.background_sound_path = background_sound_path
        self.f_game_draw_bg=f_game_draw_bg
        self.surface = pygame.Surface((w,h), pygame.SRCALPHA, 32)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self._active = active
        self.x = x
        self.y = y

        if self._active and self.background_sound_path != None:
            self.background_sound.load("{0}{1}".format(GAME_PATH, self.background_sound_path))
            self.background_sound.set_volume(self.get_music_volumen())
            self.background_sound.play(-1)
            
        if(self.color_background != None):
            self.surface.fill(self.color_background)

        if(background_image_path != None):
            self.image_background = pygame.image.load("{0}{1}".format(GAME_PATH, background_image_path))
            self.image_background = pygame.transform.scale(self.image_background,(w, h)).convert_alpha()
        else:
            self.image_background = None

        self.tiempo_evita_doble_click = 0

        self.render()
    
    @property
    def active(self):
        return self._active
    
    @active.setter
    def active(self, active):
        if active and self.background_sound_path is not None:
            if self.get_music_state():
                self.background_sound.load("{0}{1}".format(GAME_PATH, self.background_sound_path))
                self.background_sound.set_volume(self.get_music_volumen())
                self.background_sound.play(-1)
            else:
                self.background_sound.stop()    
        else:
            self.background_sound.stop()

        #if active != self._active:
        #    self.old_value_chk_sounds = self.f_get_value_chk_sounds()
        #    self.old_value_chk_music = self.f_get_value_chk_music()
        #    self.old_value_volume_sounds = self.f_get_value_volume_sounds()
        #    self.old_value_volume_music = self.f_get_value_volume_music()

        self._active = active

    def get_music_state(self):
        return self.form_sounds["music_state"]
    
    def get_music_volumen(self):
        return self.form_sounds["music_volumen"]

    def get_effects_state(self):
        return self.form_sounds["effects_state"]
    
    def get_effects_volumen(self):
        return self.form_sounds["effects_volumen"]

    def set_active(self,name):
        for aux_form in self.forms_dict.values():
            aux_form.reset_form()
        self.forms_dict[name].activate_form()

    def set_form_sounds(self, clave, valor):
        self.form_sounds[clave] = valor

    def render(self):
        if self.background_sound_path != None:
            self.background_sound.set_volume(self.get_music_volumen())
        if self.image_background != None:
            self.surface.blit(self.image_background,(0,0))

    def reset_form(self):
        self.active = False

    def activate_form(self):
        self.tiempo_evita_doble_click = 1000
        self.active = True
        self.render()

    def update(self):
        pass

    def draw(self):
        self.master_surface.blit(self.surface,self.slave_rect)

    