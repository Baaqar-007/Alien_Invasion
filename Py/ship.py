import pygame
class Ship:
    def __init__(self,ai_game):

        #initialise the ship and set its starting posiyion
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        #load the ship and get its rect
        self.image=pygame.image.load('images/Ship.bmp')
        self.rect=self.image.get_rect()

        #Start each new ship at the bottom centre of the screen
        self.rect.midbottom=self.screen_rect.midbottom

        #store a decimal value for the ship's horz position
        self.x=float(self.rect.x)
        #Movement flags
        self.moving_right=False
        self.moving_left=False
    def update(self):
        """update the ship's position based on the movement flags"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
           self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
           self.x-=self.settings.ship_speed

        #update rect object from self.x
        self.rect.x=self.x

    def blitme(self):
        #draw the ship at its current location
        self.screen.blit(self.image, self.rect)
