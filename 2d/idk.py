from tkinter import *
from random import randrange
import random
import time
main_window=Tk()
main_window.geometry("600x600")

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
mass_scale = 0.75

error=None
speederror=None

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


def setchoice(choice):
    global startSimulation
    global choiceSelected 
    global solarSystem 
    global simulationSpeed 
    global effectiveWidth
    global effectiveHeight
    global minRadiusSun 
    #existerror=False
    if choice == 1:
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
        fstartSim(choice)
    elif choice == 2:
        for widget in main_window.winfo_children():
            widget.destroy()
        templateSelected = "custom"

        #while True:
            #print("Current Star System:")
        back=Button(main_window,text="Back",command=start)
        back.pack()
        frame1=Frame(main_window,height=300,width=150,)
        frame1.pack(side=LEFT)
        frame2=Frame(main_window,height=300,width=150,)
        frame2.pack(side=RIGHT)
        title=Label(frame2,text="Current Star System: ")
        title.pack()
        frameList=Frame(frame2)
        frameList.pack()
        if not(solarSystem==[]):
            startSim=Button(frame2,text="Start Simulation",command=lambda:fstartSim(choice))
            startSim.pack()
        
        entername=Label(frame1,text="Name: ").grid(row=0,sticky=W)
        #entername.pack(side=LEFT)
        namespace=Entry(frame1,bd=5)
        namespace.grid(row=0,column=1)
        #namespace.pack(side=RIGHT)
        entermass=Label(frame1,text="Mass: ").grid(row=1,sticky=W)
            #entermass.pack(side=LEFT)
        massspace=Entry(frame1,bd=5)
        massspace.grid(row=1,column=1)
        #massspace.pack(side=RIGHT)
        enterxpos=Label(frame1,text="X position: ").grid(row=2,sticky=W)
        #enterxpos.pack(side=LEFT)
        xposspace=Entry(frame1,bd=5)
        xposspace.grid(row=2,column=1)
           #xposspace.pack(side=RIGHT)
        enterypos=Label(frame1,text="Y position: ").grid(row=3,sticky=W)
        #enterypos.pack(side=LEFT)
        yposspace=Entry(frame1,bd=5)
        yposspace.grid(row=3,column=1)
            #yposspace.pack(side=RIGHT)
        enterxvel=Label(frame1,text="X velocity: ").grid(row=4,sticky=W)
        #enterxvel.pack(side=LEFT)
        xvelspace=Entry(frame1,bd=5)
        xvelspace.grid(row=4,column=1)
        #xvelspace.pack(side=RIGHT)
        enteryvel=Label(frame1,text="Y velocity: ").grid(row=5,sticky=W)
        #enteryvel.pack(side=LEFT)
        yvelspace=Entry(frame1,bd=5)
        yvelspace.grid(row=5,column=1)
        #yvelspace.pack(side=RIGHT)

        '''if not(solarSystem==[]):
            for astroObject in solarSystem:
                    list=Label(frameList,text=f"""
    =================================================
    Name: {astroObject.name}
    Type: {astroObject.__class__.__name__}
    Mass: {astroObject.mass}
    Initial Position: X: {astroObject.xcor()} | Y: {astroObject.ycor()}
    Initial Velocity: X: {astroObject.velocity[0]} | Y: {astroObject.velocity[1]}
    =================================================
    """)
                    list.pack()'''

        def faddstar():
            validity=False
            global error
            try: 
                nameIn = str(namespace.get())
                massIn = float(massspace.get())
                xIn = float(xposspace.get())
                yIn = float(yposspace.get())
                xVelIn = float(xvelspace.get())
                yVelIn = float(yvelspace.get())
                validity=True
                
                for astroObject in solarSystem:
                    if (xIn==astroObject.xcor() and yIn==astroObject.ycor()):
                        if error is not None:
                            error.destroy()
                        error=Label(frame1,text="Position the same as other astroObjects.")
                        error.grid(row=8)
                        validity=False
            
                if (massIn<=0):
                    if error is not None:
                        error.destroy()
                    error=Label(frame1,text="Mass is less than or equal to 0.")
                    error.grid(row=8)
                    validity=False

            except ValueError:
                if error is not None:
                    error.destroy()
                error=Label(frame1,text="Invalid input.")
                error.grid(row=8)
                existerror=True
                validity=False 

            if (validity): 
                if error is not None:
                    error.destroy()
                solarSystem.append(Sun(nameIn, solar_system, massIn, (xIn, yIn), (xVelIn, yVelIn)))
                for list in frameList.winfo_children():
                    list.destroy()
                for astroObject in solarSystem:
                    list=Label(frameList,text=f"""
    =================================================
    Name: {astroObject.name}
    Type: {astroObject.__class__.__name__}
    Mass: {astroObject.mass}
    Initial Position: X: {astroObject.xcor()} | Y: {astroObject.ycor()}
    Initial Velocity: X: {astroObject.velocity[0]} | Y: {astroObject.velocity[1]}
    =================================================
    """)
                    list.pack()
            startSim=Button(frame2,text="Start Simulation",command=lambda:fstartSim(choice))
            startSim.pack()

        def faddplanet():
            validity=False
            global error
            try: 
                nameIn = str(namespace.get())
                massIn = float(massspace.get())
                xIn = float(xposspace.get())
                yIn = float(yposspace.get())
                xVelIn = float(xvelspace.get())
                yVelIn = float(yvelspace.get())
                validity=True
                
                for astroObject in solarSystem:
                    if (xIn==astroObject.xcor() and yIn==astroObject.ycor()):
                        if error is not None:
                            error.destroy()
                        error=Label(frame1,text="Position the same as other astroObjects.")
                        error.grid(row=8)
                        validity=False
            
                if (massIn<=0):
                    if error is not None:
                        error.destroy()
                    error=Label(frame1,text="Mass is less than or equal to 0.")
                    error.grid(row=8)
                    validity=False

            except ValueError:
                if error is not None:
                    error.destroy()
                error=Label(frame1,text="Invalid input.")
                error.grid(row=8)
                existerror=True
                validity=False 

            if (validity):
                if error is not None:
                    error.destroy()
                colorIn = ""
                solarSystem.append(Planet(nameIn, colorIn, solar_system, massIn, (xIn, yIn), (xVelIn, yVelIn)))
                for list in frameList.winfo_children():
                    list.destroy()
                for astroObject in solarSystem:
                    list=Label(frameList,text=f"""
    =================================================
    Name: {astroObject.name}
    Type: {astroObject.__class__.__name__}
    Mass: {astroObject.mass}
    Initial Position: X: {astroObject.xcor()} | Y: {astroObject.ycor()}
    Initial Velocity: X: {astroObject.velocity[0]} | Y: {astroObject.velocity[1]}
    =================================================
    """)
                    list.pack()
            startSim=Button(frame2,text="Start Simulation",command=lambda:fstartSim(choice))
            startSim.pack()

        addstar=Button(frame1,text="Add as star",command=faddstar).grid(sticky=N+S+E+W)
        addplanet=Button(frame1,text="Add as Planet",command=faddplanet).grid(sticky=N+S+E+W)
        

    elif choice == 3:
        choiceSelected = True
        solarSystem = {
            "planets": [
                Planet(
                    "",
                    None,
                    solar_system,
                    randrange(int(200 * mass_scale), int(500 * mass_scale)),
                    (  # Extra logic to ensure the planets don't spawn too close to the sun
                        randrange(int(-effectiveWidth / 2), minRadiusSun) if bool(random.getrandbits(1)) else randrange(
                            minRadiusSun, int(effectiveWidth / 2)),
                        randrange(int(-effectiveHeight / 2), minRadiusSun) if bool(
                            random.getrandbits(1)) else randrange(minRadiusSun, int(effectiveHeight / 2))),
                    (randrange(-5, 5), randrange(-5, 5))
                ) for i in range(randrange(3, 10))
            ],
            "suns": [
                Sun("", solar_system, 10000 * mass_scale, (0, 0), (0, 0)),
            ]
        }
        fstartSim(choice)


