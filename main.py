from justgames.games import *
import pygame
import random


class Logo(Sprite):
    img = Manager.image.load("logo.png", True)

    def __init__(self, x=0, y=0):
        super().__init__(Logo.img, opacity=255, x=x, y=y, interval=2*manager.screen.get_fps_limit())
        self.t = True

    def tick(self):
        manager.push_scene(mainScene)


    def update(self, *args):
        manager.screen.clear()


class L(Layer):
    img = manager.image.load("main_scene.png", True)
    img2 = manager.image.load("back.jpg")
    img3 = manager.image.load("girl.png", True)

    def __init__(self):
        super().__init__(1*Manager.screen.get_fps_limit())
        self.sprite1 = Sprite(L.img, right=manager.screen.get_width(), bottom=manager.screen.get_height())
        self.sprite2 = Sprite(L.img2, x=manager.screen.get_center_x(), y=manager.screen.get_center_y())
        self.sprite3 = Sprite(L.img3, angle=30, scale_x=2, scale_y=0.5, x=manager.screen.get_center_x(), y=manager.screen.get_center_y())
        self.add(self.sprite1)
        self.add(self.sprite2)
        self.add(self.sprite3)
        self.elevate(self.sprite1)
        self.dir = True
        self.surface2 = self.sprite1.get_surface()
        self.surface3 = Manager.image.flip(self.sprite1.get_surface(), True)

    def tick(self):
        pass

    def update(self, *args):
        if manager.keyboard.is_pressed(pygame.K_MINUS):
            self.sprite3.opacity -= 1
        if manager.keyboard.is_pressed(pygame.K_EQUALS):
            self.sprite3.opacity += 1

        if manager.keyboard.is_pressed(pygame.K_q):
            self.sprite3.scale_x -= 0.1
            self.sprite3.scale_y -= 0.1

        if manager.keyboard.is_pressed(pygame.K_w):
            self.sprite3.scale_x += 0.1
            self.sprite3.scale_y += 0.1

        if manager.keyboard.is_pressed(pygame.K_UP):
            self.sprite3.angle -= 1
        if manager.keyboard.is_pressed(pygame.K_DOWN):
            self.sprite3.angle += 1

        if manager.keyboard.is_pressed(pygame.K_LEFT):
            self.sprite3.x -= 8

        if manager.keyboard.is_pressed(pygame.K_RIGHT):
            self.sprite3.x += 8

        if manager.keyboard.is_pressed(pygame.K_d):
            self.sprite1.destroy()

        if manager.keyboard.is_pressed(pygame.K_SPACE):
            Manager.pop_scene()


class MainScene(Scene):
    def __init__(self):
        super().__init__()
        self.laer1 = self.add_layer(L())
        self.background = self.add_layer()

    def update(self):

        if manager.keyboard.is_pressed(pygame.K_ESCAPE):
            manager.quit()
        print(manager.screen.get_fps())


mainScene = MainScene()


class Greeting(Scene):
    def __init__(self):
        super().__init__()
        self.layer1 = self.add_layer()
        self.layer1.add(Logo(x=manager.screen.get_center_x(), y=manager.screen.get_center_y()))


manager.push_scene(Greeting())
manager.loop()


