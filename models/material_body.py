class Material_body:
#Задание начальных значений (временных "заглушек")
    rx = None
    ry = None
    ang = None

#Инициализация атрибутов класса
    def __init__(self, rx, ry, ang):
        self.rx = rx
        self.ry = ry
        self.ang = ang