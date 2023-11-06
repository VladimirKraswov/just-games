import pygame
from justgames.image import *
from justgames.game_object import GameObject


class Sprite(GameObject):
    def __init__(self, surface, opacity=255, angle=0, scale_x=1, scale_y=1, flip=False,
                 x=0, y=0, left=None, right=None, top=None, bottom=None,
                 is_collide=True, interval=1):
        super().__init__(interval)
        self._orig_surface = surface            # Поверхность-изображение, на основеё которого создан спрайт
        self._opacity = opacity                 # Степень прозрачность поверхности
        self._orig_surface.set_alpha(opacity)   # Задать степень прозрачность поверхности
        self._surface = self._orig_surface      # Поверхность которая будет выводиться на экран

        self._rect = self._surface.get_rect()
        self._rect.centerx = x  # Абсцисса
        self._rect.centery = y  # Ордината

        # Ордината верхней границы объекта
        if top is not None:
            self._rect.top = top
        # Ордината нижней границы объекта
        if bottom is not None:
            self._rect.bottom = bottom
        # Абсцисса левой границы объекта
        if left is not None:
            self._rect.left = left
        # Абсцисса правой границы объекта
        if right is not None:
            self._rect.right = right

        self._angle = angle                     # Угол наклона в градусах
        self._scale_x = scale_x
        self._scale_y = scale_y
        self.set_scale(scale_x, scale_y)
        if angle != 0:
            self.set_angle(angle)


        self._is_collide = is_collide

# Свойства ------------------------------------------------------------------------------------------------------------

    # Surface - Объект-изображение, на основе которого создан спрайт
    def get_surface(self): return self._surface
    def set_surface(self, new_surface):
        """Назначает new_image в качестве картинки спрайта"""
        if new_surface is not self._orig_surface:
            self._orig_surface = new_surface
        self._surface = Image.scale(self._orig_surface, self._scale_x, self._scale_y)
        self._surface = Image.rotate(self._surface, self._angle)
        pos = self.position
        self._rect = self._surface.get_rect()
        self.set_position(pos)
    surface = property(get_surface, set_surface)

    # Opacity
    def get_opacity(self): return self._opacity
    def set_opacity(self, new_oacity):
        self._opacity = new_oacity
        self._orig_surface.set_alpha(new_oacity)
        self.set_surface(self._orig_surface)
    opacity = property(get_opacity, set_opacity)

    # Angle - Угол наклона изображения
    def get_angle(self): return self._angle
    def set_angle(self, new_angle):
        self._angle = new_angle
        self.set_surface(self._orig_surface)
    angle = property(get_angle, set_angle)

    # Scale
    def get_scale_x(self): return self._scale_x
    def set_scale_x(self, new_scale_x):
        self._scale_x = new_scale_x
        if self._scale_x < 0: self.scale_x = 0
        self.set_surface(self._orig_surface)
    scale_x = property(get_scale_x, set_scale_x)

    def get_scale_y(self): return self._scale_y
    def set_scale_y(self, new_scale_y):
        self._scale_y = new_scale_y
        if self._scale_y < 0: self.scale_y = 0
        self.set_surface(self._orig_surface)
    scale_y = property(get_scale_y, set_scale_y)

    def get_scale(self): return {self._scale_x, self._scale_y}
    def set_scale(self, new_scale_x, new_scale_y=None):
        self._scale_x = new_scale_x
        if new_scale_y is not None:
            self._scale_y = new_scale_y
        else:
            self._scale_y = new_scale_x
        if self._scale_x < 0: self.scale_x = 0
        if self._scale_y < 0: self.scale_y = 0
        self.set_surface(self._orig_surface)

    # Rect
    def get_rect(self): return tuple(self._rect)
    def set_rect(self, new_rect): self._rect = new_rect
    rect = property(get_rect, set_rect)

    # Height - Высота изображения
    def get_height(self): return self._rect.height
    height = property(get_height)

    # Width - Ширина изображения
    def get_width(self): return self._rect.width
    width = property(get_width)

    # X - Абсцисса
    def get_x(self): return self._rect.centerx
    def set_x(self, new_x): self._rect.centerx = new_x
    x = property(get_x, set_x)

    # Y - Ордината
    def get_y(self): return self._rect.centery
    def set_y(self, new_y): self._rect.centery = new_y
    y = property(get_y, set_y)

    # Position - Положение спрайта на экране. Двухэлементный кортеж (х, у)
    def get_position(self): return self._rect.center
    def set_position(self, new_position): self._rect.center = new_position
    position = property(get_position, set_position)

    # Top - Ордината верхней границы спрайта
    def get_top(self): return self._rect.top
    def set_top(self, new_top): self._rect.top = new_top
    top = property(get_top, set_top)

    # Bottom - Ордината нижней границы спрайта
    def get_bottom(self): return self._rect.bottom
    def set_bottom(self, new_bottom): self._rect.bottom = new_bottom
    bottom = property(get_bottom, set_bottom)

    # Left - Абсцисса левой границы спрайта
    def get_left(self): return self._rect.left
    def set_left(self, new_left): self._rect.left = new_left
    left = property(get_left, set_left)

    # Right - Абсцисса правой границы спрайта
    def get_right(self): return self._rect.right
    def set_right(self, new_right): self._rect.right = new_right
    right = property(get_right, set_right)

    def get_is_collide(self): return self._is_collide
    def set_is_collide(self, new_status): self._is_collide = new_status
    is_collide = property(get_is_collide, set_is_collide)

# Методы --------------------------------------------------------------------------------------------------------------

    def collide(self, _object):
        if not self.is_collide or not _object.is_collide:
            return False
        if self._rect.colliderect(_object.rect):
            return True


