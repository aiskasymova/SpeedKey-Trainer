import pygame
import time

import sys
from Globals import Globals as gb
from User import User
from Statistics import Statistics

class Game:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.user = User('text.txt')
        self.stats = Statistics(self.user)

    def draw_text(self, surface, message, y_cord, font_size, color):
        font = pygame.font.Font('images/SpaceMono-Bold.ttf', font_size)
        text = font.render(message, 1, color)
        text_rect = text.get_rect(center=(gb.WIDTH / 2, y_cord))
        surface.blit(text, text_rect)

    def draw_surface(self, surface):
        surface.fill((0, 0, 0))
        surface.blit(gb.background, (0, 0))
        self.draw_text(surface, 'SpeedKey Trainer', gb.TITLE_Y, gb.TITLE_SIZE, gb.TITLE_COLOR)
        if self.user.prompt:
            if len(self.user.prompt) >= gb.NUMBER_OF_WORDS:
                lis = self.user.prompt.split()
                w1 = ' '.join(lis[:len(lis) // 2])
                w2 = ' '.join(lis[len(lis) // 2:])
                self.draw_text(surface, w1, 200, gb.TEXT_SIZE, gb.PROMPT_COLOR)
                self.draw_text(surface, w2, 240, gb.TEXT_SIZE, gb.PROMPT_COLOR)
            else:
                self.draw_text(surface, self.user.prompt, 240, gb.TEXT_SIZE, gb.PROMPT_COLOR)
            surface.fill((0, 0, 0), gb.DEF_RECT)
            pygame.draw.rect(surface, gb.RECT_COLOR, gb.DEF_RECT, gb.BORDER_W)
            self.draw_text(surface, self.user.result, 500, gb.TEXT_SIZE, gb.RESULT_COLOR)
            self.draw_text(surface, self.stats.results, 150, gb.TEXT_SIZE, gb.MEAN_RESULT_COLOR)

            if self.user.input:
                if len(self.user.input) >= 45:
                    lis = self.user.input.split()
                    w1 = ' '.join(lis[:len(lis) // 2])
                    w2 = ' '.join(lis[len(lis) // 2:])
                    self.draw_text(surface, w1, 325, gb.TEXT_SIZE, gb.INPUT_COLOR)
                    self.draw_text(surface, w2, 355, gb.TEXT_SIZE, gb.INPUT_COLOR)
                else:
                    self.draw_text(surface, self.user.input, 325, gb.TEXT_SIZE, gb.INPUT_COLOR)
            pygame.display.update()

    def run(self):
        while self.running:
            self.clock.tick(gb.FPS)
            self.stats.show_current_statistics()
            self.draw_surface(gb.WIN)
            self.check_finished()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if not self.user.timer_started:
                        self.user.start_time = time.time()
                        self.user.timer_started = True
                    x, y = pygame.mouse.get_pos()
                    if self.user.end:
                        self.reset_game()
                elif event.type == pygame.KEYDOWN:
                    if self.user.timer_started and not self.user.end:
                        if len(event.unicode) > 0:
                            self.user.read_letter(event, event.unicode)
                    if not self.user.timer_started and not self.user.end:
                        self.user.start_time = time.time()
                        self.user.timer_started = True
                        self.user.read_letter(event, event.unicode)
            pygame.display.update()

    def reset_game(self):
        self.user.start_time, self.user.time_taken = 0, 0
        self.user.timer_started, self.user.end = False, False
        self.user.input = ''
        self.user.accuracy, self.user.wpm = 0, 0
        self.user.result = ''
        self.user.error_count = 0
        self.user.prompt_ptr = 0
        self.user.word_count = 0
        self.user.prompt = self.user.get_sentence('text.txt')

    def check_finished(self):
        if self.user.input == self.user.prompt:
            self.stats.save_run_statistics()
