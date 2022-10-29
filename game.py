import pygame
import random
import math
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))


def instruction():
    def text(x, y, colour, text, size):
        font = pygame.font.SysFont("Stencil Std", size)
        text1 = font.render(text, True, colour)
        screen.blit(text1, (x, y))

    white = (255, 255, 255)
    light_red = (255, 140, 140)
    red = (255, 0, 0)
    intro = pygame.image.load('intro.png')
    yes = True
    while yes:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                yes = False
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.blit(intro, (0, 0))
        if 550 + 200 > mouse[0] > 550 and 460 + 70 > mouse[1] > 460:
            pygame.draw.rect(screen, light_red, [550, 460, 200, 70])
            if click == (1, 0, 0):
                yes = False
        else:
            pygame.draw.rect(screen, red, [550, 460, 200, 70])
        text(583, 475, white, 'BACK', 70)
        text(30, 50, red, 'UP FOR FORWARD', 70)
        text(30, 150, red, 'DOWN FOR BACKWARD', 70)
        text(30, 250, red, 'HOME FOR LEFT', 70)
        text(30, 350, red, 'END FOR RIGHT', 70)
        text(5, 580, red, '*hope you like the game*', 30)
        text(10, 460, red, 'HIGH SCORE :', 50)
        pygame.display.update()


def Pause():
    def text(x, y, colour, text, size):
        font = pygame.font.Font(None, size)
        text = font.render(text, True, colour)
        screen.blit(text, (x, y))

    white = (255, 255, 255)
    light_red = (255, 150, 150)
    red = (255, 0, 0)
    intro = pygame.image.load('intro.png')
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.blit(intro, (0, 0))
        if 0 + 200 > mouse[0] > 0 and 520 + 80 > mouse[1] > 520:
            pygame.draw.rect(screen, light_red, [0, 520, 200, 80])
            if click == (1, 0, 0):
                pause = False
                running = False
        else:
            pygame.draw.rect(screen, red, [0, 520, 200, 80])
        if 270 + 250 > mouse[0] > 300 and 520 + 80 > mouse[1] > 520:
            pygame.draw.rect(screen, light_red, [240, 520, 250, 80])
            if click == (1, 0, 0):
                game_loop()
        else:
            pygame.draw.rect(screen, red, [240, 520, 250, 80])

        if 500 + 250 > mouse[0] > 500 and 520 + 80 > mouse[1] > 520:
            pygame.draw.rect(screen, light_red, [530, 520, 270, 80])
            if click == (1, 0, 0):
                instruction()
        else:
            pygame.draw.rect(screen, red, [530, 520, 270, 80])

        text(12, 540, white, 'RESUME', 60)
        text(272, 540, white, 'RESTART', 60)
        text(542, 540, white, 'INSTRUCTION', 50)

        pygame.display.update()


def intro():
    # pygame.mixer.music.play(1)
    black = (0, 0, 0)
    RED = (255, 0, 0)
    greens = (5, 100, 5)
    blues = (84, 84, 255)
    blue = (0, 0, 255)
    green = (34, 65, 67)
    greena = (4, 198, 5)
    WHITE = (255, 255, 255)
    white = (255, 250, 120)
    pink = (255, 39, 39)

    def text(x, y, colour, text, size):
        font = pygame.font.Font(None, size)
        text = font.render(text, True, colour)
        screen.blit(text, (x, y))

    fonts = pygame.font.Font(None, 130)
    title = fonts.render("90'S GAME" , True, WHITE)
    intros = pygame.image.load('dodge.png')
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                quit()

        def text_object(text, font):
            textsurface = font.render(text, True, RED)
            return textsurface, textsurface.get_rect()

        # screen.fill(greena)
        screen.blit(intros, (0, 0))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 0 + 275 > mouse[0] > 0 and 500 + 100 > mouse[1] > 500:
            pygame.draw.rect(screen, pink, [0, 500, 275, 100])
            if click == (1, 0, 0):
                game_loop()
        else:
            pygame.draw.rect(screen, RED, [0, 500, 275, 100])
        if 255 + 300 > mouse[0] > 255 and 500 + 100 > mouse[1] > 500:
            pygame.draw.rect(screen, blues, [255, 500, 300, 100])
            if click == (1, 0, 0):
                instruction()
        else:
            pygame.draw.rect(screen, blue, [255, 500, 300, 100])
        if 555 + 300 > mouse[0] > 555 and 500 + 100 > mouse[1] > 500:
            pygame.draw.rect(screen, greena, [555, 500, 300, 100])
            if click == (1, 0, 0):
                intro = False
        else:
            pygame.draw.rect(screen, greens, [555, 500, 300, 100])
        screen.blit(title, (165, 85))
        text(90, 540, black, 'START', 50)
        text(295, 540, black, 'INSTRUCTION', 50)
        text(630, 540, black, 'QUIT', 50)
        pygame.display.update()


