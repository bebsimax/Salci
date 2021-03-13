class Vector():
    def __init__(self, start, end):
        if len(end) == 2:
            self.x_start = start[0]
            self.y_start = start[1]
            self.x_end = end[0]
            self.y_end = end[1]
            self.length = ((self.x_end-self.x_start)**2+(self.y_end-self.y_start)**2)**0.5
        #else:
            #TODO alternate constructor

    def __repr__(self):
        return "Vector:[{},{}],[{},{}]".format(self.x_start, self.y_start, self.x_end, self.y_end)

    def __mul__(self, other):
        return Vector([self.x_start*other, self.y_start*other], [self.x_end*other, self.y_end*other])

    def __rmul__(self, other):
        return Vector([self.x_start * other, self.y_start * other], [self.x_end * other, self.y_end * other])


v = Vector([0,0], [1,1])

a = v*3
print(a)

