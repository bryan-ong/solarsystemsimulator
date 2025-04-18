import itertools
import math
import random

import matplotlib.pyplot as plt
from vectors import Vector

class SolarSystem:
    def __init__(self, size, projection_2d = False):
        self.size = size
        self.projection_2d = projection_2d
        self.bodies = []

        self.fig, self.ax = plt.subplots(
            1,
            1,
            subplot_kw = {"projection": "3d"},
            figsize = (self.size / 50, self.size / 50)
        )
        self.fig.tight_layout()
        if self.projection_2d:
            self.ax.view_init(90, 0)
        else:
            self.ax.view_init(90, 0)

    def check_collision(self, first, second):
        distance_vector = Vector(*first.position) - Vector(*second.position)
        distance = distance_vector.get_magnitude()
        collision_threshold = (first.display_size / 2) + (second.display_size / 2)

        if distance < collision_threshold:
            # Handle collisions between two Suns
            if isinstance(first, Sun) and isinstance(second, Sun):
                print("Two suns collided! Game Over!")
                self.bodies.clear() # Clear all bodies in the solar system
                return

            # Handle collisions between a Sun and a Planet
            elif isinstance(first, Sun) != isinstance(second, Sun):
                # Remove the Planet if it collides with the Sun
                if isinstance(first, Planet):
                    self.remove_body(first)
                    print(f"A planet named '{first.name}' collided with the sun and was destroyed!")
                elif isinstance(second, Planet):
                    self.remove_body(second)
                    print(f"A planet named '{second.name}' collided with the sun and was destroyed!")

    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        self.bodies.remove(body)

    def update_all(self):
        self.bodies.sort(key=lambda item: item.position[0])
        for body in self.bodies:
            body.move()
            body.draw()

    def draw_all(self):
        self.ax.set_xlim((-self.size / 2, self.size / 2))
        self.ax.set_ylim((-self.size / 2, self.size / 2))
        self.ax.set_zlim((-self.size / 2, self.size / 2))
        if self.projection_2d:
            self.ax.xaxis.set_ticklabels([])
            self.ax.yaxis.set_ticklabels([])
            self.ax.zaxis.set_ticklabels([])
        else:
            self.ax.axis(True)
        plt.pause(0.0001)
        self.ax.clear()

    def calculate_all_body_interactions(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1:]:
                first.accelerate_due_to_gravity(second)
                self.check_collision(first, second)

class SolarSystemBody:
    min_display_size = 10 # Ensure not too small, but not too big
    display_log_base = 1.3

    def __init__(
            self,
            name,
            solar_system,
            mass,
            position=(0, 0, 0),
            velocity=(0, 0, 0),
    ):
        self.name = "Unnamed " + self.__class__.__name__ if name == "" else name
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
        self.solar_system.add_body(self)
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
        )
        self.colour = "black"

    def move(self):
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
            self.position[2] + self.velocity[2],
        )


    def draw(self):
        self.solar_system.ax.plot(
            *self.position,
            marker="o",
            markersize=self.display_size + self.position[0] / 30,
            color=self.colour
        )
        if self.solar_system.projection_2d:
            self.solar_system.ax.plot(
                self.position[0],
                self.position[1],
                -self.solar_system.size / 2,
                marker="o",
                markersize=self.display_size / 2,
                color=(.5, .5, .5),
                )

    def accelerate_due_to_gravity(self, other):
        distance = Vector(*other.position) - Vector(*self.position)
        distance_mag = distance.get_magnitude()
        if distance_mag == 0:
            return  # Avoid division by zero
        force_mag = self.mass * other.mass / (distance_mag ** 2)
        force = distance.normalize() * force_mag
        reverse = 1
        for body in self, other:
            acceleration = force / body.mass
            body.velocity += acceleration * reverse
            # Limit velocity to prevent unrealistic behavior
            max_velocity = 20
            if body.velocity.get_magnitude() > max_velocity:
                body.velocity = body.velocity.normalize() * max_velocity
            reverse = -1

class Sun(SolarSystemBody):
    def __init__(
            self,
            name,
            solar_system,
            mass=10_000,
            position=(0, 0, 0),
            velocity=(0, 0, 0),
    ):
        super(Sun, self).__init__(name, solar_system, mass, position, velocity)
        self.colour = "yellow"


class Planet(SolarSystemBody):
    def __init__(
            self,
            name,
            color,
            solar_system,
            mass=10,
            position=(0, 0, 0),
            velocity=(0, 0, 0),
    ):
        super(Planet, self).__init__(name, solar_system, mass, position, velocity)
        self.colour = randomize_color() if color is None else color

def randomize_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b