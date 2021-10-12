""""A ray is a line with an origin and a normalized direction"""

class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction.normalize()