from curses import KEY_DOWN, KEY_LEFT, KEY_RIGHT
import pygame
import sys
from constantes import *
from game import Game
from gui_form_menu_principal import FormMenuPrincipal
from gui_form_menu_configuracion import FormMenuConfiguracion
from gui_form_menu_highscore import FormMenuHighscore
from gui_form_nivel_completo import FormNivelCompleto
from gui_form_juego_completo import FormJuegoCompleto
from gui_form_ayuda import FormMenuAyuda
from gui_form_nivel import FormNivel


pygame.display.set_caption('Proyecto juego')
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    
pygame.init()
clock = pygame.time.Clock()

game = Game(screen)

game.add_form(FormMenuConfiguracion(game.get_menu_config("MenuConfiguracion"), 
                                master_surface=screen,
                                f_game_draw_bg=game.draw_bg,
                                active=False))

game.add_form(FormMenuPrincipal(game.get_menu_config("MenuPrincipal"), 
                                master_surface=screen, 
                                f_game_draw_bg=game.draw_bg,
                                f_game_set_player_id=game.set_player_id, 
                                active=True))

game.add_form(FormMenuAyuda(game.get_menu_config("MenuAyuda"), 
                                master_surface=screen, 
                                f_game_draw_bg=game.draw_bg,
                                active=False))

game.add_form(FormMenuHighscore(game.get_menu_config("MenuHighscore"), 
                                master_surface=screen, 
                                f_game_draw_bg=game.draw_bg,
                                f_game_get_ranking=game.get_raking,
                                active=False))

game.add_form(FormJuegoCompleto(game.get_menu_config("JuegoCompleto"), 
                                master_surface=screen, 
                                f_get_game_min_top_item=game.get_game_min_top_item,
                                f_game_draw_bg=game.draw_bg,
                                f_game_add_ranking=game.insert_ranking,
                                active=False))

game.add_form(FormNivelCompleto(game.get_menu_config("NivelCompleto"), 
                                master_surface=screen, 
                                f_game_draw_bg=game.draw_bg,
                                active=False))   

game.add_form(FormNivel(  name="Nivel1",
                            master_surface=screen,
                            game_config=game.config,
                            active=False, 
                            f_get_player_id=game.get_player_id,
                            f_game_add_points=game.add_points,
                            f_game_add_time=game.add_time,
                            f_game_get_time=game.get_total_time,
                            f_game_get_points=game.get_points,
                            f_game_draw_bg=game.draw_bg,
                            f_game_get_vidas_restantes=game.get_vidas_restantes,
                            f_game_set_vidas_restantes=game.set_vidas_restantes))                            

game.add_form(FormNivel(  name="Nivel2",
                            master_surface=screen,
                            game_config=game.config,
                            active=False, 
                            f_get_player_id=game.get_player_id,
                            f_game_add_points=game.add_points,
                            f_game_add_time=game.add_time,
                            f_game_get_time=game.get_total_time,
                            f_game_get_points=game.get_points,
                            f_game_draw_bg=game.draw_bg,
                            f_game_get_vidas_restantes=game.get_vidas_restantes,
                            f_game_set_vidas_restantes=game.set_vidas_restantes))        

game.add_form(FormNivel(  name="Nivel3",
                            master_surface=screen,
                            game_config=game.config,
                            active=False, 
                            f_get_player_id=game.get_player_id,
                            f_game_add_points=game.add_points,
                            f_game_add_time=game.add_time,
                            f_game_get_time=game.get_total_time,
                            f_game_get_points=game.get_points,
                            f_game_draw_bg=game.draw_bg,
                            f_game_get_vidas_restantes=game.get_vidas_restantes,
                            f_game_set_vidas_restantes=game.set_vidas_restantes))             

while True:

    lista_eventos = pygame.event.get()
    keys = pygame.key.get_pressed()

    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    delta_ms = clock.tick(FPS)

    for form in game.get_forms():
        if form.active:
            game.draw_bg()
            form.update(lista_eventos=lista_eventos, keys_pressed=keys, delta_ms=delta_ms)
            form.draw()
            

    pygame.display.flip()
    