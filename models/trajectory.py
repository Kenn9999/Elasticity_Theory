class trajectory:
    x_tr_points=[]
    y_tr_points=[]

    def __init__(self, x_tr_points, y_tr_points):
        self.x_tr_points = x_tr_points
        self.y_tr_points = y_tr_points
    def __init__(self):
        self.x_tr_points = []
        self.y_tr_points = []
    def add (self,x,y):
        self.x_tr_points.append(x)
        self.y_tr_points.append(y)