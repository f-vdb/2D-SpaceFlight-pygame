import sys
import pygame
import settings
import ship
import asteroid
import gameFunctions as gf


def run_game():
    # Initialisiere das Spiel.
    pygame.init()
    # mySettings ist eine Instanz der Klasse Settings aus der Datei settings.
    mySettings = settings.Settings()

    # Spiel im Fenstermodus. Sinnvoll bei der Fehlersuche.
    # Darum ist die Zeile auskommentiert.
    # So kann die Zeile einfach wieder aktiviert werden.
    screen = pygame.display.set_mode((mySettings.screenWidth, mySettings.screenHight))

    # Spiel im Vollbilsmodus.
    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption(mySettings.windowCaption)
    # Schalte die Maus aus, damit sie nicht mehr sichtbar ist.
    pygame.mouse.set_visible(False)
    # einstellen der fps
    clock = pygame.time.Clock()

    # myShip ist eine Instanz der Klasse Ship aus der Datei ship.
    myShip = ship.Ship(screen)

    bullets = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Starte die Hauptschleife des Spiels.
    while True:
        print("len asteroids: ", len(asteroids))
        clock.tick(mySettings.fps)
        gf.checkEvents(mySettings, screen, myShip, bullets)
        myShip.update()
        gf.updateBullets(bullets)
        gf.updateAsteriods(mySettings, screen, asteroids)
        gf.updateScreen(mySettings, screen, myShip, bullets, asteroids)

run_game()