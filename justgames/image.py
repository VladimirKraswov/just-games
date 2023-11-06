import pygame


class Image:

    @staticmethod
    def load(file_name, transparent=False):
        try:
            image = pygame.image.load(file_name)
        except pygame.error:
            raise SystemExit('Could not load image "%s" %s' % (file_name, pygame.get_error()))
        if transparent:
            corner = image.get_at((0, 0))
            image.set_colorkey(corner, pygame.RLEACCEL)
        return image.convert()

    @staticmethod
    def scale(image, x_scale, y_scale=None):
        if y_scale is None:
            y_scale = x_scale
        (x_size, y_size) = image.get_size()
        x_size = int(x_size * x_scale)
        y_size = int(y_size * y_scale)
        return pygame.transform.scale(image, (x_size, y_size))

    @staticmethod
    def flip(image, x_bool, y_bool=False):
        return pygame.transform.flip(image, x_bool, y_bool)

    @staticmethod
    def rotate(image, angle):
        return pygame.transform.rotate(image, angle)


