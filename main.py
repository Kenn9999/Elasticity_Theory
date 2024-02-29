from methods.move_through_space import movets
from methods.create_body import create_body
from methods.plot_streamlines import plot_streamlines
import matplotlib.pyplot as plt
import numpy as np

mbpx, mbpy = create_body(100)
plt.plot(mbpx,mbpy)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()
movets(0.1, 1, 25, mbpx, mbpy)

for t in np.arange(0.1, 1, 0.1):
    plot_streamlines(t, -10,10)