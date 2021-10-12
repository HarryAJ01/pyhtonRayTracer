from colour import Colour
from image import Image
from point import Point
from ray import Ray

"""Renders a 3D object into a 2D object using ray tracing"""


class RenderEngine:

    MAX_DEPTH = 5
    MIN_DISPLACE = 0.0001

    def render(self, scene):
        width = scene.width
        height = scene.height
        aspect_ratio = float(width) / height

        x0 = - 1.0
        x1 = 1.0
        x_distance = (x1 - x0) / (width - 1)

        y0 = - 1.0 / aspect_ratio
        y1 = 1.0 / aspect_ratio
        y_distance = (y1 - y0) / (height - 1)

        camera = scene.camera
        pixels = Image(width, height)

        for l in range(height):
            y = y0 + l * y_distance
            for i in range(width):
                x = x0 + i * x_distance
                ray = Ray(camera, Point(x, y) - camera)
                pixels.set_pixel(i, l, self.ray_trace(ray, scene))
        return pixels

    def ray_trace(self, ray, scene, depth =0):
        colour = Colour(0, 0, 0)

        # Find nearest object hit by ray
        distance_hit, object_hit = self.find_nearest(ray, scene)
        if object_hit is None:
            return colour
        hit_position = ray.origin + ray.direction * distance_hit
        hit_normal = object_hit.normal(hit_position)
        colour += self.colour_at_position(object_hit, hit_position, hit_normal, scene)

        # Reflection
        if depth < self.MAX_DEPTH:
            new_ray_position = hit_position + hit_normal * self.MIN_DISPLACE
            new_ray_direction = ray.direction - 2 * ray.direction.dot_product(hit_normal) * hit_normal
            new_ray = Ray(new_ray_position, new_ray_direction)

            # Attenuate the reflected ray by reflection coefficient
            colour += self.ray_trace(new_ray, scene, depth + 1) * object_hit.material.reflection

        return colour

    def find_nearest(self, ray, scene):
        distance_minimum = None
        object_hit = None
        for obj in scene.objects:
            dist = obj.intersects(ray)
            if dist is not None and (object_hit is None or dist < distance_minimum):
                distance_minimum = dist
                object_hit = obj
        return (distance_minimum, object_hit)

    def colour_at_position(self, object_hit, hit_position, normal, scene):
        material = object_hit.material
        object_colour = material.colour_at_position(hit_position)
        distance_to_camera = scene.camera - hit_position
        colour = material.ambient * Colour.from_hex("#000000")
        specular_k = 50

        # Calculations for the light
        for light in scene.lights:
            distance_to_light = Ray(hit_position, light.position - hit_position)

            # Diffuse Shading (Lambert)
            colour += object_colour * material.diffuse * max(normal.dot_product(distance_to_light.direction), 0)

            # Specular Shading (Blinn - Phong)
            half_vector = (distance_to_light.direction + distance_to_camera).normalize()
            colour += light.colour * material.specular * max(normal.dot_product(half_vector), 0) ** specular_k

        return colour
