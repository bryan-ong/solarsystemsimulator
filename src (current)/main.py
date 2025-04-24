import threading
from turtle import Turtle
import time
from customtkinter import *
from tkinter import *
from PIL import Image
from const import *
from solarsystem import *


set_appearance_mode("dark")
set_default_color_theme("blue")

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Gravision")
        self.geometry(str(SCR_WIDTH) + "x" + str(SCR_HEIGHT))

        self.container = CTkFrame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

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
                             command=lambda: controller.show_page(Menu))

        back_btn.place(relx=0.1, rely=0.1, anchor="center")

        explanation_img = Image.open("../assets/explanation.png")
        explanation_lbl = CTkButton(self, text="", bg_color=WISTERIA, hover_color=WISTERIA, fg_color="transparent", border_color=CANDY_DREAMS,
                                    border_width= 5, width=420, height=270, corner_radius=5,
                                    image=CTkImage(light_image=explanation_img, dark_image=explanation_img, size=(400, 250)))
        explanation_lbl.place(x=(SCR_WIDTH // 2 - 200), rely=0.7)


class Default(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.solar_system = None
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

        self.simulation_running = False
        self.simulation_speed = 0.01
        self.simulation_job = None

    def create_default_system(self):

        self.solar_system = SolarSystem(SCR_WIDTH, SCR_HEIGHT)

        Sun("Sun 1", self.solar_system, 10000, (-200, 0), (0, 3))
        Sun("Sun 2", self.solar_system, 10000, (200, 0), (0, -4))
        Planet("Planet 1", None, self.solar_system, 500, (50, 0), (0, 11))
        Planet("Planet 2", None, self.solar_system, 10, (-350, 0), (0, -10))
        Planet("Planet 3", None, self.solar_system, 5, (0, 200), (-2, -7))

    def run_simulation(self):
        if not self.simulation_running:
            return

        self.solar_system.calculate_all_body_interactions()
        self.solar_system.update_all()
        self.simulation_job = self.after(int(self.simulation_speed * 1000), self.run_simulation)


    def on_close(self):
        self.stop_simulation()

        if hasattr(self, 'solar_system') and self.solar_system:
            self.solar_system = None
            turtle.clearscreen()
            turtle.bye()

    def start_simulation(self):
        try:
            speed_input = float(self.sim_speed.get())
            self.simulation_speed = max(0.001, 1 / speed_input * 0.01)
        except ValueError:
            self.simulation_speed = 0.01


        self.create_default_system()
        print(self.solar_system)

        self.simulation_running = True
        self.run_simulation()
        canvas = self.solar_system.get_screen().getcanvas()
        root = canvas.winfo_toplevel()

        root.protocol("WM_DELETE_WINDOW", self.on_close)

    def stop_simulation(self):
        self.simulation_running = False
        if self.simulation_job:
            self.after_cancel(self.simulation_job)
            self.simulation_job = None

    def back_to_menu(self):
        self.stop_simulation()

        if hasattr(self, 'solar_system') and self.solar_system:
            turtle.clearscreen()
            turtle.bye()
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
                             command=lambda: controller.show_page(Simulation))

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
                         from_=0, to=10000,
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
                           from_=-20, to=20,
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
                           from_=-20, to=20,
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
                          from_=-500, to=500,
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
                          from_=-500, to=500,
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


class Random(CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
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
                             command=lambda: controller.show_page(Simulation))

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

        start_btn = CTkButton(master=self, text="Start Simulation", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                              bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA,
                              border_width=5, height=75, width=BUTTON_SIZE,
                              command=lambda: controller.show_page(Menu))

        start_btn.place(relx=0.5, rely=0.7, anchor="center")


class MainSimulation:
    def __init__(self, master, sim_speed=1.0):
        self.master = master
        self.sim_speed = sim_speed
        self.solar_system = SolarSystem(SCR_WIDTH, SCR_HEIGHT)
        self.running = False


    def create_default_system(self):
        self.solar_system.bodies = []
        Sun("Sun 1", self.solar_system, 500, (-50, 0), (0, 0))
        Sun("Sun 2", self.solar_system, 500, (100, 0), (0, -0))
        Planet("Planet 1", None, self.solar_system, 500, (50, 0), (0, 11))
        Planet("Planet 2", None, self.solar_system, 10, (-350, 0), (0, -10))
        Planet("Planet 3", None, self.solar_system, 5, (0, 200), (-2, -7))

    def start_simulation(self):
        self.running = True
        self.run_simulation()

    def stop_simulation(self):
        self.running = False

    def run_simulation(self):
        if self.running:
            self.solar_system.calculate_all_body_interactions()
            self.solar_system.update_all()
            self.master.after(int(1 / self.sim_speed) * 25, self.run_simulation)


if __name__ == "__main__":
    app = App()
    app.mainloop()
