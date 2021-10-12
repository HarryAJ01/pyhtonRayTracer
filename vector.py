import math


class Vector:

    """"Class to represent a 3D vector with the necessary operations"""

    # Default Constructor, values stored as floats initially
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    # Function to find the dot product between this vector and a given Vector
    def dot_product(self, inVector):
        return (self.x * inVector.x) + (self.y * inVector.y) + (self.z * inVector.z)

    # Function to find the magnitude of this vector
    def magnitude(self):
        return math.sqrt(self.dot_product(self))

    # Adjusting the magnitude to find the direction of travel for this vector
    def normalize(self):
        return self / self.magnitude()

    # Overloading Operators for Vector Calculations

    def __add__(self, inVector):
        return Vector(self.x + inVector.x, self.y + inVector.y, self.z + inVector.z)

    def __sub__(self, inVector):
        return Vector(self.x - inVector.x, self.y - inVector.y, self.z - inVector.z)

    def __mul__(self, inVector):
        assert not isinstance(inVector, Vector)
        return Vector(self.x * inVector, self.y * inVector, self.z * inVector)

    def __rmul__(self, inVector):
        return self.__mul__(inVector)

    def __truediv__(self, inVector):
        assert not isinstance(inVector, Vector)
        return Vector(self.x / inVector, self.y / inVector, self.z / inVector)

    # Returns a string representation of the vector
    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)
