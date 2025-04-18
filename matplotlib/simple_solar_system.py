def get_color_input():
    color_input = input("Enter color (leave blank for random color) [r g b] 0-255: ")
    if color_input.strip() == "":
        return None
    else:
        try:
            r, g, b = map(float, color_input.split())
            return r / 255, g / 255, b / 255
        except (ValueError, TypeError):
            print("Invalid color input. Please enter three numbers for RGB.")
            return get_color_input()

from solar_system_3d import SolarSystem, Sun, Planet

solar_system = SolarSystem(400)

sun = Sun(
    name="Sun",
    solar_system=solar_system,
    mass=10000,
    position=(0, 0, 0),
    velocity=(0, 0, 0)
)

mercury = Planet(
    name="Mercury",
    color=(0.7, 0.5, 0.2),
    solar_system=solar_system,
    mass=150,
    position=(20, 20, 20),
    velocity=(25, 25, 0)
)
#
# venus = Planet(
#     name="Venus",
#     color=(0.9, 0.6, 0.1),
#     solar_system=solar_system,
#     mass=48.7,
#     position=(70, 0, 70),
#     velocity=(0, 3.5, 0)
# )
#
# earth = Planet(
#     name="Earth",
#     color=(0, 0, 1),
#     solar_system=solar_system,
#     mass=50,
#     position=(100, 0, 100),
#     velocity=(0, 3, 0)
# )
#
# mars = Planet(
#     name="Mars",
#     color=(0.8, 0.2, 0.1),
#     solar_system=solar_system,
#     mass=10,
#     position=(150, 150, 0),
#     velocity=(0, 2.4, 0)
# )
#
# jupiter = Planet(
#     name="Jupiter",
#     color=(0.8, 0.6, 0.4),
#     solar_system=solar_system,
#     mass=500,
#     position=(0, 500, 0),
#     velocity=(0, 1.3, 0)
# )
#
# saturn = Planet(
#     name="Saturn",
#     color=(0.9, 0.8, 0.5),
#     solar_system=solar_system,
#     mass=200,
#     position=(900, 0, 900),
#     velocity=(0, 0.9, 0)
# )
#
# uranus = Planet(
#     name="Uranus",
#     color=(0.4, 0.6, 0.8),
#     solar_system=solar_system,
#     mass=100,
#     position=(1800, 1800, 0),
#     velocity=(0, 0.7, 0)
# )
#
# neptune = Planet(
#     name="Neptune",
#     color=(0.2, 0.3, 0.9),
#     solar_system=solar_system,
#     mass=90,
#     position=(0, 2800, 2800),
#     velocity=(0, 0.5, 0)
# )

while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.draw_all()
