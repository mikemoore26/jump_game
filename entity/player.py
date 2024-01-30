import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        player_walk2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
        self.player_walk = [player_walk1, player_walk2]
        self.player_index = 0
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.3)


    def animation(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0

            self.image = self.player_walk[int(self.player_index)]

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def collide_obstacles(self,obstacles):
        for obj in obstacles:
            if self.rect.colliderect(obj.rect):
                print("game")



    def update(self, obstacles) -> None:
        self.player_input()
        self.apply_gravity()
        self.animation()
        #self.collide_obstacles(obstacles)

    def draw(self,screen):

        screen.blit(self.image,self.rect)