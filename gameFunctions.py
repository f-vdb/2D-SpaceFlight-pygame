import sys
import pygame

def checkEvents(myShip):
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_RIGHT:
                myShip.movingRight = True
            elif event.key == pygame.K_LEFT:
                myShip.movingLeft = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                myShip.movingRight = False
            elif event.key == pygame.K_LEFT:
                myShip.movingLeft = False

def updateScreen(mySettings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraws the screen at each loop pass.
    screen.fill(mySettings.backgroundColor)
    ship.blitme()

    # cleans the screen
    pygame.display.flip()