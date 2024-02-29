from models.stream_line import streamLine
import matplotlib.pyplot as plt
import numpy as np


def plot_streamlines(time, min_val, max_val, skip=20):
    x_vals = np.linspace(min_val, -1, abs(min_val) * 10 + 1)
    y_vals = np.linspace(1, max_val, max_val * 10 + 1)
    x, y = np.meshgrid(x_vals, y_vals)

    s = streamLine(time, x, y)

    x_decimated = x[::skip, ::skip]
    y_decimated = y[::skip, ::skip]
    v1_decimated = s.v1[::skip, ::skip]
    v2_decimated = s.v2[::skip, ::skip]

    plt.figure(figsize=(10, 6))
    plt.streamplot(x, y, s.v1, s.v2, density=1, color='red')
    plt.quiver(x_decimated, y_decimated, v1_decimated, v2_decimated, scale=100)
    plt.title(f'time = {time}')
    plt.xlim(min_val, 0)
    plt.ylim(0, max_val)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.show()