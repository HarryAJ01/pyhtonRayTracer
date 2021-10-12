from colour import Colour

"""A light source at a point in the grid, a light is given a colour"""


class Light:

    # Constructor, position and colour given, default colour is white
    def __init__(self, position, colour=Colour.from_hex("#FFFFFF")):
        self.position = position
        self.colour = colour
