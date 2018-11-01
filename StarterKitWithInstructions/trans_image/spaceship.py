import pygame
from bullet import Bullet

class Spaceship():

    def __init__(self,width,height,x,y,color):
        self.alpha  = 255
        self.width  = width
        self.height = height
        self.x      = x
        self.y      = y
        self.color  = color
        
        self.image = pygame.image.load("05passion_fruit.png")
        rect = self.image.get_rect()
        temp_surf = pygame.Surface((rect[2], rect[3]), pygame.locals.SRCALPHA)
        temp_surf.fill( (0, 0, 0, 0) )
        temp_surf.blit(self.image, (0,0))
        self.image = temp_surf

        return

    def moveLeft(self, dx):
        self.x -= dx
        # check the wall
        if self.x < 0:
            self.x = 0
        return

    def moveRight(self, dx, upper_limit):
        self.x += dx
        # check the wall
        if self.x > upper_limit:
            self.x = upper_limit
        return

    def moveUp(self, dy):
        self.y -= dy
        # check the wall
        if self.y < 0:
            self.y = 0
        return

    def moveDown(self, dy, board_height):
        self.y += dy
        # check the wall
        if self.y > board_height - self.height:
            self.y = board_height - self.height
        return

    def fire(self,width,height,color):
        return Bullet(width,height,(self.x + self.width) , (self.y + (self.height /2) - (height/2)),color)
    
    def draw(self, surface):
        #rect = pygame.Rect( self.x, self.y, self.width, self.height )
        #pygame.draw.rect(surface, self.color, rect)
        self.image.set_alpha(self.alpha)
        self.alpha -= 1
        if self.alpha < 0:
            self.alpha = 255
        surface.blit(self.image, (self.x, self.y))
        return
        
