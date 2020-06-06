import sys
import pygame
from settings import Settings

from ship import Ship

import game_functions as gf

from pygame.sprite import Group

def run_game():
     # Initialize game , create a screen object.
     pygame.init()
     ai_settings = Settings()
     #screen = pygame.display.set_mode((ai_settings.screen_height, ai_settings.screen_width))
     screen = pygame.display.set_mode((800, 500))
     pygame.display.set_caption("Alien Invasion")
     ship = Ship(ai_settings,screen)
     bullets = Group()


       # Start the main loop for the game

     while True:	 
       gf.check_events(ai_settings,screen,ship,bullets)
       ship.update()
       gf.update_bullets(bullets)
       gf.update_screen(ai_settings,screen,ship,bullets)
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
        # Make the most recently drawn screen visible. z
       screen.fill(ai_settings.bg_color)
       ship.blitme()
       pygame.display.flip()

run_game()