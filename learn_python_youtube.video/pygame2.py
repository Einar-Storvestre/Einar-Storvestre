import pygame

#denne linje skal alltid være med i alle pygamekoder
pygame.init()
#                           bredde-høyde
screen=pygame.display.set_mode([800, 600])

#title
pygame.display.set_caption("einar sitt første spill")
#icon
#icon=pygame.image.load('ski_bilde.png')
#pygame.display.set_icon(icon)

#player
#playerimg=pygame.image.load


#game loop
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

#      RGB  -    red-green-blue
    screen.fill ((0,255,255))




#denne linjen skal alltid være med i alle pygamekoder
pygame.display.update()
