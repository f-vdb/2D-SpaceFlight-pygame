import sys
import pygame
import bullet
import asteroid

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
        fireBullet(settings, screen, myShip, bullets)


def fireBullet(settings, screen, myShip, bullets):
    if len(bullets) < settings.allowedBullets:
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


def checkEventNewGame(settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_n:
                print("n")
                settings.newGame = True


def checkEvents(settings, screen, myShip, bullets):
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDownEvents(event, settings, screen, myShip, bullets)
        elif event.type == pygame.KEYUP:
            checkKeyUpEvents(event, myShip)


def updateScreen(settings, screen, ship, bullets, asteriods):
    """Update images on the screen and flip to the new screen."""
    # Redraws the screen at each loop pass.
    screen.fill(settings.backgroundColor)
    ship.blitme()
    for bullet in bullets:
        bullet.drawBullet()

    for asteriod in asteriods:
        asteriod.drawAsteriod()

    if pygame.sprite.spritecollideany(ship, asteriods):
        font = pygame.freetype.Font("fonts/sans.ttf")
        font.render_to(screen, (200, 400), "Game OVER", settings.colors["black"], size=64)
        settings.gameRunning = False


    font = pygame.freetype.Font("fonts/sans.ttf")
    font.render_to(screen, (700, 32), "Hello World", settings.colors["darkGrey"], size=16)

    '''
    font.render_to(screen, (700, 32), "Hello World", settings.colors["darkGrey"],
                   settings.colors["blue"], size=16,
                   style=pygame.freetype.STYLE_UNDERLINE | pygame.freetype.STYLE_OBLIQUE)
    '''
    # cleans the screen
    pygame.display.flip()


def updateBullets(bullets, asteriods):
    # bullets fliegen unendlich weiter...kostet Arbeitsspeicher und CPU
    # print(len(bullets))
    # Geschosse die aus dem Bild geflogen sind loeschen.
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, asteriods, True, True)

def createAsteriods(settings, screen, asteriods):
    if len(asteriods) < settings.allowedAsteriods:
        newAsteriod = asteroid.Asteroid(settings, screen)
        asteriods.add(newAsteriod)

def updateAsteriods(settings, screen, asteriods):
    createAsteriods(settings, screen, asteriods)
    asteriods.update()

    for asteroid in asteriods.copy():
        if asteroid.rect.top > asteroid.screen_rect.bottom:
            asteriods.remove(asteroid)



