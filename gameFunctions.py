import sys

import pygame

def checkEvents():
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def updateScreen(mySettings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraws the screen at each loop pass.
    screen.fill(mySettings.backgroundColor)
    ship.blitme()

    # cleans the screen
    pygame.display.flip()