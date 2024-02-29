from models.space_point import Space_point
from models.space import space
import numpy as np
class streamLine:
    def __init__(self, time, x1, x2):
        self.v1 = -np.sin(time) * x1
        self.v2 = np.exp(time) * x2