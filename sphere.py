"""3D Object to be rendered, has a centre, radius and material"""
from math import sqrt


class Sphere:

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    # Checks if ray intersects this sphere. Returns distance to intersection or None if there is no intersection
    def intersects(self, ray):
        sphere_to_ray = ray.origin - self.center
        a = 1
        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.radius * self.radius
        discriminant = b * b - 4 * a * c

        if discriminant >= 0:
            distance = (-b - sqrt(discriminant)) / 2
            if distance > 0:
                return distance
        return None
    # Function to return the surface normal to the point given on spheres surface
    def normal(self, surface_point):
        return (surface_point - self.center).normalize()
