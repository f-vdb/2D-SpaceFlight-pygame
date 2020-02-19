
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

        self.bulletSpeed = self.myShipSpeed + 2 # damit das Raumschiff nicht
                                                # die eigenen Geschosse einholt.
        self.bulletWidth = 3
        self.bulletHeight = 15
        self.bulletColor = 60, 60, 60
        self.allowedBullets = 3


        self.allowedAsteriods = 1

