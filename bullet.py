import pygame

class Bullet(pygame.sprite.Sprite):
    """Geschosse abgefeuert vom Raumschiff."""
    def __init__(self, settings, screen, ship):
        """Erstelle ein Geschoss an der Position des Schiffes.
           Die Klasse Bullet erbt die Eigenschaften und Methoden der Klasse Sprite.
           Bullet ist abgeleitet von Sprite (Sprite Superklasse von Bullet).
        """
        # Init-Funktion von Sprite (Superklasse von Bullet) aufrufen.
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, settings.bulletWidth, settings.bulletHeight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = settings.bulletColor
        self.speed = settings.bulletSpeed

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)



