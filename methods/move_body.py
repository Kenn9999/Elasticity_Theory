from models.trajectory import trajectory
from methods.runge_kutta import rungekutta
def move(t0, t, n, x0, y0):
    h = t/n
    tr = trajectory()
    prx = x0
    pry = y0
    for i in range(n):
        x, y = rungekutta(t0 + h * i, h, prx, pry)
        tr.add(x, y)
        prx = x
        pry = y
    return tr