def fstartSim(choice):
    global simulationSpeed
    for widget in main_window.winfo_children():
        widget.destroy()
    framespeed=Frame(main_window,height=400,width=300)
    framespeed.pack()
    LsimulationSpeed=Label(framespeed,text="How fast would you like to run the simulation? Default: 1")
    LsimulationSpeed.grid(row=0,sticky=W)
    SimulationSpeed=Entry(framespeed,bd=5)
    SimulationSpeed.grid(row=1)

    def startsimulation():
        global simulationSpeed
        global speederror
        if speederror is not None:
            speederror.destroy()
        simulationSpeed=SimulationSpeed.get()
        simulationSpeed=float(simulationSpeed)
        if (simulationSpeed<=0):
            speederror=Label(framespeed, text="Speed less than or equal to 0.")
            speederror.grid(row=3)
        else :
            while True:
                solar_system.calculate_all_body_interactions()
                solar_system.update_all()
                time.sleep(1 / int(simulationSpeed) / 100 )

    startSim=Button(framespeed,text="Start Simulation",command=startsimulation).grid(row=2)
    
    def goback(choice):
        if (choice==1 or choice==3):
            start()
        else: 
            setchoice(choice)

    back=Button(main_window,text="Back",command=lambda:goback(choice))
    back.pack()

def start():
    for widget in main_window.winfo_children():
        widget.destroy()
    default =Button(main_window,text="Default",command=lambda:setchoice(1))
    default.pack()
    custom =Button(main_window,text="Custom",command=lambda:setchoice(2))
    custom.pack()
    random =Button(main_window,text="Random",command=lambda:setchoice(3))
    random.pack()

start()
main_window.mainloop()