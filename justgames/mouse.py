import pygame


class Mouse(object):
    # ------Properties--------#

    ## position
    def get_position(self):
        return pygame.mouse.get_pos()

    def set_position(self, new_position):
        pygame.mouse.set_pos(new_position)

    position = property(get_position, set_position)

    ## x
    def get_x(self):
        return pygame.mouse.get_pos()[0]

    def set_x(self, new_x):
        current_y = pygame.mouse.get_pos()[1]
        pygame.mouse.set_pos((new_x, current_y))

    x = property(get_x, set_x)

    ## y
    def get_y(self):
        return pygame.mouse.get_pos()[1]

    def set_y(self, new_y):
        current_x = pygame.mouse.get_pos()[0]
        pygame.mouse.set_pos((current_x, new_y))

    y = property(get_y, set_y)

    ## is visible
    def set_is_visible(self, new_visibility):
        pygame.mouse.set_visible(new_visibility)

    is_visible = property(fset=set_is_visible)

    def is_pressed(self, button_number):
        return pygame.mouse.get_pressed()[button_number] == 1
