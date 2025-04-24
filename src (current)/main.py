import threading
import turtle
from turtle import Turtle
import time

import PIL.ImageTk
from customtkinter import *
from tkinter import *
from PIL import Image
from const import *
from solarsystem import *
from random import randrange

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
icon_path = os.path.join(project_root, "assets", "icon.ico")


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Gravision")
        self.geometry(str(SCR_WIDTH) + "x" + str(SCR_HEIGHT))

        self.container = CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.iconbitmap(icon_path)

        self.frames = {}
        for F in (Menu, Simulation, Theory, Default, Custom, Random):
            frame = F(parent=self.container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_page(Menu)

    def show_page(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

    def close_windows(self):
        self.destroy()


class Menu(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(fg_color="transparent")
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
                            command=lambda: controller.show_page(Simulation))
        theory_btn = CTkButton(master=self, text="Theory", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                               bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                               border_width=5, height=75, width=BUTTON_SIZE,
                               command=lambda: controller.show_page(Theory))
        exit_btn = CTkButton(master=self, text="Exit", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                             border_width=5, height=75, width=BUTTON_SIZE, command=lambda: controller.close_windows())

        sim_btn.place(relx=0.5, rely=0.5, anchor="center")
        theory_btn.place(relx=0.5, rely=0.6, anchor="center")
        exit_btn.place(relx=0.5, rely=0.7, anchor="center")


class Simulation(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(fg_color="transparent")
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
                                command=lambda: controller.show_page(Default))

        default_btn.place(relx=0.5, rely=0.5, anchor="center")

        custom_btn = CTkButton(master=self, text="Custom", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                               bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                               border_width=5, height=75, width=BUTTON_SIZE,
                               command=lambda: controller.show_page(Custom))

        custom_btn.place(relx=0.5, rely=0.6, anchor="center")

        random_btn = CTkButton(master=self, text="Randomize", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                               bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                               border_width=5, height=75, width=BUTTON_SIZE,
                               command=lambda: controller.show_page(Random))

        random_btn.place(relx=0.5, rely=0.7, anchor="center")

        back_btn = CTkButton(master=self, text="Back to Menu", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                             border_width=5, height=75, width=BUTTON_SIZE,
                             command=lambda: controller.show_page(Menu))

        back_btn.place(relx=0.5, rely=0.8, anchor="center")


class Theory(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(fg_color="transparent")
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
                                text="",
                                fg_color="transparent",
                                bg_color=SWEET_FLAG,
                                height=300, width=1400,
                                border_color=WISTERIA,
                                hover_color=SWEET_FLAG,
                                border_width=5,
                                font=CTkFont(family='Inter', size=24),
                                text_color=(CANDY_DREAMS, CANDY_DREAMS),
                                anchor="w",
                                )
        explanation.place(relx=0.5, rely=0.5, anchor="center")

        explainationtext = CTkLabel(master=explanation,
                                    text="- Objects usually move with a constant velocity in space. \n"
                                         "- The moving direction changes due to gravity of objects nearby. \n"
                                         "- All objects with mass exert gravity and attract each other. \n"
                                         "- The higher the mass, the stronger the gravitational force is. \n"
                                         "- High-velocity objects may escape this pull, while slower ones \n"
                                         "might end up crashing into each other. \n"
                                         "- Heavier objects tend to remain its moving direction. \n"
                                         "- Object with a much lower mass might disappear while the object \n"
                                         "with higher mass won’t.", fg_color="transparent",
                                    bg_color=SWEET_FLAG,
                                    height=270, width=1400,
                                    font=CTkFont(family='Inter', size=24),
                                    text_color=(CANDY_DREAMS, CANDY_DREAMS),
                                    anchor="w",
                                    justify="left")
        explainationtext.place(relx=0.27, rely=0.05)

        back_btn = CTkButton(master=self, text="Back to Menu", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                             border_width=5, height=75, width=BUTTON_SIZE,
                             command=lambda: controller.show_page(Menu))

        back_btn.place(relx=0.1, rely=0.1, anchor="center")

        explanation_img = Image.open("../assets/explanation.png")
        explanation_lbl = CTkButton(self, text="", bg_color=WISTERIA, hover_color=WISTERIA, fg_color="transparent",
                                    border_color=CANDY_DREAMS,
                                    border_width=5, width=420, height=270, corner_radius=5,
                                    image=CTkImage(light_image=explanation_img, dark_image=explanation_img,
                                                   size=(400, 250)))
        explanation_lbl.place(x=(SCR_WIDTH // 2 - 400), rely=0.7)
        explanation_label = CTkButton(master=self,
                                      text="""m = mass of object\nf = gravitational force\n r = distance between two objects """,
                                      fg_color="transparent",
                                      bg_color=SWEET_FLAG,
                                      height=100, width=250,
                                      border_color=WISTERIA,
                                      hover_color=SWEET_FLAG,
                                      border_width=5,
                                      font=CTkFont(family='Inter', size=24),
                                      text_color=(CANDY_DREAMS, CANDY_DREAMS),
                                      )
        explanation_label.place(x=(SCR_WIDTH // 2 - 200) + 300, rely=0.8)


class Default(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(fg_color="transparent")
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
                             command=self.back_to_menu)

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

        self.sim_speed = CTkEntry(master=self, font=("BRLNSDB", 64), text_color=CANDY_DREAMS,
                                  bg_color=PURPLE, fg_color="transparent", border_color=WISTERIA, justify="center",
                                  border_width=5, height=75, width=BUTTON_SIZE)
        self.sim_speed.insert(0, "1")
        self.sim_speed.place(relx=0.5, rely=0.6, anchor="center")

        start_btn = CTkButton(master=self, text="Start Simulation", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                              bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                              border_width=5, height=75, width=BUTTON_SIZE,
                              command=self.start_simulation)

        start_btn.place(relx=0.5, rely=0.7, anchor="center")

        self.solar_system = None
        self.simulation_running = False
        self.simulation_speed = 0.01
        self.simulation_job = None

        # PLEASE DON'T MIND ALL THE EXCEPTIONS, IT WORKS...

    def create_default_system(self):
        try:
            turtle.reset()
            turtle.hideturtle()

            self.solar_system = SolarSystem(SCR_WIDTH, SCR_HEIGHT)

            Sun("Sun 1", self.solar_system, 10000, (-200, 0), (0, 3))
            Sun("Sun 2", self.solar_system, 10000, (200, 0), (0, -4))
            Planet("Planet 1", None, self.solar_system, 500, (50, 0), (0, 11))
            Planet("Planet 2", None, self.solar_system, 10, (-350, 0), (0, -10))
            Planet("Planet 3", None, self.solar_system, 5, (0, 200), (-2, -7))
        except:
            pass

    def run_simulation(self):
        if self.simulation_running:
            try:
                self.solar_system.calculate_all_body_interactions()
                self.solar_system.update_all()
                self.simulation_job = self.after(int(self.simulation_speed * 1000), self.run_simulation)
            except:
                pass

    def start_simulation(self):
        try:
            speed_input = float(self.sim_speed.get())
            self.simulation_speed = max(0.001, 1 / speed_input * 0.01)
        except ValueError:
            self.simulation_speed = 0.01

        if self.simulation_running:
            self.simulation_running = False
            if self.simulation_job:
                self.after_cancel(self.simulation_job)
                self.simulation_job = None

        self.create_default_system()

        self.simulation_running = True
        self.run_simulation()

    def stop_simulation(self):
        self.simulation_running = False
        if self.simulation_job:
            self.after_cancel(self.simulation_job)
            self.simulation_job = None

        if hasattr(self, 'solar_system') and self.solar_system:
            self.solar_system.bodies = []

    def back_to_menu(self):
        self.stop_simulation()

        try:
            turtle.reset()
            turtle.bye()
        except:
            pass

        self.solar_system = None

        self.controller.show_page(Simulation)


class Custom(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(fg_color="transparent")
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

        list = CTkButton(master=self, text="", bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG,
                         border_color=WISTERIA,
                         border_width=5, height=SCR_HEIGHT // 2, width=BUTTON_SIZE * 3)
        list.place(relx=0.75, rely=0.5, anchor="center")

        start_btn = CTkButton(master=self,
                              text="Start Simulation", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                              bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                              border_width=5, height=75, width=BUTTON_SIZE,
                              command=lambda:self.start_simulation()
                              )

        start_btn.place(relx=0.75,
                        rely=0.9,
                        anchor="center")

        back_btn = CTkButton(master=self, text="Back to Simulate", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                             border_width=5, height=75, width=BUTTON_SIZE,
                             command=lambda: self.back_to_menu())

        back_btn.place(relx=0.1, rely=0.1, anchor="center")

        add_planet_btn = CTkButton(master=self,
                                   text="Add as Planet", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                                   bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA,
                                   border_color=WISTERIA,
                                   border_width=5, height=75, width=BUTTON_SIZE,
                                   command=lambda: self.add_celestial_body("Planet")
                                   )

        add_planet_btn.place(relx=0.2,
                             rely=0.9,
                             anchor="center")

        add_star_btn = CTkButton(master=self,
                                 text="Add as Star", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                                 bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA,
                                 border_color=WISTERIA,
                                 border_width=5, height=75, width=BUTTON_SIZE,
                                 command=lambda: self.add_celestial_body("Star")
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

        self.var_name = StringVar()

        name = CTkEntry(master=self, font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=PURPLE, fg_color="transparent", border_color=WISTERIA, justify="center",
                             border_width=5, height=75, width=BUTTON_SIZE * 1.5, textvariable=self.var_name)

        name.place(relx=0.3,
                        rely=0.3,
                        anchor="center")

        label = CTkButton(master=self,
                          text="Mass: ", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                          border_width=5, height=75, width=BUTTON_SIZE,
                          )
        label.place(relx=0.1, rely=0.4, anchor="center")

        self.var_mass = IntVar()
        mass = CTkSlider(master=self,
                              bg_color=WISTERIA, width=BUTTON_SIZE * 1.5, height=20, fg_color=SWEET_FLAG,
                              corner_radius=1, button_color=LILAC, button_hover_color="white", progress_color=PURPLE,
                              from_=1, to=10000, variable=self.var_mass)
        mass.set(1)
        mass.place(relx=0.3, rely=0.4, anchor="center")

        value = CTkButton(self, textvariable=self.var_mass, font=("BRLNSDB", 24), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                          border_width=5, height=75, width=75)
        value.place(relx=0.43, rely=0.4, anchor="center")

        label = CTkButton(master=self,
                          text="Initial X-vel: ", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                          border_width=5, height=75, width=BUTTON_SIZE,
                          )
        label.place(relx=0.1, rely=0.5, anchor="center")

        self.var_x_velo = IntVar()

        x_velo = CTkSlider(master=self,
                                bg_color=WISTERIA, width=BUTTON_SIZE * 1.5, height=20, fg_color=SWEET_FLAG,
                                corner_radius=1, button_color=LILAC, button_hover_color="white", progress_color=PURPLE,
                                from_=-20, to=20,
                                variable=self.var_x_velo)
        x_velo.place(relx=0.3,
                          rely=0.5,
                          anchor="center", )
        value = CTkButton(self, textvariable=self.var_x_velo, font=("BRLNSDB", 24), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                          border_width=5, height=75, width=75)
        value.place(relx=0.43, rely=0.5, anchor="center")

        label = CTkButton(master=self,
                          text="Initial Y-vel: ", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                          border_width=5, height=75, width=BUTTON_SIZE)

        label.place(relx=0.1, rely=0.6, anchor="center")

        self.var_y_velo = IntVar()
        y_velo = CTkSlider(master=self, bg_color=WISTERIA, width=BUTTON_SIZE * 1.5, height=20, fg_color=SWEET_FLAG,
                                corner_radius=1, button_color=LILAC, button_hover_color="white", progress_color=PURPLE,
                                from_=-20, to=20,
                                variable=self.var_y_velo)
        y_velo.place(relx=0.3, rely=0.6, anchor="center")

        value = CTkButton(self, textvariable=self.var_y_velo, font=("BRLNSDB", 24), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                          border_width=5, height=75, width=75)
        value.place(relx=0.43, rely=0.6, anchor="center")

        label = CTkButton(master=self,
                          text="Initial X-pos: ", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                          border_width=5, height=75, width=BUTTON_SIZE)

        label.place(relx=0.1, rely=0.7, anchor="center")

        self.var_x_pos = IntVar()
        x_pos = CTkSlider(master=self,
                               bg_color=WISTERIA, width=BUTTON_SIZE * 1.5, height=20, fg_color=SWEET_FLAG,
                               corner_radius=1, button_color=LILAC, button_hover_color="white", progress_color=PURPLE,
                               from_=-500, to=500,
                               variable=self.var_x_pos)
        x_pos.place(relx=0.3, rely=0.7, anchor="center")

        value = CTkButton(self, textvariable=self.var_x_pos, font=("BRLNSDB", 24), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                          border_width=5, height=75, width=75)
        value.place(relx=0.43, rely=0.7, anchor="center")

        label = CTkButton(master=self,
                          text="Initial Y-pos: ", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                          border_width=5, height=75, width=BUTTON_SIZE,
                          )
        label.place(relx=0.1, rely=0.8, anchor="center")
        self.var_y_pos = IntVar()
        y_pos = CTkSlider(master=self,
                               bg_color=WISTERIA, width=BUTTON_SIZE * 1.5, height=20, fg_color=SWEET_FLAG,
                               corner_radius=1,
                               button_color=LILAC, button_hover_color="white", progress_color=PURPLE,
                               from_=-500, to=500,
                               variable=self.var_y_pos)
        y_pos.place(relx=0.3, rely=0.8, anchor="center")
        value = CTkButton(self, textvariable=self.var_y_pos, font=("BRLNSDB", 24), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA,
                          border_width=5, height=75, width=75)
        value.place(relx=0.43, rely=0.8, anchor="center")

        self.solar_system = None
        self.simulation_running = False
        self.simulation_speed = 0.01
        self.simulation_job = None
        self.body_list = []

    def add_celestial_body(self, body_type):
        # I want to only create the SolarSystem instance only when start_simulation is called (as creating the instance would open the turtle window immediately, disrupting the flow),
        # this means the original way (now deleted) of immediately appending to the System's bodies list is not possible, as self.solar_system is None at the time. To circumvent this,
        # we have to store the list of Bodies to be created in a dictionary in a list. Then only initialize those bodies once we start the simulation.
        name = self.var_name.get()
        mass = self.var_mass.get()
        x_pos = self.var_x_pos.get()
        y_pos = self.var_y_pos.get()
        x_velo = self.var_x_velo.get()
        y_velo = self.var_y_velo.get()

        body_data = {
            'type': body_type,
            'name': name,
            'mass': mass,
            'position': (x_pos, y_pos),
            'velocity': (x_velo, y_velo)
        }

        self.body_list.append(body_data)
        print(f"Stored {body_type}: {name}")

    def start_simulation(self):
        try:
            # speed_input = float(self.sim_speed.get())
            speed_input = 1
            self.simulation_speed = max(0.001, 1 / speed_input * 0.01)
        except ValueError:
            self.simulation_speed = 0.01

        if self.simulation_running:
            self.simulation_running = False
            if self.simulation_job:
                self.after_cancel(self.simulation_job)
                self.simulation_job = None

        try:

            turtle.reset()
            turtle.hideturtle()
            self.solar_system = SolarSystem(SCR_WIDTH, SCR_HEIGHT)

            for body_data in self.body_list:
                if body_data['type'] == "Star":
                    Sun(body_data['name'], self.solar_system, body_data['mass'],
                        body_data['position'], body_data['velocity'])
                elif body_data['type'] == "Planet":
                    Planet(body_data['name'], None, self.solar_system, body_data['mass'],
                           body_data['position'], body_data['velocity'])
        except:
            pass


        self.simulation_running = True
        self.run_simulation()


    def run_simulation(self):
        if self.simulation_running:
            try:
                self.solar_system.calculate_all_body_interactions()
                self.solar_system.update_all()
                self.simulation_job = self.after(int(self.simulation_speed * 1000), self.run_simulation)
            except:
                pass

    def stop_simulation(self):
        self.simulation_running = False
        if self.simulation_job:
            self.after_cancel(self.simulation_job)
            self.simulation_job = None

        if hasattr(self, 'solar_system') and self.solar_system:
            self.solar_system.bodies = []

    def back_to_menu(self):
        self.stop_simulation()

        try:
            turtle.reset()
            turtle.bye()
        except:
            pass

        self.solar_system = None

        self.controller.show_page(Simulation)


class Random(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(fg_color="transparent")
        self.place(relwidth=1, relheight=1)

        bg_img = Image.open("../assets/bg.jpg")
        bg_lbl = CTkLabel(self, text="",
                          image=CTkImage(light_image=bg_img, dark_image=bg_img, size=(SCR_WIDTH, SCR_HEIGHT)))
        bg_lbl.place(x=0, y=0)

        title = CTkButton(master=self, text="RANDOM", font=("BRLNSDB", 96), text_color=CANDY_DREAMS,
                          bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG,
                          border_color=WISTERIA, border_width=5,
                          width=SCR_WIDTH + 100, height=SCR_HEIGHT / 8)

        title.place(relx=0.5, rely=0.3, anchor="center")

        back_btn = CTkButton(master=self, text="Back to Simulate", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                             border_width=5, height=75, width=BUTTON_SIZE,
                             command=self.back_to_menu)

        back_btn.place(relx=0.1, rely=0.1, anchor="center")

        label = CTkButton(master=self,
                          text="""Generates a solar system using a randomized range of values.
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

        self.sim_speed = CTkEntry(master=self, font=("BRLNSDB", 64), text_color=CANDY_DREAMS,
                                  bg_color=PURPLE, fg_color="transparent", border_color=WISTERIA, justify="center",
                                  border_width=5, height=75, width=BUTTON_SIZE)
        self.sim_speed.insert(0, "1")
        self.sim_speed.place(relx=0.5, rely=0.6, anchor="center")

        start_btn = CTkButton(master=self, text="Start Simulation", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                              bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                              border_width=5, height=75, width=BUTTON_SIZE,
                              command=self.start_simulation)

        start_btn.place(relx=0.5, rely=0.7, anchor="center")

        self.solar_system = None
        self.simulation_running = False
        self.simulation_speed = 0.01
        self.simulation_job = None

        # PLEASE DON'T MIND ALL THE EXCEPTIONS, IT WORKS...

    def create_random_system(self):
        effective_width = 1500
        effective_height = 750
        min_radius_sun = 200

        try:
            turtle.reset()
            turtle.hideturtle()
            self.solar_system = SolarSystem(SCR_WIDTH, SCR_HEIGHT)

            for i in range(randrange(3, 10)):
                Planet("", None, self.solar_system, randrange(200, 500),
                       (  # Extra logic to ensure the planets don't spawn too close to the sun
                           randrange(int(-effective_width / 2), min_radius_sun) if bool(
                               random.getrandbits(1)) else randrange(
                               min_radius_sun, int(effective_width / 2)),
                           randrange(int(-effective_height / 2), min_radius_sun) if bool(
                               random.getrandbits(1)) else randrange(min_radius_sun, int(effective_height / 2))),
                       (randrange(-5, 5), randrange(-5, 5))
                       )

            Sun("", self.solar_system, 10000, (0, 0), (0, 0)),

        except:
            pass

    def run_simulation(self):
        if self.simulation_running:
            try:
                self.solar_system.calculate_all_body_interactions()
                self.solar_system.update_all()
                self.simulation_job = self.after(int(self.simulation_speed * 1000), self.run_simulation)
            except:
                pass

    def start_simulation(self):
        try:
            speed_input = float(self.sim_speed.get())
            self.simulation_speed = max(0.001, 1 / speed_input * 0.01)
        except ValueError:
            self.simulation_speed = 0.01

        if self.simulation_running:
            self.simulation_running = False
            if self.simulation_job:
                self.after_cancel(self.simulation_job)
                self.simulation_job = None

        self.create_random_system()

        self.simulation_running = True
        self.run_simulation()

    def stop_simulation(self):
        self.simulation_running = False
        if self.simulation_job:
            self.after_cancel(self.simulation_job)
            self.simulation_job = None

        if hasattr(self, 'solar_system') and self.solar_system:
            self.solar_system.bodies = []

    def back_to_menu(self):
        self.stop_simulation()

        try:
            turtle.reset()
            turtle.bye()
        except:
            pass

        self.solar_system = None

        self.controller.show_page(Simulation)

if __name__ == "__main__":
    app = App()
    app.mainloop()
