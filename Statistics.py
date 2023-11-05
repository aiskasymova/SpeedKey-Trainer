import pygame
import time
import numpy as np


class Statistics:
    def __init__(self, user1):
        self.user = user1
        self.wpm_stats = []
        self.accuracy_stats = []
        self.error_count_stats = []
        self.mean_accuracy = 0
        self.mean_wpm = 0
        self.mean_error_count = 0
        self.times_played = 0
        self.results = ''

    def save_run_statistics(self):
        user = self.user
        if user.timer_started and not user.end:
            user.time_taken = time.time() - user.start_time
            user.accuracy = max(100 - (user.error_count * 100 / user.prompt_ptr), 0) if user.prompt_ptr > 0 else 100
            user.wpm = len(user.input) * 60 / (5 * user.time_taken) if len(user.input) > 0 else 0
            user.end = True
            user.result = f'Time : {round(user.time_taken)} | | Accuracy: {round(user.accuracy)}% WPM: {round(user.wpm)} Errors: {user.error_count}'
            self.wpm_stats.append(user.wpm)
            self.accuracy_stats.append(user.accuracy)
            self.error_count_stats.append(user.error_count)
            self.times_played += 1
            self.update_session_statistics()
            print(user.result)

    def show_current_statistics(self):
        user = self.user
        if user.timer_started and not user.end:
            user.time_taken = time.time() - user.start_time
            accuracy = max(100 - (user.error_count * 100 / user.prompt_ptr), 0) if user.prompt_ptr > 0 else 100
            wpm = round(len(user.input) * 60 / (5 * (time.time() - user.start_time))) if len(user.input) > 0 else 0
            user.result = f'Time : {round(user.time_taken)} Accuracy: {round(accuracy)}% WPM: {round(wpm)}  Errors: {user.error_count}'
            pygame.display.update()

    def update_session_statistics(self):
        if self.times_played > 0:
            self.mean_accuracy = np.mean(self.accuracy_stats)
            self.mean_wpm = np.mean(self.wpm_stats)
            self.mean_error_count = np.mean(self.error_count_stats)
            self.results = f'Mean accuracy: {round(self.mean_accuracy)}% Mean WPM: {round(self.mean_wpm)}  Mean errors: {round(self.mean_error_count)}'
