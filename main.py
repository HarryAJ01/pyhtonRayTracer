"""Python Ray Tracer by Harry Applegarth-Jones"""

from light import Light
from vector import Vector
from colour import Colour
from point import Point
from sphere import Sphere
from scene import Scene
from renderEngine import RenderEngine
from material import Material, ChequeredMaterial


def main():
    print("Rendering in progress...")
    WIDTH = 1280
    HEIGHT = 800
    camera = Vector(0, -0.35, -1)
    objects = [Sphere(Point(0.25, -0.3, -0.3), 0.2, Material(Colour.from_hex("#0000FF"))),
               Sphere(Point(-0.75, -0.55, 2.25), 0.6, Material(Colour.from_hex("#803980"))),
               Sphere(Point(0, 10000.5, 1), 10000.0, ChequeredMaterial(colour1=Colour.from_hex("#420500"),
                      colour2=Colour.from_hex("#e6b87d"), ambient=0.2))]

    lights = [Light(Point(1.5, -0.5, -10.0), Colour.from_hex("#FFFFFF")),
              Light(Point(-0.5, -10.5, 0), Colour.from_hex("#E6E6E6"))]
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    # Written in Portable Pixel Map file, this is because I can change individual pixels
    # Additionally, in human readable format
    with open("Ray_Trace_Render.ppm", "w") as img_file:
        image.write_ppm(img_file)
    print("Image Successfully Rendered")


if __name__ == "__main__":
    main()
