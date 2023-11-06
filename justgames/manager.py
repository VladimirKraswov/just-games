import pygame
from justgames.auxiliary import Stack  # И мпортируем стек из вспомогательного модуля
from justgames.image import Image
from justgames.screen import Screen
from justgames.keyboard import Keyboard
from justgames.mouse import Mouse
from justgames.event import Event
from justgames.sound import Sound


class Manager:
    image = Image()         # Класс для работы с изображениями
    screen = Screen(1024, 768, fullscreen=False)       # Графический экран
    keyboard = Keyboard()   # Класс для работы с клавиатурой
    mouse = Mouse()         # Класс для работы с мышкой
    event = Event()         # Класс для работы с событиями
    sound = Sound()
    _quit = False           # Если True, выходим из игры
    _stopped = False        # Если True, остановить сцену
    _stack_scene = Stack()  # Стек сцен
    _event = None

    @staticmethod
    def init():
        pass

    # Возвращает True если стек сцен пуст, иначе False
    @staticmethod
    def is_empty_scene():
        return Manager._stack_scene.is_empty()

    # Приостанавливает выполнение текущей сцены, поднимая её выше в стеке.
    # Ставит на её место другую сцену
    @staticmethod
    def push_scene(scene):
        Manager._stack_scene.push(scene)

    # Удаляет из стека текущую сцену, ставя на её место предыдущюю
    # Возвращает предыдущюю сцену в стеке
    @staticmethod
    def pop_scene():
        if not Manager._stack_scene.is_empty():
            return Manager._stack_scene.pop()

    # Меняет выполняемые сцены
    @staticmethod
    def replace_scene(scene):
        if not Manager._stack_scene.is_empty():
            Manager._stack_scene.pop()
            Manager._stack_scene.push(scene)

    # возвращает колличество сцен в стеке
    @staticmethod
    def count_scene():
        return Manager._stack_scene.size()

    # Останавливает текущюю счену
    @staticmethod
    def stop_scene():
        Manager._stopped = True

    # Возобновляет выполнение текущей сцены
    @staticmethod
    def start_scene():
        Manager._stopped = False

    # Основной игровой цыкл
    @staticmethod
    def loop():
        while not Manager._quit:
            # Обработка событий
            for event in Manager.event.get():           # Пройтись по всем событиям
                if event.type == pygame.QUIT:       # Если тип события выход то,
                    Manager.quit()                  # выходим из игры

            Manager._stack_scene.peek().update_tick()                # Обновляем сцену
            for layer in Manager._stack_scene.peek().get_layers():   # проходим по всем слоям в сцене.
                if layer.to_destroy:
                    Manager._stack_scene.peek().remove_layer(layer)
                layer.update_tick()                                  # Обновляем сой
                for obj in layer.get_objects():                      # Проходим по всём объектам в слое
                    if obj.to_destroy:
                        layer.remove(obj)
                    obj.update_tick()                                # Обновляем объекты
                    Manager.screen.draw(obj)                         # Рисуем объекты

            Manager.screen.update()                                  # Выводим всё на дисплей

    # Выход из игры
    @staticmethod
    def quit():
        pygame.time.wait(1000)
        Manager._quit = True


manager = Manager

