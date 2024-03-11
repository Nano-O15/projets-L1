import sys
import pygame
import math

from shape import Shape

class Tools:
    Palette = 0
    Line = 1
    Circle = 2
    Rectangle = 3

    def __init__ (self, canvas_size):
        ## canvas
        self._canvas_size = canvas_size

        ## current tool setup
        self._active = Tools.Line
        self._previous = Tools.Palette
        self._pos = (0, 0)

    def get_active_tool (self):
        return self._active

    def switch_tool (self, key):
        self._previous = self._active
        if (key == pygame.K_p):
            self._active = Tools.Palette
        elif (key == pygame.K_l):
            self._active = Tools.Line
        elif (key == pygame.K_c):
            self._active = Tools.Circle
        elif (key == pygame.K_r):
            self._active = Tools.Rectangle
        else:
            sys.stderr.write('[ERROR] unknown tool for ' + str(key) + '\n')

    def switch_back (self):
        self._active = self._previous

    def set_position (self, pos):
        self._pos = pos

    def make_shape (self, color, pos):
        surface = pygame.Surface(self._canvas_size, pygame.SRCALPHA, 32)

        if self._active == Tools.Line:
            pygame.draw.line(surface, color, self._pos, pos)  

        elif self._active == Tools.Circle:
            x1 = self._pos[0]
            y1 = self._pos[1]
            x2 = pos[0]
            y2 = pos[1]
            diametre = math.sqrt((((x2 - x1)**2)+((y2 - y1)**2)))
            rayon = int(diametre/2)
            xcentre = (x1+x2)/2
            ycentre = (y1+y2)/2
            centre = (xcentre, ycentre)
            pygame.draw.circle(surface, color, centre, rayon, 1)  

        elif self._active == Tools.Rectangle:
            x1 = self._pos[0]
            y1 = self._pos[1]
            x2 = pos[0]
            y2 = pos[1]
            csg = (min(x1, x2), min(y1, y2))
            longueur = abs(x1 - x2)
            largeur = abs(y1 - y2)
            lxl = (longueur, largeur)
            rect = (csg, lxl)
            pygame.draw.rect(surface, color, rect, 1)  

        return Shape(surface)
