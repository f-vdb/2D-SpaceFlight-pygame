import pygame


class Settings():
    """Eine Klasse fuer alle Einstellungen."""

    def __init__(self):
        """Initialisiere die Spieleinstellungen."""
        self.screenWidth = 800
        self.screenHight = 600
        self.backgroundColor = (230, 230, 230)
        self.windowCaption = "Space Flight"
        self.myShipSpeed = 10
        self.myShipDistanceBottomEdge = 10
        self.fps = 60

        self.bulletSpeed = self.myShipSpeed + 2  # damit das Raumschiff nicht
        # die eigenen Geschosse einholt.
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = 60, 60, 60
        self.allowedBullets = 3

        self.allowedAsteriods = 1

        self.colors = {
            "lightGrey": pygame.Color(200, 200, 200),
            "darkGrey": pygame.Color(100, 100, 100),
            "green": pygame.Color(50, 255, 63),
            "red": pygame.Color(220, 30, 30),
            "blue": pygame.Color(50, 75, 245),
            "black": pygame.Color(0, 0, 0)
        }

        self.gameRunning = True
        self.newGame = False
