from curses import KEY_DOWN, KEY_LEFT, KEY_RIGHT
import pygame
import sys
from constantes import *
from game import Game
from gui_form_menu_principal import FormMenuPrincipal
from gui_form_menu_configuracion import FormMenuConfiguracion
from gui_form_nivel import FormNivel


pygame.display.set_caption('Proyecto juego')
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    
pygame.init()
clock = pygame.time.Clock()

game = Game(screen)

game.add_form(FormMenuPrincipal(game.get_menu_config("MenuPrincipal"), 
                                master_surface=screen, 
                                f_get_value_chk_sounds=game.get_chk_sounds, 
                                f_get_value_chk_music=game.get_chk_music, 
                                f_get_value_volume_sounds=game.get_volume_sounds, 
                                f_get_value_volume_music=game.get_volume_music,
                                active=True))

game.add_form(FormMenuConfiguracion(game.get_menu_config("MenuConfiguracion"), 
                                master_surface=screen, 
                                f_get_value_chk_sounds=game.get_chk_sounds, 
                                f_get_value_chk_music=game.get_chk_music, 
                                f_get_value_volume_sounds=game.get_volume_sounds, 
                                f_get_value_volume_music=game.get_volume_music,
                                f_set_volumen=game.set_volumen,
                                active=False))

if LEVEL_DEBUG:
    game.add_form(FormNivel(  name="debug",
                            master_surface=screen,
                            game_config=game.config,
                            player_id="stink",
                            active=False, 
                            f_game_add_points=game.add_points,
                            f_game_add_time=game.add_time,
                            f_get_value_chk_sounds=game.get_chk_sounds, 
                            f_get_value_chk_music=game.get_chk_music, 
                            f_get_value_volume_sounds=game.get_volume_sounds, 
                            f_get_value_volume_music=game.get_volume_music,
                            f_set_game_volumen=game.set_volumen))      

game.add_form(FormNivel(  name="Nivel1",
                            master_surface=screen,
                            game_config=game.config,
                            player_id="stink",
                            active=False, 
                            f_game_add_points=game.add_points,
                            f_game_add_time=game.add_time,
                            f_get_value_chk_sounds=game.get_chk_sounds, 
                            f_get_value_chk_music=game.get_chk_music, 
                            f_get_value_volume_sounds=game.get_volume_sounds, 
                            f_get_value_volume_music=game.get_volume_music,
                            f_set_game_volumen=game.set_volumen))                            

game.add_form(FormNivel(  name="Nivel2",
                            master_surface=screen,
                            game_config=game.config,
                            player_id="stink",
                            active=False, 
                            f_game_add_points=game.add_points,
                            f_game_add_time=game.add_time,
                            f_get_value_chk_sounds=game.get_chk_sounds, 
                            f_get_value_chk_music=game.get_chk_music, 
                            f_get_value_volume_sounds=game.get_volume_sounds, 
                            f_get_value_volume_music=game.get_volume_music,
                            f_set_game_volumen=game.set_volumen))      

game.add_form(FormNivel(  name="Nivel3",
                            master_surface=screen,
                            game_config=game.config,
                            player_id="stink",
                            active=False, 
                            f_game_add_points=game.add_points,
                            f_game_add_time=game.add_time,
                            f_get_value_chk_sounds=game.get_chk_sounds, 
                            f_get_value_chk_music=game.get_chk_music, 
                            f_get_value_volume_sounds=game.get_volume_sounds, 
                            f_get_value_volume_music=game.get_volume_music,
                            f_set_game_volumen=game.set_volumen))          

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    delta_ms = clock.tick(FPS)

    keys = pygame.key.get_pressed()
    lista_eventos = pygame.event.get()

    for form in game.get_forms():
        if form.active:
            form.update(lista_eventos=lista_eventos, keys_pressed=keys, delta_ms=delta_ms)
            form.draw()

    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel

    pygame.display.flip()
     
    #print(delta_ms)
