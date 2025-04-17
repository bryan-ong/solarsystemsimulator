
from customtkinter import *
from win32api import GetSystemMetrics
from PIL import Image

# Color palette
MAJORELLE_BLUE = "#574ae2"
AFTER_WORK_BLUE = "#222a68"
SWEET_FLAG = "#654597"
WISTERIA = "#ab81cd"
CANDY_DREAMS = "#e2adf2"
POMPELMO = "#ff6464"
TRANSPARENT = "#ffff15"
# Variables
top_bar_height = 36
app = CTk()
app.attributes("-fullscreen", True)
SCR_WIDTH = GetSystemMetrics(0)
SCR_HEIGHT = GetSystemMetrics(1)
set_appearance_mode("dark")
def quit_app():
    app.quit()

class MainMenu(CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def draw_main_menu(self):
        bg_img = Image.open("assets/bg.jpg")
        bg_lbl = CTkLabel(app, text="", image=CTkImage(light_image=bg_img, dark_image=bg_img, size=(SCR_WIDTH, 1080)))
        bg_lbl.place(x=0, y=0)

        top_bar = CTkCanvas(master=app, bg=MAJORELLE_BLUE, width=SCR_WIDTH, height=36, bd=0, highlightthickness=0)
        top_bar.place(relx=0.5, rely=0, anchor="n")

        exit_btn_img = Image.open("assets/closebtn.png").convert("RGBA")
        exit_btn = CTkButton(top_bar, image=CTkImage(dark_image=exit_btn_img, light_image=exit_btn_img),
                             text="", hover_color=POMPELMO, fg_color=MAJORELLE_BLUE, corner_radius=0, width=top_bar_height,
                             height=top_bar_height, command=quit_app)
        exit_btn.place(x=SCR_WIDTH, rely=0, anchor="ne")

        mini_btn_img = Image.open("assets/minibtn.png").convert("RGBA")
        mini_btn = CTkButton(top_bar, image=CTkImage(dark_image=mini_btn_img, light_image=mini_btn_img),
                             text="", hover_color=POMPELMO, fg_color=MAJORELLE_BLUE, corner_radius=0, width=top_bar_height,
                             height=top_bar_height, command=self.iconify())
        mini_btn.place(x=SCR_WIDTH - top_bar_height, rely=0, anchor="ne")


        title_btn = CTkButton(master=app, text="GRAVISION", font=("BRLNSDB", 96), text_color=CANDY_DREAMS,
                             bg_color=SWEET_FLAG, fg_color="transparent", hover_color=SWEET_FLAG, border_color=WISTERIA, border_width=5, width=SCR_WIDTH + 100, height=SCR_HEIGHT/8)
        title_btn.place(relx=0.5, rely=0.33, anchor="center")

        sim_btn = CTkButton(master=app, text="Simulate", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA, border_width=5, height=75, width=200)
        setting_btn = CTkButton(master=app, text="Settings", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA, border_width=5, height=75, width=200)
        theory_btn = CTkButton(master=app, text="Theory", font=("BRLNSDB", 32), text_color=CANDY_DREAMS,
                             bg_color=SWEET_FLAG, fg_color="transparent", hover_color=WISTERIA, border_color=WISTERIA, border_width=5, height=75, width=200)
        sim_btn.place(relx=0.5, rely=0.5, anchor="center")
        setting_btn.place(relx=0.5, rely=0.6, anchor="center")
        theory_btn.place(relx=0.5, rely=0.7, anchor="center")


app.mainloop()
