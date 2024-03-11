import pygame

from palette import *
from tools import *

class MiniPaint:

    def __init__ (self):
        ## initialize pygame
        pygame.init()

        ## open new window
        self._window = pygame.display.set_mode((600, 420), pygame.DOUBLEBUF)
        pygame.display.set_caption('MiniPaint - OUKHEMANOU Mohand')

        ## create canvas
        self._canvas = pygame.Surface((600, 420), pygame.SRCALPHA, 32)

        ## initialize MiniPaint
        self._bgcolor = pygame.Color(255, 255, 255, 255) # white
        self._shapes = pygame.sprite.OrderedUpdates()
        self._palette = Palette(self._canvas.get_size())
        self._tools = Tools(self._canvas.get_size())

    def run (self):
        done = False
        tmp = None
        while not done:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self._tools.set_position(event.pos)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if self._tools.get_active_tool() == self._tools.Palette:
                        self._palette.pick_color()
                        print(event.pos)

                    elif tmp != None:
                        self._shapes.add(tmp)
                        tmp = None

                elif event.type == pygame.KEYDOWN:
                    if event.mod & pygame.KMOD_SHIFT:
                        self._tools.switch_tool(event.key)

                    elif event.mod & pygame.KMOD_CTRL:
                        if event.key == pygame.K_s:
                            pygame.image.save(self._canvas, "Dessin.png")

                elif event.type == pygame.MOUSEMOTION:
                    if event.buttons[0]:
                        tmp = self._tools.make_shape(self._palette.get_color(), event.pos)

                    elif self._tools.get_active_tool() == Tools.Palette:
                        self._palette.update_color(event.pos)

            ## clear window
            self._canvas.fill(self._bgcolor)

            ## draw existing shapes
            self._shapes.draw(self._canvas)

            ## draw current shape
            if tmp != None:
                self._canvas.blit(tmp.image, tmp.rect)


            ## display color picker
            if self._tools.get_active_tool() == Tools.Palette:
                self._canvas.blit(self._palette.get_color_picker(), (0, 0))
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._tools.switch_back()


            ## update display
            self._window.blit(self._canvas, (0, 0))
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    mp = MiniPaint()
    mp.run()
