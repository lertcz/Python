import pygame, sys
from pygame.constants import K_SPACE
from random import randint

pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FlappyCube")

player_x, player_y = screen_width/2, screen_height/2

size = 60
player = pygame.Rect(player_x, player_y, size, size) # x, y, width, height
player.center = player_x, player_y

pipe = pygame.Rect(0, 0, 100, 500)
pipe.center = 650, 750
pipe2 = pygame.Rect(0, 0, 100, 500)
pipe2.center = 650, 50

points = 0
player_gravity = 4
running = True
started = False
failed = False
scored = False

pygame.font.init()
font = pygame.font.SysFont('arial', 45)
ENDfont = pygame.font.SysFont('arial', 100)
textsurface = font.render(str(points), False, "black")

#draw 1st frame
screen.fill("lightblue")
pygame.draw.rect(screen, "black", player)
pygame.display.flip()

while running:
    for event in pygame.event.get():
        #quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #flap if space is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_y -= 75
                started = True

    #collisions with top and bottom of the screen and pipes
    if (player.bottom > screen_height) or (player.top < 0) or (player.colliderect(pipe) or player.colliderect(pipe2)):
        failed = True

    if started:
        #players gravity
        player_y += player_gravity
        player.center = player_x, player_y

        #add points
        if player_x > pipe.center[0] and not scored:
            scored = True
            points += 1
            textsurface = font.render(str(points), False, "black")

        #move pipes
        speed = 3
        pipe.center = pipe.center[0] - speed, pipe.center[1]
        pipe2.center = pipe2.center[0] - speed, pipe2.center[1]

        #reset pipes
        if pipe.right < 0:
            offset = randint(-200,200)
            pipe.center = 650, 750 + offset
            pipe2.center = 650, 50 + offset

            scored = False
            
        #draw BG
        screen.fill("lightblue")

        #draw palyer
        pygame.draw.rect(screen, "black", player)

        #draw pipes
        pygame.draw.rect(screen, "#BFFF00", pipe)
        pygame.draw.rect(screen, "#BFFF00", pipe2)

        #draw score
        textsurface_rect = textsurface.get_rect(center=(screen_width/2, 50))
        screen.blit(textsurface, textsurface_rect)

        if failed:
            screen.fill("white")
            textsurface = ENDfont.render(str(points), False, "black")
            textsurface_rect = textsurface.get_rect(center=(screen_width/2, screen_height/2))
            screen.blit(textsurface, textsurface_rect)
            started = False

        pygame.display.flip()
        clock.tick(60)