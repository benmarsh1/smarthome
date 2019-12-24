
from control import *
import pygame

pygame.init()

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 128)

screen = pygame.display.set_mode([500, 500])
screen.fill((255,255,255))
textsurface = font.render('On', True, (0, 0, 0))
pygame.display.set_caption(device.name)
running = True
def printtext(text,r,g,b):
    textsurface = font.render(text, True, (r, g, b))
    screen.blit(textsurface,
                (250 - textsurface.get_width() // 2, 240 - textsurface.get_height() // 2))

printtext("on", 0, 0, 0)
pygame.display.flip()

while running:



    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    answer=input("Do you want to:\n1.change the colour of the lights?\n2.turn light on or off?\n3.exit.\n>>")
    if answer == "1":
        change_colour()
        screen.fill((device.Light.r, device.Light.g, device.Light.b))
        printtext("on", 0, 0, 0)
    elif answer == "2":
        device.state=input("Do you want to turn it on or off?:\n>>")
        if device.state == "on":
            screen.fill((255,255,255))
            printtext("on",0,0,0)
        elif device.state == "off":
            screen.fill((0,0,0))
            printtext("off",255,255,255)
    elif answer == "3":
        pygame.quit()
        raise SystemExit
    pygame.display.flip()


pygame.quit()