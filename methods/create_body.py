import math
def create_body(n):
    mbpx = []
    mbpy = []
    xc, yc = -2, 2  # Центр круга
    radius = 1  # Радиус круга
    for i in range(n):
        angle = 2 * math.pi * i / n
        x = xc + radius * math.cos(angle)
        y = yc + radius * math.sin(angle)
        mbpx.append(x)
        mbpy.append(y)
    # Добавляем первую точку еще раз, чтобы замкнуть круг
    mbpx.append(mbpx[0])
    mbpy.append(mbpy[0])
    return mbpx, mbpy