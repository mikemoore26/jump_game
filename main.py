import pygame
from sys import exit
from random import randint

from entity.player import Player
from entity.Obstacle import Obstacle


def display_score():
    current_time = pygame.time.get_ticks() // 1000 - start_time
    score_surface = test_font.render(f"score: {current_time}", False, (64, 64, 64))
    screen.blit(score_surface, score_surface.get_rect(midtop = (WIDTH//2, 50)))
    return current_time

def collision():
    if pygame.sprite.spritecollide(player.sprite,obstacles_group, False):
        obstacles_group.empty()
        return False
    return True

pygame.init()

GAME_TITLE = "Mike\'s Jumping Game"
WIDTH, HEIGHT = 800, 400
BG_MUSIC = pygame.mixer.Sound('audio/music.wav')
BG_MUSIC.set_volume(0.1)
BG_MUSIC.play(loops=  -1)

pygame.display.set_caption(GAME_TITLE)

screen = pygame.display.set_mode((WIDTH,HEIGHT))

RUNNING = True

GAME_ACTIVE = False
player = pygame.sprite.GroupSingle()
player.add(Player())
obstacles_group = pygame.sprite.Group()

floor_y = 300
start_time = 0
score = 0

Clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# snail_frame1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# snail_frame2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
# snail = [snail_frame1,snail_frame2]
# snail_index = 0
# snail_surface = snail_frame1
#snail_rect = snail_surface.get_rect(midbottom = (700,300))

#timer
obstacle_timer = pygame.USEREVENT+1
pygame.time.set_timer(obstacle_timer,2000)

snail_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_timer,500)

fly_timer = pygame.USEREVENT + 2
pygame.time.set_timer(fly_timer,300)

while RUNNING:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
            pygame.quit()
            exit()

        if GAME_ACTIVE:
            # if event.type == pygame.MOUSEMOTION:
            #     if player_rect.collidepoint(event.pos):
            #         print('event: collide')
            #
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
            #         player_gravity = -20

            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacles_group.add(Obstacle('snail'))
                    #obstacles.append(snail_surface.get_rect(bottomright=(randint(900, 1100), 300)))
                else:
                    obstacles_group.add(Obstacle('fly'))
                    #obstacles.append(fly_surface.get_rect(center=(900,160)))

            if event.type == fly_timer:
                pass
                # if fly_index == 0:
                #     fly_index = 1
                # else :
                #     fly_index = 0
                #
                # fly_surface = fly[fly_index]

            if event.type == snail_timer:
                pass
                # if snail_index == 0:
                #     snail_index = 1
                # else :
                #     snail_index = 0
                #
                # snail_surface = snail[snail_index]


        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #snail_rect.x = 700
                    start_time = pygame.time.get_ticks() // 1000
                    #obstacles_group = pygame.sprite.Group()
                    GAME_ACTIVE = True


    if GAME_ACTIVE:

        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface,(0,300))


        score = display_score()

        # screen.blit(snail_surface, snail_rect)
        # snail_rect.left -= 4

        #obstacles = obstacle_movement(obstacle_list=obstacles)


        player.update(obstacles_group)
        player.draw(screen)
        # player_animation()

        obstacles_group.update()
        obstacles_group.draw(screen)

        GAME_ACTIVE = collision()


    else:
        screen.fill('Orange')
        title_text = test_font.render(GAME_TITLE,False, (34,54,22))
        title_text_rec = title_text.get_rect(center = (WIDTH//2,50))
        screen.blit(title_text,title_text_rec)

        standing_man = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
        standing_man = pygame.transform.rotozoom(standing_man,0, 2)
        standing_man_rect = standing_man.get_rect(center = (WIDTH//2, HEIGHT//2))
        screen.blit(standing_man,standing_man_rect)


        if score != 0:
            score_text = test_font.render(f"Score: {score}", False, (34,43,22))
            screen.blit(score_text, score_text.get_rect(center =(WIDTH//2, HEIGHT-50)))

        info_text = test_font.render("Press space to continue...", False, (34, 54, 22))
        info_text_rec = info_text.get_rect(center=(WIDTH // 2, HEIGHT-20))
        screen.blit(info_text, info_text_rec)







    pygame.display.update()
    Clock.tick(60)
