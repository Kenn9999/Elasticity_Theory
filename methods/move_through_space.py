from methods.move_body import move
from methods.plot_trajectory import plottr
import matplotlib.pyplot as plt
def movets(t0, t, n, x, y):
    for i in range(len(x)):
        res=move(t0, t, n, x[i], y[i])
        plottr(res.x_tr_points, res.y_tr_points)
    plt.show()