import math
def rungekutta(t0, dt, x0, y0):
    kx1 = -math.sin(t0) * x0
    kx2 = -math.sin(t0 + dt) * (x0 + dt * kx1)
    x1 = x0 + dt * (kx1 / 2 + kx2 / 2)

    ky1 = math.exp(t0) * y0
    ky2 = math.exp(t0 + dt) * (y0 + dt * ky1)
    y1 = y0 + dt * (ky1 / 2 + ky2 / 2)

    return x1, y1