
class Settings():
    """ Eine Klasse fuer alle Einstellungen."""

    def __init__(self):
        """Initialisiere die Spieleinstellungen."""
        self.screenWidth = 800
        self.screenHight = 600
        self.backgroundColor = (230, 230, 230)
        self.windowCaption = "Space Flight"
        self.myShipSpeed = 4
        self.fps = 60