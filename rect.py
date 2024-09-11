import pygame
pygame.init()
window = pygame.display.set_mode((400,400))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(window,(25,255,255),pygame.Rect(30,30,60,60))
    pygame.display.flip()


