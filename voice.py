import pygame

# icon = pygame.image.load("images/monitor.png")


def spotifymain():
    pygame.font.init()
    pygame.display.set_caption("Voice Recognizer")
    screen = pygame.display.set_mode((300, 150))
    text = pygame.font.SysFont("monospace", 25)
    i = 0
    while i < 10000:
        textb = text.render("Say Song Name", 1, (255, 255, 255))
        screen.blit(textb, (50, 50))
        pygame.display.update()
        i = i+1

    pygame.quit()


def powermain():
    pygame.font.init()
    pygame.display.set_caption("Voice Recognizer")
    screen = pygame.display.set_mode((300, 150))
    text = pygame.font.SysFont("monospace", 25)
    i = 0
    while i < 10000:
        textb = text.render("Say Power Mode", 1, (255, 255, 255))
        screen.blit(textb, (50, 50))
        pygame.display.update()
        i = i+1

    pygame.quit()


def mainmain():
    pygame.font.init()
    pygame.display.set_caption("Voice Recognizer")
    screen = pygame.display.set_mode((300, 150))
    text = pygame.font.SysFont("monospace", 25)
    i = 0
    while i < 10000:
        textb = text.render("Say Function", 1, (255, 255, 255))
        screen.blit(textb, (50, 50))
        pygame.display.update()
        i = i+1

    pygame.quit()


def callmain():
    pygame.font.init()
    pygame.display.set_caption("Voice Recognizer")
    screen = pygame.display.set_mode((300, 150))
    text = pygame.font.SysFont("monospace", 25)
    i = 0
    while i < 10000:
        textb = text.render("Say Person name", 1, (255, 255, 255))
        screen.blit(textb, (50, 50))
        pygame.display.update()
        i = i+1

    pygame.quit()
