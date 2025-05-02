import pygame
import sys
import random
from pygame.locals import MOUSEBUTTONDOWN


def runpygame():
    # initialise
    pygame.init()

    # setup clock
    fps = 60
    fpsClock = pygame.time.Clock()

    # setup window
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))

    # setup color
    black = (0, 0, 0)
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    rect_color = (255, 255, 255)

    # initialise game loop
    running = True

    # countdown
    countdown = True
    count_start_time = pygame.time.get_ticks()
    int_countdown = "3"
    color_change_time = None

    # cheange color
    blue_on_off = False

    # averge
    ave = []

    # font_path
    font_path = 'NotoSansJP-VariableFont_wght.ttf'

    # Rect
    rect = pygame.Rect(150, 200, 500, 300)

    # time
    time = 0
    tmp_time = 0

    while running:

        # update
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if blue_on_off:
                    if rect.collidepoint(event.pos):
                        blue_on_off = False
                        ave.append((tmp_time - time) / 1000)

            # close window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # draw
        screen.fill(black)

        if countdown:
            # draw countdown
            font_count = pygame.font.Font(font_path, 80)
            count_text = font_count.render(int_countdown, True, white)
            screen.blit(count_text, [375, 50])

            # time count
            count_time = pygame.time.get_ticks() - count_start_time
            if count_time < 1000:
                int_countdown = '3'
            elif count_time < 2000:
                int_countdown = '2'
            elif count_time < 3000:
                int_countdown = '1'
            else:
                countdown = False
            time = pygame.time.get_ticks()

        if len(ave) < 5:
            if not blue_on_off:
                rect_color = (255, 255, 255)
                text = '青色になったらここをクリック！！'

            pygame.draw.rect(screen, rect_color, rect)
            tmp_time = pygame.time.get_ticks()
            # font
            font_loop = pygame.font.Font(font_path, 30)
            text_loop = font_loop.render(text, True, black)
            text_rect = text_loop.get_rect(center=rect.center)
            screen.blit(text_loop, text_rect)

            if color_change_time is None:
                ran = random.randint(1000, 5000)
                color_change_time = ran

            if not blue_on_off and tmp_time - time >= color_change_time:
                blue_on_off = True
                rect_color = (0, 0, 255)
                time = tmp_time
                color_change_time = None
                text = 'クリック！！'

        else:
            averave = sum(ave)/len(ave)

            # text on screen
            font = pygame.font.Font(font_path, 40)
            font_result = pygame.font.Font(font_path, 70)
            first_text = font.render('あなたの平均反応速度は・・・', True, white)
            result = font_result.render("{:.3f}".format(averave), True, yellow)
            end_text = font.render('でした！', True, white)

            screen.blit(first_text, [125, 100])
            screen.blit(result, [315, 180])
            screen.blit(end_text, [325, 300])
        pygame.display.flip()

        fpsClock.tick(fps)


if __name__ == '__main__':
    runpygame()
