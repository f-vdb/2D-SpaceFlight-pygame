import sys
import pygame


def checkKeyDownEvents(event, myShip):
    if event.key == pygame.K_RIGHT:
        myShip.movingRight = True
    elif event.key == pygame.K_LEFT:
        myShip.movingLeft = True
    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_UP:
        myShip.movingUp = True
    elif event.key == pygame.K_DOWN:
        myShip.movingDown = True


def checkKeyUpEvents(event, myship):
    if event.key == pygame.K_RIGHT:
        myship.movingRight = False
    elif event.key == pygame.K_LEFT:
        myship.movingLeft = False
    elif event.key == pygame.K_UP:
        myship.movingUp = False
    elif event.key == pygame.K_DOWN:
        myship.movingDown = False


def checkEvents(myShip):
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDownEvents(event, myShip)
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event, myShip)


def updateScreen(mySettings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraws the screen at each loop pass.
    screen.fill(mySettings.backgroundColor)
    ship.blitme()

    # cleans the screen
    pygame.display.flip()