import pygame


class Sound:
    pygame.mixer.init(44100, -16, 2, 2048)

    @staticmethod
    def load_sound(file_name):
        return pygame.mixer.Sound(file_name)

    @staticmethod
    def load_music(file_name):
        pygame.mixer.music.load(file_name)

    @staticmethod
    def play_music(loop=0):
        pygame.mixer.music.play(loop)

    @staticmethod
    def fadeout_music(millisec):
        pygame.mixer.music.fadeout(millisec)

    @staticmethod
    def stop_music():
        pygame.mixer.music.stop()
