import sys
import pygame
import bullet

def checkKeyDownEvents(event, settings, screen, myShip, bullets):
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
    elif event.key == pygame.K_SPACE:
        newBullet = bullet.Bullet(settings, screen, myShip)
        bullets.add(newBullet)


def checkKeyUpEvents(event, myship):
    if event.key == pygame.K_RIGHT:
        myship.movingRight = False
    elif event.key == pygame.K_LEFT:
        myship.movingLeft = False
    elif event.key == pygame.K_UP:
        myship.movingUp = False
    elif event.key == pygame.K_DOWN:
        myship.movingDown = False


def checkEvents(settings, screen, myShip, bullets):
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDownEvents(event, settings, screen, myShip, bullets)
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event, myShip)


def updateScreen(settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraws the screen at each loop pass.
    screen.fill(settings.backgroundColor)
    ship.blitme()
    for bullet in bullets:
        bullet.drawBullet()

    # cleans the screen
    pygame.display.flip()