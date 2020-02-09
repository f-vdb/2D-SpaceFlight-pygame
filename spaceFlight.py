import sys
import pygame
import settings
import ship
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

    # Starte die Hauptschleife des Spiels.
    while True:
        clock.tick(mySettings.fps)
        gf.checkEvents(mySettings, screen, myShip, bullets)
        myShip.update()
        bullets.update()
        # bullets fliegen unendlich weiter...kostet Arbeitsspeicher und CPU
        # print(len(bullets))
        # Geschosse die aus dem Bild geflogen sind loeschen.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)



        gf.updateScreen(mySettings, screen, myShip, bullets)

run_game()