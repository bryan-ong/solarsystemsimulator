# binary_star_system.py

def get_color_input():
    color_input = input("Enter color (leave blank for random color) [r g b] 0-255: ") # Input should be 3 numbers with no spaces
    if color_input.strip() == "": # We return none if blank
        return None
    else:
        try:
            r, g, b = map(float, color_input.split())
            return r / 255, g / 255, b / 255  # Normalize to 1.0F as that's what turtle.color() uses
        except (ValueError, TypeError):
            print("Invalid color input. Please enter three numbers for RGB.")
            return get_color_input()

from solar_system_3d import SolarSystem, Sun, Planet

solar_system = SolarSystem(400)

suns = (
    Sun(
        name="",
        solar_system=solar_system,
        position=(50, 50, 50),
        velocity=(3, 0, 3)),
    Sun("", solar_system, position=(-50, -50, 50), velocity=(-3, 0, -3)),
)


planets = Planet(
    name="Earth",
    color=(0, 0, 1),
    solar_system=solar_system,
    mass=10,
    position=(100, 0, 0),
    velocity=(0, 1, 0)
)

while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.draw_all()
