import pygame

class Button:
    def __init__(self):
        self.touching = False
        self.pressed = False
        self.width = 300
        self.height = 75
        self.color = (0,0,0)
        self.rect = pygame.Rect(150,300, self.width, self.height)
        self.font = pygame.font.Font('freesansbold.ttf', 32)