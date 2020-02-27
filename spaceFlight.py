
import pygame
import settings
import ship
import gameFunctions as gf

# pygame.init() ruft die Funktion pygame.freetype.init()
# automatisch auf, wenn das Modul freetype zuvor importiert wurde.
# Darum wird hier nochmal explizit freetyp importiert.
import pygame.freetype

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

    font = pygame.freetype.Font("fonts/sans.ttf")

    gameRunning = True

    # myShip ist eine Instanz der Klasse Ship aus der Datei ship.
    myShip = ship.Ship(screen)

    bullets = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Starte die Hauptschleife des Spiels.
    if mySettings.gameRunning == True:
        while True:
            clock.tick(mySettings.fps)
            gf.checkEvents(mySettings, screen, myShip, bullets)
            myShip.update()
            gf.updateBullets(bullets, asteroids)
            gf.updateAsteriods(mySettings, screen, asteroids)
            gf.updateScreen(mySettings, screen, myShip, bullets, asteroids)
            if mySettings.gameRunning == False:
                break
    if mySettings.gameRunning == False:
        while True:
            gf.checkEventNewGame(mySettings)
            if mySettings.newGame == True:
                break
    if mySettings.newGame == True:
        mySettings.newGame = False
        run_game()

run_game()