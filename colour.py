from vector import Vector


"""Using the Vector Operations to represent a colour, stored in RGB dimentions"""

class Colour(Vector):

    @classmethod
    def from_hex(cls, hexcolour="#000000"):
        r = int(hexcolour[1:3], 16) / 255.0
        g = int(hexcolour[3:5], 16) / 255.0
        b = int(hexcolour[5:7], 16) / 255.0
        return cls(r, g, b)