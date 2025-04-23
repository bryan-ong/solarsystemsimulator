from turtle import Turtle
from customtkinter import *
from tkinter import *
from PIL import Image
from const import *
from solarsystem import *
import time
from random import *

from solarsystem import SolarSystem, Sun, Planet

set_appearance_mode("dark")
set_default_color_theme("dark-blue")


# solar_system = SolarSystem(width = 1800, height = 800) # Set window dimensions, will change in future when implementing gui
startSimulation = False
choiceSelected = True
solarSystem = []
simulationSpeed = 0.01 # Simulation speed of 0.01 is equal to 1x speed (arbitrary units)
effectiveWidth = 1500 # Range where we spawn the planets
effectiveHeight = 750 # Here as well
minRadiusSun = BUTTON_SIZE # Minimum distance from the Sun
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

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Gravision")
        self.geometry(str(SCR_WIDTH) + "x" + str(SCR_HEIGHT))
        self.menu = Menu(self)
        self.simulation = Simulation(self)
        self.theory = Theory(self)
        self.default = Default(self)
        self.custom = Custom(self)
        self.random = Random(self)

        self.show_page(self.menu)

    def show_page(self, page):
        page.tkraise()

    def close_windows(self):
        self.destroy()


class Menu(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.place(relwidth=1, relheight=1)

        bg_img = Image.open("../assets/bg.jpg")
        bg_lbl = CTkLabel(self, image=CTkImage(light_image=bg_img, dark_image=bg_img, size=(SCR_WIDTH, SCR_HEIGHT)))
        bg_lbl.place(x=0, y=0)

        label = CTkButton(master=self, text="GRAVISION", font=("BRLNSDB", 96), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG,
                          border_color=WISTERIA, border_width=5,
                          width=SCR_WIDTH + 100, height=SCR_HEIGHT / 8)

        label.place(relx=0.5, rely=0.3, anchor="center")

        sim_btn = CTkButton(master=self, text="Simulate", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                            bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                            border_width=5, height=75, width=BUTTON_SIZE,
                            command=lambda: master.show_page(master.simulation))
        theory_btn = CTkButton(master=self, text="Theory", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                               bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                               border_width=5, height=75, width=BUTTON_SIZE,
                               command=lambda: master.show_page(master.theory))
        exit_btn = CTkButton(master=self, text="Exit", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                             border_width=5, height=75, width=BUTTON_SIZE, command=lambda: master.close_windows())

        sim_btn.place(relx=0.5, rely=0.5, anchor="center")
        theory_btn.place(relx=0.5, rely=0.6, anchor="center")
        exit_btn.place(relx=0.5, rely=0.7, anchor="center")


class Simulation(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.place(relwidth=1, relheight=1)
        bg_img = Image.open("../assets/bg.jpg")
        bg_lbl = CTkLabel(self, text="",
                          image=CTkImage(light_image=bg_img, dark_image=bg_img, size=(SCR_WIDTH, SCR_HEIGHT)))
        bg_lbl.place(x=0, y=0)

        title = CTkButton(master=self, text="SIMULATE", font=("BRLNSDB", 96), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG,
                          border_color=WISTERIA, border_width=5,
                          width=SCR_WIDTH + 100, height=SCR_HEIGHT / 8)

        title.place(relx=0.5, rely=0.3, anchor="center", )

        default_btn = CTkButton(master=self, text="Default Preset", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                                bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA,
                                border_color=WISTERIA,
                                border_width=5, height=75, width=BUTTON_SIZE,
                                command=lambda: master.show_page(master.default))

        default_btn.place(relx=0.5, rely=0.5, anchor="center")

        custom_btn = CTkButton(master=self, text="Custom", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                               bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                               border_width=5, height=75, width=BUTTON_SIZE,
                               command=lambda: master.show_page(master.custom))

        custom_btn.place(relx=0.5, rely=0.6, anchor="center")

        random_btn = CTkButton(master=self, text="Randomize", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                               bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                               border_width=5, height=75, width=BUTTON_SIZE,
                               command=lambda: master.show_page(master.random))

        random_btn.place(relx=0.5, rely=0.7, anchor="center")

        back_btn = CTkButton(master=self, text="Back to Menu", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                             border_width=5, height=75, width=BUTTON_SIZE,
                             command=lambda: master.show_page(master.menu))

        back_btn.place(relx=0.5, rely=0.8, anchor="center")


class Theory(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.place(relwidth=1, relheight=1)
        bg_img = Image.open("../assets/bg.jpg")
        bg_lbl = CTkLabel(self, text="",
                          image=CTkImage(light_image=bg_img, dark_image=bg_img, size=(SCR_WIDTH, SCR_HEIGHT)))
        bg_lbl.place(x=0, y=0)

        title = CTkButton(master=self, text="THEORY", font=("BRLNSDB", 96), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG,
                          border_color=WISTERIA, border_width=5,
                          width=SCR_WIDTH + 100, height=SCR_HEIGHT / 8)

        title.place(relx=0.5, rely=0.25, anchor="center")

        explanation = CTkButton(master=self,
                                text="""In space, objects usually move with a constant velocity. 
However, its moving direction might be affected when another object comes near. 
This is because every object with mass has its own gravity. When two objects meet each other, 
they will be attracted to each other and cause their direction to change. If their velocity is high enough, 
they will soon move away from each other, although their direction may have changed a little too. 
However, if their velocity isn’t high enough, they might end up crashing into each other. 
When one of the object’s mass is way higher than the other, 
it might crash with the object with a much lower mass without much change in its moving direction 
as the higher the mass of an object is, the higher the gravity it has. 
In the end, the object with a much lower mass might disappear while the object with a much higher mass won’t.""",
                                fg_color="transparent",
                                bg_color=SWEET_FLAG,
                                height=300, width=1400,
                                border_color=WISTERIA,
                                hover_color=SWEET_FLAG,
                                border_width=5,
                                font=CTkFont(family='Inter', size=24),
                                text_color=(CANDY_DREAMS, CANDY_DREAMS),
                                )
        explanation.place(relx=0.5, rely=0.5, anchor="center")

        back_btn = CTkButton(master=self, text="Back to Menu", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                             border_width=5, height=75, width=BUTTON_SIZE,
                             command=lambda: master.show_page(master.menu))

        back_btn.place(relx=0.1, rely=0.1, anchor="center")

        explanation_img = Image.open("../assets/explanation.png")
        explanation_lbl = CTkButton(self, text="", bg_color=WISTERIA, hover_color=WISTERIA, fg_color="transparent", border_color=CANDY_DREAMS,
                                    border_width= 5, width=420, height=270, corner_radius=5,
                                    image=CTkImage(light_image=explanation_img, dark_image=explanation_img, size=(400, 250)))
        explanation_lbl.place(x=(SCR_WIDTH // 2 - 200), rely=0.7)

class Default(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.place(relwidth=1, relheight=1)

        bg_img = Image.open("../assets/bg.jpg")
        bg_lbl = CTkLabel(self, text="",
                          image=CTkImage(light_image=bg_img, dark_image=bg_img, size=(SCR_WIDTH, SCR_HEIGHT)))
        bg_lbl.place(x=0, y=0)

        title = CTkButton(master=self, text="DEFAULT", font=("BRLNSDB", 96), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG,
                          border_color=WISTERIA, border_width=5,
                          width=SCR_WIDTH + 100, height=SCR_HEIGHT / 8)

        title.place(relx=0.5, rely=0.3, anchor="center")

        back_btn = CTkButton(master=self, text="Back to Simulate", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                             border_width=5, height=75, width=BUTTON_SIZE,
                             command=lambda: master.show_page(master.simulation))

        back_btn.place(relx=0.1, rely=0.1, anchor="center")

        label = CTkButton(master=self,
                                text="""Generates a solar system using the default preset.
How fast would you like to run the simulation? Leave blank for default: 1""",
                                fg_color="transparent",
                                bg_color=SWEET_FLAG,
                                border_color=WISTERIA,
                                hover_color=SWEET_FLAG,
                                border_width=5,
                                font=CTkFont(family='Inter', size=24),
                                text_color=(CANDY_DREAMS, CANDY_DREAMS),
                                )

        label.place(relx=0.5, rely=0.5, anchor="center")

        sim_speed = CTkEntry(master=self, font=("BRLNSDB", 64), text_color=CANDY_DREAMS,
                             bg_color=PURPLE, fg_color="transparent", border_color=WISTERIA, justify="center",
                             border_width=5, height=75, width=BUTTON_SIZE)

        sim_speed.place(relx=0.5, rely=0.6, anchor="center")

        def finalstartsim():
            solar_system = SolarSystem(width = 1800, height = 800) # Set window dimensions, will change in future when implementing gui

            global simulationSpeed
            global speederror
            if speederror is not None:
                speederror.destroy()
            simulationSpeed=sim_speed.get()
            simulationSpeed=float(simulationSpeed)
            if (simulationSpeed<=0):
                speederror=Label(master=self, text="Speed less than or equal to 0.")
                speederror.grid(row=3)
            else :
                while True:
                    # print("pikachu")
                    solar_system.calculate_all_body_interactions()
                    solar_system.update_all()
                    time.sleep(1 / simulationSpeed / 100 )

        start_btn = CTkButton(master=self, text="Start Simulation", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                             border_width=5, height=75, width=BUTTON_SIZE,
                             command=finalstartsim)

        start_btn.place(relx=0.5, rely=0.7, anchor="center")


class Custom(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.place(relwidth=1, relheight=1)

        bg_img = Image.open("../assets/bg.jpg")
        bg_lbl = CTkLabel(self, text="",
                          image=CTkImage(light_image=bg_img, dark_image=bg_img, size=(SCR_WIDTH, SCR_HEIGHT)))
        bg_lbl.place(x=0, y=0)

        label = CTkButton(master=self,
                          text="Add Celestial Bodies", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                          border_width=5, height=75, width=BUTTON_SIZE * 3)

        label.place(relx=0.225, rely=0.2, anchor="center")

        label = CTkButton(master=self,
                         text="List of Bodies",
                         font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                         bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                         border_width=5, height=75, width=BUTTON_SIZE)

        label.place(relx=0.75, rely=0.15, anchor="center")

        list = CTkButton(master=self, text="", bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                          border_width=5, height=SCR_HEIGHT // 2, width=BUTTON_SIZE * 3)
        list.place(relx=0.75, rely=0.5, anchor="center")

        start_btn = CTkButton(master=self,
                                   text="Start Simulation", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                                   bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                                   border_width=5, height=75, width=BUTTON_SIZE,
                                   # command=lambda:master.show_page(master.menu)
                                   )

        start_btn.place(relx=0.75,
                             rely=0.9,
                             anchor="center")

        back_btn = CTkButton(master=self, text="Back to Simulate", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                             border_width=5, height=75, width=BUTTON_SIZE,
                             command=lambda: master.show_page(master.simulation))

        back_btn.place(relx=0.1, rely=0.1, anchor="center")

        add_planet_btn = CTkButton(master=self,
                                   text="Add as Planet", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                                   bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                                   border_width=5, height=75, width=BUTTON_SIZE,
                                   # command=lambda:master.show_page(master.menu)
                                   )

        add_planet_btn.place(relx=0.2,
                             rely=0.9,
                             anchor="center")

        add_star_btn = CTkButton(master=self,
                                 text="Add as Star", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                                 bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                                 border_width=5, height=75, width=BUTTON_SIZE,
                                 # command=lambda:master.show_page(master.menu)
                                 )
        add_star_btn.place(relx=0.33,
                           rely=0.9,
                           anchor="center", )

        label = CTkButton(master=self,
                         text="Name: ", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                         bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                         border_width=5, height=75, width=BUTTON_SIZE,
                         )
        label.place(relx=0.1,
                    rely=0.3,
                    anchor="center", )

        name = CTkEntry(master=self, font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=PURPLE, fg_color="transparent", border_color=WISTERIA, justify="center",
                             border_width=5, height=75, width=BUTTON_SIZE * 1.5)

        name.place(relx=0.3,
                   rely=0.3,
                   anchor="center")

        label = CTkButton(master=self,
                         text="Mass: ", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                         bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                         border_width=5, height=75, width=BUTTON_SIZE,
                         )
        label.place(relx=0.1,
                    rely=0.4,
                    anchor="center", )
        varmass = IntVar()
        mass = CTkSlider(master=self,
                         bg_color=WISTERIA, width=BUTTON_SIZE * 1.5, height=20, fg_color=SWEET_FLAG, corner_radius=1, button_color=LILAC, button_hover_color="white", progress_color=PURPLE,
                         from_=0, to=1000,
                         variable=varmass)
        mass.place(relx=0.3,
                   rely=0.4,
                   anchor="center", )
        value = CTkButton(self, textvariable=varmass, font=("BRLNSDB", 24), text_color=CANDY_DREAMS,
                         bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                         border_width=5, height=75, width=75)
        value.place(relx=0.43,
                    rely=0.4,
                    anchor="center", )

        label = CTkButton(master=self,
                         text="Initial X-vel: ", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                         bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                         border_width=5, height=75, width=BUTTON_SIZE,
                         )
        label.place(relx=0.1,
                    rely=0.5,
                    anchor="center", )
        varx_velo = IntVar()
        x_velo = CTkSlider(master=self,
                           bg_color=WISTERIA, width=BUTTON_SIZE * 1.5, height=20, fg_color=SWEET_FLAG, corner_radius=1, button_color=LILAC, button_hover_color="white", progress_color=PURPLE,
                           from_=0, to=1000,
                           variable=varx_velo)
        x_velo.place(relx=0.3,
                     rely=0.5,
                     anchor="center", )
        value = CTkButton(self, textvariable=varx_velo, font=("BRLNSDB", 24), text_color=CANDY_DREAMS,
                         bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                         border_width=5, height=75, width=75)
        value.place(relx=0.43,
                    rely=0.5,
                    anchor="center", )

        label = CTkButton(master=self,
                         text="Initial Y-vel: ", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                         bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                         border_width=5, height=75, width=BUTTON_SIZE)

        label.place(relx=0.1,
                    rely=0.6,
                    anchor="center")

        vary_velo = IntVar()
        y_velo = CTkSlider(master=self,
                           bg_color=WISTERIA, width=BUTTON_SIZE * 1.5, height=20, fg_color=SWEET_FLAG, corner_radius=1, button_color=LILAC, button_hover_color="white", progress_color=PURPLE,
                           from_=0, to=1000,
                           variable=vary_velo)
        y_velo.place(relx=0.3,
                     rely=0.6,
                     anchor="center", )
        value = CTkButton(self, textvariable=vary_velo, font=("BRLNSDB", 24), text_color=CANDY_DREAMS,
                         bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                         border_width=5, height=75, width=75)
        value.place(relx=0.43,
                    rely=0.6,
                    anchor="center", )

        label = CTkButton(master=self,
                         text="Initial X-pos: ", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                         bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                         border_width=5, height=75, width=BUTTON_SIZE)

        label.place(relx=0.1,
                    rely=0.7,
                    anchor="center", )

        varx_pos = IntVar()
        x_pos = CTkSlider(master=self,
                          bg_color=WISTERIA, width=BUTTON_SIZE * 1.5, height=20, fg_color=SWEET_FLAG, corner_radius=1, button_color=LILAC, button_hover_color="white", progress_color=PURPLE,
                          from_=0, to=1000,
                          variable=varx_pos)
        x_pos.place(relx=0.3,
                    rely=0.7,
                    anchor="center", )
        value = CTkButton(self, textvariable=varx_pos, font=("BRLNSDB", 24), text_color=CANDY_DREAMS,
                         bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                         border_width=5, height=75, width=75)
        value.place(relx=0.43,
                    rely=0.7,
                    anchor="center", )

        label = CTkButton(master=self,
                          text="Initial Y-pos: ", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                          border_width=5, height=75, width=BUTTON_SIZE,
                          )
        label.place(relx=0.1,
                    rely=0.8,
                    anchor="center", )
        vary_pos = IntVar()
        y_pos = CTkSlider(master=self,
                          bg_color=WISTERIA, width=BUTTON_SIZE * 1.5, height=20, fg_color=SWEET_FLAG, corner_radius=1,
                          button_color=LILAC, button_hover_color="white", progress_color=PURPLE,
                          from_=0, to=1000,
                          variable=vary_pos)
        y_pos.place(relx=0.3,
                    rely=0.8,
                    anchor="center", )
        value = CTkButton(self, textvariable=vary_pos, font=("BRLNSDB", 24), text_color=CANDY_DREAMS,
                         bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                         border_width=5, height=75, width=75)
        value.place(relx=0.43,
                    rely=0.8,
                    anchor="center")



    #     '''if not(solarSystem==[]):
    #         for astroObject in solarSystem:
    #                 list=Label(frameList,text=f"""
    # =================================================
    # Name: {astroObject.name}
    # Type: {astroObject.__class__.__name__}
    # Mass: {astroObject.mass}
    # Initial Position: X: {astroObject.xcor()} | Y: {astroObject.ycor()}
    # Initial Velocity: X: {astroObject.velocity[0]} | Y: {astroObject.velocity[1]}
    # =================================================
    # """)
    #                 list.pack()'''

    # def faddstar():
    #     validity=False
    #     global error
    #     try:
    #         nameIn = str(name.get())
    #         massIn = float(mass.get())
    #         xIn = float(x_velo.get())
    #         yIn = float(y_velo.get())
    #         # xVelIn = float(xvelspace.get())
    #         # yVelIn = float(yvelspace.get())
    #         validity=True


class Random(CTkFrame):
    # solarSystem = {
    #     "planets": [
    #         Planet(
    #             "",
    #             None,
    #             solarSystem,
    #             randrange(200, 500),
    #             (  # Extra logic to ensure the planets don't spawn too close to the sun
    #                 randrange(int(-effectiveWidth / 2), minRadiusSun) if bool(random.getrandbits(1)) else randrange(
    #                     minRadiusSun, int(effectiveWidth / 2)),
    #                 randrange(int(-effectiveHeight / 2), minRadiusSun) if bool(
    #                     random.getrandbits(1)) else randrange(minRadiusSun, int(effectiveHeight / 2))),
    #             (randrange(-5, 5), randrange(-5, 5))
    #         ) for i in range(randrange(3, 10))
    #     ],
    #     "suns": [
    #         Sun("", solar_system, 10000, (0, 0), (0, 0)),
    #     ]
    # }
    def __init__(self, master):
        super().__init__(master)
        self.place(relwidth=1, relheight=1)

        bg_img = Image.open("../assets/bg.jpg")
        bg_lbl = CTkLabel(self, text="",
                          image=CTkImage(light_image=bg_img, dark_image=bg_img, size=(SCR_WIDTH, SCR_HEIGHT)))
        bg_lbl.place(x=0, y=0)

        title = CTkButton(master=self, text="DEFAULT", font=("BRLNSDB", 96), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG,
                          border_color=WISTERIA, border_width=5,
                          width=SCR_WIDTH + 100, height=SCR_HEIGHT / 8)

        title.place(relx=0.5, rely=0.3, anchor="center")

        back_btn = CTkButton(master=self, text="Back to Simulate", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                             border_width=5, height=75, width=BUTTON_SIZE,
                             command=lambda: master.show_page(master.simulation))

        back_btn.place(relx=0.1, rely=0.1, anchor="center")

        label = CTkButton(master=self,
                          text="""Generates a solar system using randomized values.
    How fast would you like to run the simulation? Leave blank for default: 1""",
                          fg_color="transparent",
                          bg_color=SWEET_FLAG,
                          border_color=WISTERIA,
                          hover_color=SWEET_FLAG,
                          border_width=5,
                          font=CTkFont(family='Inter', size=24),
                          text_color=(CANDY_DREAMS, CANDY_DREAMS),
                          )

        label.place(relx=0.5, rely=0.5, anchor="center")

        sim_speed = CTkEntry(master=self, font=("BRLNSDB", 64), text_color=CANDY_DREAMS,
                             bg_color=PURPLE, fg_color="transparent", border_color=WISTERIA, justify="center",
                             border_width=5, height=75, width=BUTTON_SIZE)

        sim_speed.place(relx=0.5, rely=0.6, anchor="center")

        def finalstartsim():
            solar_system = SolarSystem(width = 1800, height = 800) # Set window dimensions, will change in future when implementing gui

            global simulationSpeed
            global speederror
            if speederror is not None:
                speederror.destroy()
            simulationSpeed=sim_speed.get()
            simulationSpeed=float(simulationSpeed)
            if (simulationSpeed<=0):
                speederror=Label(master=self, text="Speed less than or equal to 0.")
                speederror.grid(row=3)
            else :
                while True:
                    # print("pikachu")
                    solar_system.calculate_all_body_interactions()
                    solar_system.update_all()
                    time.sleep(1 / simulationSpeed / 100 )

        start_btn = CTkButton(master=self, text="Start Simulation", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                              bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                              border_width=5, height=75, width=BUTTON_SIZE,
                              command=finalstartsim)

        start_btn.place(relx=0.5, rely=0.7, anchor="center")


class MainSimulation(Turtle):
    def __init__(self):
        super().__init__()
        self.solar_system = SolarSystem(SCR_WIDTH, SCR_HEIGHT)

    def create_default_system(self):
        global solarSystem
        solarSystem = {
            "planets": (
                Planet("", None, self, 500, (50, 0), (0, 11)),
                Planet("", None, self, 10, (-350, 0), (0, -10)),
                Planet("", None, self, 5, (0, 200), (-2, -7)),
            ),
            "suns": (
                Sun("", self, 10000, (-200, 0), (0, 3)),
                Sun("", self, 10000, (200, 0), (0, -4)),
            )
        }


if __name__ == "__main__":
    app = App()
    app.mainloop()
