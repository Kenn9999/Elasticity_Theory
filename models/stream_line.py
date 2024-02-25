#from models.space_point import SpacePoint
#from models.space import space
import numpy as np

class StreamLine:
    def __init__(self, time, x1, x2):
        self.v1 = np.sin(time) * x1
        self.v2 = np.exp(time) * x2