class Material_point:
#Задание начальных значений (временных "заглушек")
    rx = None
    ry = None

#Инициализация атрибутов класса
    def __init__(self, rx, ry):
        self.rx = rx
        self.ry = ry