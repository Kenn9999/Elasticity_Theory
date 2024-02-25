class Trajectory:
    x_trajectory_points = []
    y_trajectory_points = []

    def __init__(self, x_trajectory_points, y_trajectory_points):
        self.x_trajectory_points = x_trajectory_points
        self.y_trajectory_points = y_trajectory_points
    def __init__(self):
        self.x_trajectory_points = []
        self.y_trajectory_points = []
    def add(self, x, y):
        self.x_trajectory_points.append(x)
        self.y_trajectory_points.append(y)
