import pygame


class GamesError (Exception): pass


class Screen(object):
    display_surface = None          # Поверхность экрана
    _initialised = False            # Существование экземпляра
    _width = 0                      # Ширина графического экрана
    _height = 0                     # Высота экрана
    _fullscreen = False             # Полноэкранный режим
    _fps_limit = 60                 # Частота обновления экрана
    _clock = pygame.time.Clock()    # Используем для ограничения FPS
    _draw_rect = False

    def __init__(self, screen_width=800, screen_height=600, fullscreen=False):
        if Screen._initialised:
            raise GamesError("Cannot have more than on Screen object")

        Screen.init_screen(screen_width, screen_height, fullscreen)

        Screen._initialised = True

    @staticmethod
    def init_screen(width=800, height=600, fullscreen=False):
        pygame.init()
        Screen._width = width
        Screen._height = height
        Screen._fullscreen = fullscreen
        if fullscreen:
            Screen.display_surface = pygame.display.set_mode((width, height),
                                                             pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
        else:
            Screen.display_surface = pygame.display.set_mode((width, height), pygame.HWSURFACE | pygame.DOUBLEBUF)

    @staticmethod
    def get_width():
        return Screen._width

    @staticmethod
    def get_height():
        return Screen._height

    @staticmethod
    def get_center_x():
        return int(Screen._width/2)

    @staticmethod
    def get_center_y():
        return int(Screen._height/2)

    @staticmethod
    def get_center():
        return {Screen.get_center_x(), Screen.get_center_y()}

    @staticmethod
    def get_fps_limit():
        return Screen._fps_limit

    @staticmethod
    def get_fps():
        return Screen._clock.get_fps()

    @staticmethod
    def clear(color=(15, 15, 15)):
        Screen.display_surface.fill(color)

    @staticmethod
    def set_draw_rect(boolean):
        Screen._draw_rect = boolean

    @staticmethod
    def draw(_object):
        Screen.display_surface.blit(_object.surface, _object.rect)
        if Screen._draw_rect:
            pygame.draw.rect(Screen.display_surface, (255, 255, 0), _object.rect, 1)

    @staticmethod
    def update():
        pygame.display.flip()
        Screen._clock.tick(Screen._fps_limit)  # Установить лимит на Game.__fps кадров в секунду
