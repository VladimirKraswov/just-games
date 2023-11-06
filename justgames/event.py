import pygame


class Event:

    @staticmethod
    def get():
        return pygame.event.get()

    @staticmethod
    def get_event_grab():
        return pygame.event.get_grab()

    @staticmethod
    def set_event_grab(new_status):
        pygame.event.set_grab(new_status)

