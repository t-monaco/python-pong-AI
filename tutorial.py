import pygame
from pong import Game

WIDTH, HEIGHT = 700, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

game = Game(WINDOW, WIDTH, HEIGHT)

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        game.move_paddle(left=True, up=True)
    elif keys[pygame.K_s]:
        game.move_paddle(left=True, up=False)

    game.loop()
    game.draw(False, True)
    pygame.display.update()

pygame.quit()
