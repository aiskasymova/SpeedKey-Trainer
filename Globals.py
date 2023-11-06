import pygame


class Globals(object):
    WIDTH, HEIGHT = 800, 600
    FPS = 30
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('SpeedKey Trainer')
    TITLE_SIZE = 55
    TITLE_Y = 100
    pygame.init()

    background = pygame.image.load('images/openPic.jpeg')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    TITLE_COLOR = (249, 231, 159)
    PROMPT_COLOR = (210, 255, 87)
    RECT_COLOR = (133, 193, 233)
    INPUT_COLOR = (93, 173, 226)
    RESULT_COLOR = (250, 33, 17)
    MEAN_RESULT_COLOR = (242, 78, 155)

    NUMBER_OF_WORDS = 60
    TEXT_SIZE = 22

    DEF_RECT = (50, 300, 700, 80)
    BORDER_W = 2