import math
import random
import turtle

def randomize_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b

class SolarSystemBody(turtle.Turtle):
    min_display_size = 20
    display_log_base = 1.1

    def __init__(
            self,
            name,
            solar_system,
            mass,
            position=(0, 0),
            velocity=(0, 0),
    ):
        super().__init__()
        self.name = "Unnamed " + self.__class__.__name__ if name == "" else name
        self.mass = mass
        self.setposition(position)
        self.velocity = velocity
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
        )

        self.penup()
        self.hideturtle()

        solar_system.add_body(self)

    def draw(self):
        self.clear()
        self.dot(int(self.display_size))

    def move(self):
        self.setx(self.xcor() + self.velocity[0])
        self.sety(self.ycor() + self.velocity[1])


class Sun(SolarSystemBody):
    def __init__(
            self,
            name,
            solar_system,
            mass,
            position=(0, 0),
            velocity=(0, 0),
    ):
        super().__init__(name, solar_system, mass, position, velocity)
        self.color("yellow")

class Planet(SolarSystemBody):

    def __init__(
            self,
            name,
            color,
            solar_system,
            mass,
            position=(0, 0),
            velocity=(0, 0),
    ):
        super().__init__(name, solar_system, mass, position, velocity)
        inputColor = randomize_color() if color is None else color
        self.color(inputColor)

class SolarSystem:
    def __init__(self, width, height):
        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0)
        self.solar_system.setup(width, height)
        self.solar_system.bgcolor("black")

        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        self.bodies.remove(body)
        body.clear()

    def update_all(self):
        for body in self.bodies:
            body.move()
            body.draw()
        self.solar_system.update()

    def draw_planets(self):
        for body in self.bodies:
            body.draw()
        self.solar_system.update()

    @staticmethod
    def accelerate_due_to_gravity(
            first: SolarSystemBody,
            second: SolarSystemBody,
    ):
        force = first.mass * second.mass / first.distance(second) ** 2
        angle = first.towards(second)
        reverse = 1
        for body in first, second:
            acceleration = force / body.mass
            acc_x = acceleration * math.cos(math.radians(angle))
            acc_y = acceleration * math.sin(math.radians(angle))
            body.velocity = (
                body.velocity[0] + (reverse * acc_x),
                body.velocity[1] + (reverse * acc_y),
            )
            reverse = -1

    def check_collision(self, first, second):
        if isinstance(first, Planet) and isinstance(second, Planet):
            return
        if isinstance(first, Sun) and isinstance(second, Sun):
            self.bodies.clear()
            print("Game Over!")
        if first.distance(second) < first.display_size / 2 + second.display_size / 2:
            for body in first, second:
                if isinstance(body, Planet):
                    self.remove_body(body)

    def calculate_all_body_interactions(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1:]:
                self.accelerate_due_to_gravity(first, second)
                self.check_collision(first, second)