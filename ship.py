import pygame

# Geschwindigkeit des Raumschiffes jetzt auch in settings.
import settings
mySettings = settings.Settings()

class Ship():
    # Init-Funktion bekommt einen Parameter (ein Argument): screen)
    def __init__(self, screen):
        # Eigenschaften der Klasse Ship:
        self.screen = screen
        self.image = pygame.image.load("images/rocket01.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Plaziert jedes das Raumschiff mittig am unteren Bidlschirmrand.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom -mySettings.myShipDistanceBottomEdge

        self.movingRight = False
        self.movingLeft = False

    # Methode der Klassen Ship:
    def update(self):
        if self.movingRight == True:
            self.rect.centerx += mySettings.myShipSpeed
        if self.movingLeft == True:
            self.rect.centerx -= mySettings.myShipSpeed

    def blitme(self):
        """ Zeichne das Raumschiff.
            blit: zeichnet ein Image auf das andere. """
        self.screen.blit(self.image, self.rect)



