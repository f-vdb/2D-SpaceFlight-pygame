import pygame

class Asteroid(pygame.sprite.Sprite):
    """"""
    def __init__(self, settings, screen):
        """Erstelle ein Geschoss an der Position des Schiffes.
           Die Klasse Bullet erbt die Eigenschaften und Methoden der Klasse Sprite.
           Bullet ist abgeleitet von Sprite (Sprite Superklasse von Bullet).
        """
        # Init-Funktion von Sprite (Superklasse von Bullet) aufrufen.
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("images/stone80px.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = 100
        self.rect.top = self.screen_rect.top-100
        self.speed = 6
        self.settings = settings


    def update(self):
        self.rect.centery += self.speed

    def drawAsteriod(self):
        self.screen.blit(self.image, self.rect)


