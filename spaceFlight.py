import sys
import pygame

import settings
import ship

def run_game():
    # Initialisiere das Spiel.
    pygame.init()
    # mySettings ist eine Instanz der Klasse Settings aus der Datei settings.
    mySettings = settings.Settings()

    screen = pygame.display.set_mode((mySettings.screenWidth, mySettings.screenHight))
    pygame.display.set_caption(mySettings.windowCaption)
    # myShip ist eine Instanz der Klasse Ship aus der Datei ship.
    myShip = ship.Ship(screen)

    # Starte die Hauptschleife des Spiels.
    while True:
        # Lauscht auf Tastatur- und Mauseingaben.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(mySettings.backgroundColor)
        myShip.blitme() # blitme ist eine Methode der Klasse ship.
        pygame.display.flip()

run_game()


