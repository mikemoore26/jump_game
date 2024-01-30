import pygame
from random import randint

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        y_pos = 0

        if type == "fly":
            fly_frame1 = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
            fly_frame2 = pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()
            self.frames = [fly_frame2, fly_frame1]
            y_pos = 210

        elif type == 'snail':
            snail_frame1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_frame2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame1, snail_frame2]
            y_pos = 300

        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(midbottom =( randint(600,900), y_pos))

    def animation(self):
        self.index += 0.1
        if self.index >= len(self.frames): self.index = 0
        self.image = self.frames[int(self.index)]

    def move(self):
        self.rect.x -= 4
        if self.rect.x <= -100:
            del self


    def update(self):
        self.move()
        self.animation()

    def draw(self,screen):
        screen.blit(self.index, self.rect)