def game_loop():
    white = (200, 200, 200)
    whites = (255, 255, 255)
    # player car coordinate
    pygame.mixer.music.stop()
    # pygame.mixer.music.play()
    x = random.randint(220, 450)
    y = 300
    a = 0
    x_change = 0
    y_change = 0
    leftx = random.randint(200, 350)
    lefty = -10
    lefty_change = 3
    rightx = random.randint(350, 500)
    righty = -500
    righty_change = 2
    # colors
    RED = (255, 0, 0)
    green = (30, 130, 0)
    print('X ' + str((x)), 'Y ' + str((y)))
    print('LEFTX ' + str((leftx)))

    def crash(x, y, x1, y1):
        distance = math.sqrt(math.pow(x - x1, 2)) + (math.pow(y - y1, 2))
        if distance <= 40:
            return True
        else:
            return False

    def text_objects(text, font):
        textsurface = font.render(text, True, RED)
        return textsurface, textsurface.get_rect()

    def message_display(text):
        largetext = pygame.font.Font('freesansbold.ttf', 75)
        textsurf, textrect = text_objects(text, largetext)
        textrect.center = (400, 300)
        screen.blit(textsurf, textrect)
        pygame.display.update()
        time.sleep(3)
        game_loop()

    def out():
        message_display('YOU CRASHED')

    def out2():
        message_display('YOU CROSS LINE')

    def obs(x, y, z):
        if z == 0:
            left = pygame.image.load('left.png')
            screen.blit(left, (x, y))
        if z == 1:
            right = pygame.image.load('right.png')
            screen.blit(right, (x, y))

    def text(x, y, colour, text, size):
        font = pygame.font.Font(None, size)
        text = font.render(text, True, colour)
        screen.blit(text, (x, y))

    player = pygame.image.load('front.png')
    road = pygame.image.load('road.png')
    strip = pygame.image.load('strip.png')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = 2

                elif event.key == pygame.K_RIGHT:
                    x_change = -2

                elif event.key == pygame.K_UP:
                    y_change = -2

                elif event.key == pygame.K_DOWN:
                    y_change = 2
                if event.type == pygame.K_ESCAPE:
                    Pause()

                elif event.key == pygame.K_SPACE:
                    running = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        a += 1
        # print(a)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x <= 150:
            print("LINE CROSSED")
            out2()
        if x >= 510:
            print("LINE CROSSED")
            out2()
        x -= x_change
        y += y_change
        lefty += lefty_change
        righty += righty_change
        if lefty >= 650:
            lefty = -410
            leftx = random.randint(200, 350)
            obs(leftx, lefty, 0)
        if righty >= 700:
            righty = -500
            rightx = random.randint(350, 500)
            obs(rightx, righty, 1)
        collision = crash(x, y, leftx, lefty)
        if collision:
            print("CAR CRASHED")
            out()
        collision1 = crash(x, y, rightx, righty)
        if collision1:
            print('CAR  CRASHED')
            out()
        if 650 + 150 > mouse[0] > 650 and 2 + 50 > mouse[1] > 2:
            pygame.draw.rect(screen, white, [650, 2, 150, 50])
            if click == (1, 0, 0):
                Pause()
        else:
            pygame.draw.rect(screen, whites, [650, 2, 150, 50])
        screen.fill(green)
        screen.blit(road, (200, 0))
        screen.blit(strip, (395, 0))
        obs(leftx, lefty, 0)
        obs(rightx, righty, 1)
        screen.blit(player, (x, y))
        text(665, 12, RED, 'PAUSE', 55)
        text(10, 10, RED, 'SCORE: ', 50)
        text(145, 10, RED, str(a), 50)

        pygame.display.update()
intro()
