import pygame
import sys
import random

class Snake: 

    def __init__(self): 
        #initialize pygame
        pygame.init()

        #window
        self._window = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption('Projet Pygame : Snake - OUKHEMANOU Mohand')

        #loop
        self._game = True

        #snake's dimension 
        self._snake = 10

        #start position
        self._x = 500
        self._y = 400

        #snake's body
        self._body = []

        #snake's size
        self._size = 1

        #snake's movement
        self._x_move = 0
        self._y_move = 0

        #apple's dimension
        self._apple = 10

        #apple's position
        self._x2 = random.randrange(30, 970, 10)
        self._y2 = random.randrange(30, 770, 10) 

        #score
        self._score = 0

        #initialize fps
        self._clock = pygame.time.Clock()

        #initialize colors
        self._black = (0, 0, 0)
        self._grey = (110, 122, 95)
        self._white = (255, 255, 255)
        self._green = (148, 218, 46)

        #accueil
        self._accueil = True
        self._image = pygame.image.load("snake_menu.jpeg")

    def run (self): 

        while self._accueil:
            
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self._accueil = False
                    
            self._window.fill(self._black)
            self._window.blit(self._image, (140, 150))
            self.texte("Accueil", "Press Enter to Start", (120, 600, 100, 725))
            pygame.display.flip()

        while self._game: 

            for event in pygame.event.get():
                
                #quit the window
                if event.type == pygame.QUIT:
                    sys.exit()
                
                #initialize the key to move the snake
                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_UP:
                        self._y_move = -10
                        self._x_move = 0
                    
                    elif event.key == pygame.K_DOWN:
                        self._y_move = 10
                        self._x_move = 0
                    
                    elif event.key == pygame.K_LEFT:
                        self._x_move = -10
                        self._y_move = 0
                    
                    elif event.key == pygame.K_RIGHT:
                        self._x_move = 10
                        self._y_move = 0

                    if event.key == pygame.K_z:
                        self._y_move = -10
                        self._x_move = 0
                    
                    elif event.key == pygame.K_s:
                        self._y_move = 10
                        self._x_move = 0
                    
                    elif event.key == pygame.K_q:
                        self._x_move = -10
                        self._y_move = 0
                    
                    elif event.key == pygame.K_d:
                        self._x_move = 10
                        self._y_move = 0
            
            #background
            self._window.fill(self._green)
            
            self.set_fps()

            self.set_snake()
            
            self.move()

            self.set_apple()

            self.eat_apple()

            self.contour()

            self.get_score()

            self.game_over()

            pygame.display.flip()

    def set_fps (self):
        #set the fps to 19
        self._clock.tick(19)
    
    def set_snake (self):
        #head of the snake
        pygame.draw.rect(self._window, self._black, (self._x, self._y, self._snake, self._snake))

        #position of the head 
        self._head = []
        self._head.append(self._x)
        self._head.append(self._y)

        #pposition of the body
        self._body.append(self._head)

        #body of the snake
        if len(self._body) > self._size: 
            self._body.pop(0)
        
        for i in self._body:
            pygame.draw.rect(self._window, self._black, (i[0], i[1], self._snake, self._snake))
    
    def move (self):
        #move the snake
        self._x += self._x_move
        self._y += self._y_move

    def set_apple (self):
        #create the apple
        pygame.draw.rect(self._window, self._grey, (self._x2, self._y2, self._apple, self._apple))

    def eat_apple (self):
        #what happened when we eat an apple ?  
        if (self._x == self._x2) and (self._y == self._y2):
            self._x2 = random.randrange(30, 970, 10)
            self._y2 = random.randrange(30, 770, 10)
            self._size += 1
            self._score += 1
    
    def contour (self):
        #contour of the window
        pygame.draw.rect(self._window, self._green, (0, 0, 1000, 800), 1)

    def get_score (self):
        #display the score
        self.texte("Score", "Score : {}".format(str(self._score)), (10, 10, 30, 50))
    
    def game_over (self):
        #pgame-over if we hit the contours
        if self._x <= 0:
            self._game = False
            print("Game Over - Your Score Is {}".format(str(self._score)))
        if self._x >= 1000:
            self._game = False
            print("Game Over - Your Score Is {}".format(str(self._score)))
        if self._y <=  0:
            self._game = False
            print("Game Over - Your Score Is {}".format(str(self._score)))
        if self._y >= 800:
            self._game = False
            print("Game Over - Your Score Is {}".format(str(self._score)))
        
        #game-over if we hit the body
        for i in self._body[:-1]: 
            if self._head == i:
                self._game = False
                print("Game Over - Your Score Was {}".format(str(self._score)))

    def texte (self, context, texte, position):
        #display text
        #condition according to the context
        if context == "Accueil" :
            font = pygame.font.SysFont("Arial.TFF", 100, True)
        if context == "Score":
            font = pygame.font.SysFont("Arial.TFF", 30, True)
        #display the text in a new surface
        texte = font.render(texte, True, self._white)
        self._window.blit(texte, position)

#run the game
if __name__ == '__main__':
    snk = Snake()
    snk.run()