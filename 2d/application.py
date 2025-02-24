import turtle
from random import randrange
import random
import time
import threading

from solarsystem import SolarSystem, Sun, Planet

solar_system = SolarSystem(width = 1800, height = 800) # Set window dimensions, will change in future when implementing gui
startSimulation = False
choiceSelected = True
solarSystem = []
simulationSpeed = 0.01 # Simulation speed of 0.01 is equal to 1x speed (arbitrary units)
effectiveWidth = 1500 # Range where we spawn the planets
effectiveHeight = 750 # Here as well
minRadiusSun = 200 # Minimum distance from the Sun
# All of these only apply to the random configuration

# while not startSimulation:
#     solar_system.draw_planets()


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

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

while not startSimulation:
    firstChoice = int(input("""
1. Use default star system
2. Make custom star system
3. Use random star system
"""))

    if firstChoice == 1:
        choiceSelected = True
        solarSystem = {
            "planets": (
                Planet("", None, solar_system, 500, (50, 0), (0, 11)),
                Planet("", None, solar_system, 10, (-350, 0), (0, -10)),
                Planet("", None, solar_system, 5, (0, 200), (-2, -7)),
            ),
            "suns": (
                Sun("", solar_system, 10000, (-200, 0), (0, 3)),
                Sun("", solar_system, 10000, (200, 0), (0, -4)),
            )
        }
        break
    elif firstChoice == 3:
        choiceSelected = True
        solarSystem = {
            "planets": [
                Planet(
                    "",
                    None,
                    solar_system,
                    randrange(200, 500),
                    (  # Extra logic to ensure the planets don't spawn too close to the sun
                        randrange(int(-effectiveWidth / 2), minRadiusSun) if bool(random.getrandbits(1)) else randrange(
                            minRadiusSun, int(effectiveWidth / 2)),
                        randrange(int(-effectiveHeight / 2), minRadiusSun) if bool(
                            random.getrandbits(1)) else randrange(minRadiusSun, int(effectiveHeight / 2))),
                    (randrange(-5, 5), randrange(-5, 5))
                ) for i in range(randrange(3, 10))
            ],
            "suns": [
                Sun("", solar_system, 10000, (0, 0), (0, 0)),
            ]
        }
        break
    elif firstChoice == 2:
        templateSelected = "custom"
        while True:
            print("Current Star System:")
            for astroObject in solarSystem:
                print(f"""
=================================================
Name: {astroObject.name}
Type: {astroObject.__class__.__name__}
Mass: {astroObject.mass}
Initial Position: X: {astroObject.xcor()} | Y: {astroObject.ycor()}
Initial Velocity: X: {astroObject.velocity[0]} | Y: {astroObject.velocity[1]}
=================================================
""")

            secondChoice = int(input(f"""
1. Create Star
2. Create Planet
3. Start Simulation
4. Quit Program
"""))

            if secondChoice == 1:
                nameIn = input("Enter name (optional): ")
                while True:
                    massIn = float(input("Enter mass: "))
                    if massIn > 0: break
                    else: print("Mass must be positive")
                xIn = float(input("Enter X position: "))
                yIn = float(input("Enter Y position: "))
                xVelIn = float(input("Enter X velocity: "))
                yVelIn = float(input("Enter Y velocity: "))
                solarSystem.append(Sun(nameIn, solar_system, massIn, (xIn, yIn), (xVelIn, yVelIn)))
                continue
            elif secondChoice == 2:
                nameIn = input("Enter name (optional): ")
                while True:
                    massIn = float(input("Enter mass: "))
                    if massIn > 0: break
                    else: print("Mass must be positive")
                colorIn = get_color_input()
                xIn = float(input("Enter X position: "))
                yIn = float(input("Enter Y position: "))
                xVelIn = float(input("Enter X velocity: "))
                yVelIn = float(input("Enter Y velocity: "))
                solarSystem.append(Planet(nameIn, colorIn, solar_system, massIn, (xIn, yIn), (xVelIn, yVelIn)))
                continue
            elif secondChoice == 3:
                choiceSelected = True
                startSimulation = True
                break
            elif secondChoice == 4:
                quit()
            else:
                print("Please enter a valid option")
                continue


if choiceSelected:
    simulationSpeed = 1 / int(input("""How fast would you like to run the simulation? Default: 1
""")) * 0.01
    startSimulation = True

while startSimulation:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    time.sleep(simulationSpeed) # Simulation speed, I will set 0.01 as the default 1x Speed