from justgames.image import Image


class GameObject:
    def __init__(self, interval=1):
        self.__interval = interval  # Определяет интервал между вызовами метода tick() объекта
        self.__stopped = False      # Если True, обработка объекта остановлена
        self.__tick_count = 0       # Сколько вызовов метода _update_tick() прошло
        self.__to_destroy = False   # Если True, объект помечен на удаление

# Свойства ------------------------------------------------------------------------------------------------------------
    @property
    def stopped(self):
        return self.__stopped

    @property
    def to_destroy(self):
        return self.__to_destroy

    def get_interval(self):
        return self.__interval

    def set_interval(self, new_interval):
        self.__interval = new_interval
        self.__tick_count = 0
    interval = property(get_interval, set_interval)

# Методы --------------------------------------------------------------------------------------------------------------
    def update_tick(self):
        self.__tick_count += 1
        if self.__tick_count >= self.__interval:
            self.__tick_count = 0
            self.tick()
        self.update()

    def tick(self):
        pass

    def start(self):
        self.__stopped = False
        # self._tick_count = 0

    def stop(self):
        self.__stopped = True

    def update(self, *args):
        pass

    def draw(self):
        pass

    def destroy(self):
        self.stop()
        self.__to_destroy = True


