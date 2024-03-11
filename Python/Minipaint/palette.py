import pygame

class Palette:

    def __init__ (self, canvas_size):
        self._color = pygame.Color(0, 0, 0, 255)
        self._hover = pygame.Color(0, 0, 0, 255)
        self._palette = pygame.image.load("color-picker.png")
        self._cp = pygame.Surface(canvas_size, pygame.SRCALPHA, 32)
        self._cp.fill(pygame.Color(0, 0, 0, 150))
        self._cp.blit(self._palette, (0, 0))

    def get_color (self):
        return self._color

    def update_color (self, pos):
        self._hover = self._cp.get_at(pos)
        rect = (260, 0, 10, 256)
        pygame.draw.rect(self._cp, self._hover, rect)

    def pick_color (self):
        self._color = self._hover

    def get_color_picker (self):
        rect = (270, 0, 10, 256)
        pygame.draw.rect(self._cp, self.get_color(), rect)
        return self._cp

