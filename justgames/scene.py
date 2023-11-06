from justgames.game_object import *
from justgames.sprite import *


class Layer(GameObject):
    def __init__(self, interval=1):
        super().__init__(interval=interval)
        self.__objects = []

    def get_objects(self):
        return self.__objects

    def add(self, _object):
        self.__objects.append(_object)

    def remove(self, _object):
        self.__objects.remove(_object)

    def elevate(self, _object, above=None):
        objects = self.__objects[:]
        objects.remove(_object)

        if above is None:
            objects.append(_object)
        else:
            idx = 1+objects.index(above)
            objects[idx:idx] = [_object]

        self.__objects = objects

    def lower(self, _object, below=None):
        objects = self.__objects[:]
        objects.remove(_object)

        if below is None:
            self.__objects = [_object]+objects
        else:
            idx = objects.index(below)
            objects[idx:idx] = [_object]
            self.__objects = objects

    def get_collide_objects(self, _object):
        """Функция принимает объект, и возвращает список всех объектов пересикающихся с ним"""
        collide_list = []  # Список всех объектов пересикающихся с _object

        if not isinstance(_object, Sprite):           # Если _object не является Sprite,
            return collide_list                       # или его потомком, возвращаем пустой список

        for obj in self.__objects:                    # Перебираем все объекты в слое
            if obj is not _object:                    # Если очередной объект не _object то идём дальше
                if isinstance(obj, Sprite):           # Если объект Sprite или его потомок, то идем дальше
                    if obj.is_collide:                # Если у объекта включена проверка пересечений, идём дальше
                        if obj.collide(_object):      # Если объект пересикаеться с _object то,
                            collide_list.append(obj)  # добавляем иго в список

        return collide_list


class Scene(GameObject):
    def __init__(self, interval=1):
        super().__init__(interval=interval)
        self.__layers = []

    def get_layers(self):
        return self.__layers

    def add_layer(self, layer=None):
        if layer is not None:
            self.__layers.append(layer)
        else:
            self.__layers.append(Layer())

        return self.__layers[len(self.__layers)-1]

    def remove_layer(self, layer):
        if layer in self.__layers:
            self.__layers.remove(layer)

    def elevate(self, layer, above=None):
        layers = self.__layers[:]
        layers.remove(layer)

        if above is None:
            layers.append(layer)
        else:
            idx = 1+layers.index(above)
            layers[idx:idx] = [layer]

        self.__layers = layers

    def lower(self, layer, below=None):
        layers = self.__layers[:]
        layers.remove(layer)

        if below is None:
            self.__layers = [layer]+layers
        else:
            idx = layers.index(below)
            layers[idx:idx] = [layer]
            self.__layers = layers

    def is_empty_layer(self):
        return self.__layers == []

    def get_collide_objects(self, _object):
        """Функция принимает объект, и возвращает список всех объектов пересикающихся с ним"""
        collide_list = []  # Список всех объектов пересикающихся с _object

        if not isinstance(_object, Sprite):               # Если _object не является Sprite,
            return collide_list                           # или его потомком, возвращаем пустой список

        for layer in self.__layers:                       # Перебираем все слои на сцене
            for obj in layer.get_objects():               # Перебираем все объекты в слое
                if obj is not _object:                    # Если очередной объект не _object то идём дальше
                    if isinstance(obj, Sprite):           # Если объект Sprite или его потомок, то идем дальше
                        if obj.is_collide:                # Если у объекта включена проверка пересечений, идём дальше
                            if obj.collide(_object):      # Если объект пересикаеться с _object то,
                                collide_list.append(obj)  # добавляем иго в список

        return collide_list

