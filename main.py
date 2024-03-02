#Basic Import Functions
import tkinter as tk
import customtkinter as ctk
import PIL.Image
from tkinter import messagebox
import random
import time
from pathlib import Path
import json
import tkinter.messagebox

#Defining Commands - Making Main Frame, All Widgets in 2nd Window
def create_typing():
    global current_word_label, container, typing_container, text_container, current_text, typing_box, container
    #Clearing Frame
    for widget in main_window.winfo_children(): #Emptying out frame 
        widget.place_forget()
    main_window.pack_forget()
    
    root.geometry("1400x700")
    container = ctk.CTkFrame(root)
    container.pack(expand=True, fill="both")
    typing_container = ctk.CTkFrame(container)
    typing_container.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor="c")
    main_image = PIL.Image.open("main_image.png")
    dummy_widget1 = ctk.CTkLabel(typing_container, text = "", image =ctk.CTkImage(main_image, size=(1400, 700)))
    dummy_widget1.pack()
    text_container = ctk.CTkFrame(typing_container)
    text_container.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.45, anchor="n")
    # settings_container = ctk.CTkFrame(typing_container, fg_color= "blue")
    # settings_container.place(relx = 0.05, rely = 0.95, anchor = "sw", relheight = 0.4 )
    Back = ctk.CTkButton(container, text = "← Go Back", command = go_back)
    Back.place(relx = 0.1)
    current_word_label = ctk.CTkLabel(text_container, text=sampled_words[0], font=ctk.CTkFont(size=40))
    current_word_label.place(relx=0.5, rely=0.5, anchor="c")
    timer_label = ctk.CTkLabel(text_container, text = f"Time left: {timer_seconds} seconds")
    timer_label.place(relx = 0.5, rely = 0.7, anchor="c")

    current_text = ""
    typing_box = ctk.CTkEntry(typing_container, placeholder_text=sampled_words[0])
    typing_box.bind("<KeyRelease>", on_key_press)
    typing_box.place(relx=0.5, rely=0.95, anchor="c")
    click_box = ctk.CTkLabel(typing_container, text = "Click Box to Start", font=ctk.CTkFont(size=24), corner_radius= 100)
    click_box.place(relx=0.5, rely=0.9, anchor="c")

def go_back():
    container.pack_forget()  # Forget the current window
    root.geometry("450x350")  # Adjust window size

    make_main_window() # Have to remake content who knows why!!!
    place_main_window_content()

#After each key is pressed, it checks whether the word is right. If it is the word is destroyed and replaced with the other words. +1 Score
def on_key_press(e):
    global score
    current_text = typing_box.get()
    if current_text.strip() == sampled_words[0]:
        sampled_words.pop(0)
        update_current_word()
        typing_box.configure(placeholder_text=sampled_words[0])
        typing_box.delete(0, tk.END)
        score += 1
        update_timer()
        
#Command to update the word
def update_current_word():
    current_word_label.configure(text=sampled_words[0])

def get_words():
    global sampled_words
    with open("words.json") as file:
        words = json.load(file)
        sampled_words = random.sample(words, 100)



#Basic Import Functions
import tkinter as tk
import customtkinter as ctk
import PIL.Image
import random
import json

# Initialize a variable to store the ID of the scheduled update
timer_update_id = None

# Defining Commands - Making Main Frame, All Widgets in 2nd Window
def create_typing():
    global current_word_label, container, typing_container, text_container, current_text, typing_box, container, timer_label
    # Clearing Frame
    for widget in main_window.winfo_children():  # Emptying out frame
        widget.place_forget()
    main_window.pack_forget()

    root.geometry("1400x700")
    container = ctk.CTkFrame(root)
    container.pack(expand=True, fill="both")
    typing_container = ctk.CTkFrame(container)
    typing_container.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor="c")
    main_image = PIL.Image.open("main_image.png")
    dummy_widget1 = ctk.CTkLabel(typing_container, text="", image=ctk.CTkImage(main_image, size=(1400, 700)))
    dummy_widget1.pack()
    text_container = ctk.CTkFrame(typing_container)
    text_container.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.45, anchor="n")

    wpm_label = ctk.CTkLabel(typing_container, text="WPM: ")
    wpm_label.place(in_=typing_container, relx=0.1)

    Back = ctk.CTkButton(container, text="← Go Back", command=go_back)
    Back.place(relx=0.1)

    current_word_label = ctk.CTkLabel(text_container, text=sampled_words[0], font=ctk.CTkFont(size=40))
    current_word_label.place(relx=0.5, rely=0.5, anchor="c")

    global timer_label
    timer_label = ctk.CTkLabel(text_container, text=f"Time left: {timer_seconds} seconds")
    timer_label.place(relx=0.5, rely=0.7, anchor="c")

    current_text = ""
    typing_box = ctk.CTkEntry(typing_container, placeholder_text=sampled_words[0])
    typing_box.bind("<KeyRelease>", on_key_press)
    typing_box.place(relx=0.5, rely=0.95, anchor="c")

    click_box = ctk.CTkLabel(typing_container, text="Click Box to Start", font=ctk.CTkFont(size=24), corner_radius=100)
    click_box.place(relx=0.5, rely=0.9, anchor="c")


def go_back():
    container.pack_forget()  # Forget the current window
    root.geometry("450x350")  # Adjust window size
    make_main_window()  # Have to remake content who knows why!!!
    place_main_window_content()


def on_key_press(e):
    global score
    current_text = typing_box.get()
    if current_text.strip() == sampled_words[0]:
        sampled_words.pop(0)
        update_current_word()
        typing_box.configure(placeholder_text=sampled_words[0])
        typing_box.delete(0, tk.END)
        score += 1
        update_timer()


def update_current_word():
    current_word_label.configure(text=sampled_words[0])


def get_words():
    global sampled_words
    with open("words.json") as file:
        words = json.load(file)
        sampled_words = random.sample(words, 100)


def update_timer():
    global timer_seconds, timer_update_id, score 
    if timer_seconds > 0:
        timer_seconds -= 1
        timer_label.configure(text=f"Time left: {timer_seconds} seconds")
        # Cancel the previous scheduled update
        if timer_update_id:
            root.after_cancel(timer_update_id)
        # Schedule the next update
        timer_update_id = root.after(1000, update_timer)
    else:
        timer_label.configure(text="Time's up!")
        wpm_label = ctk.CTkLabel(typing_container, text = f"WPM: {score} ")
        wpm_label.place(in_ = typing_container, relx = 0.1)
        Restart_button = ctk.CTkButton(typing_container, text = "Restart", command = restart)
        Restart_button.place(relx=0.6, rely=0.95, anchor="c" )
        restart()
        


def start_timer(duration):
    global timer_seconds
    timer_seconds = duration
    update_timer()


def credits():
    tk.messagebox.showinfo("Credits", "Made by Gaurav 12SDD2")


def open_settings():
    settings_window = ctk.CTkToplevel(root)
    settings_window.lift()
    settings_window.focus_force()
    settings_window.grab_set()
    settings_window.grab_release()
    settings_window.title("Settings - Touch Typing Helper - Gaurav Surve")
    settings_window.geometry("500x300")

    frame2 = ctk.CTkFrame(settings_window, width=450, height=250)
    frame2.place(relx=0.5, rely=0.5, anchor=("c"))

    settings_image = PIL.Image.open("settings_image.png")
    dummy_widget3 = ctk.CTkLabel(frame2, text="", image=ctk.CTkImage(settings_image, size=(450, 250)))
    dummy_widget3.place()


def make_main_window():
    global main_window, Welcome_TTH, Begin_TTH, Settings, Credits, dummy_widget

    main_window = ctk.CTkFrame(root, width=400, height=500, border_width=10)

    dummy_widget = ctk.CTkLabel(main_window, text="", image=ctk.CTkImage(PIL.Image.open(Path(__file__).resolve().parents[0] / "polka.png"), size=(1400, 700)))

    Welcome_TTH = ctk.CTkLabel(main_window, text="Welcome to the Touch Type Helper", font=("Work Sans", 24), fg_color="#B89A94", corner_radius=100)

    Begin_TTH = ctk.CTkButton(main_window, text="Begin", font=("Arial", 16), fg_color="#B89A94", command=create_typing)

    Settings = ctk.CTkButton(main_window, text="Settings⚙️", font=("Arial", 16), fg_color="#B89A94", command=open_settings)

    Credits = ctk.CTkButton(main_window, text="Credits", font=("Arial", 16), fg_color="#B89A94", command=credits)

    ctk.set_default_color_theme("green")


def place_main_window_content():
    main_window.pack(expand=True, fill="both")
    dummy_widget.pack()
    Welcome_TTH.place(relx=0.5, rely=0.2, anchor="c")
    Begin_TTH.place(relx=0.5, rely=0.4, anchor="c")
    Settings.place(relx=0.5, rely=0.5, anchor="c")
    Credits.place(relx=0.5, rely=0.6, anchor="c")




def start_timer(duration):
   global timer_seconds
   timer_seconds = duration
   update_timer()

#Credits Function
def credits():
    tk.messagebox.showinfo("Credits", "Made by Gaurav 12SDD2")

#Command for settings button
def open_settings():     
    settings_window = ctk.CTkToplevel(root)
    settings_window.lift()
    settings_window.focus_force()
    settings_window.grab_set()
    settings_window.grab_release()
    settings_window.title("Settings - Touch Typing Helper - Gaurav Surve")
    settings_window.geometry("500x300")
    #Frame 2 Setting
    frame2 = ctk.CTkFrame(settings_window, width = 450, height = 250) #Settings Pop-up window frame
    frame2.place(relx = 0.5, rely = 0.5, anchor = ("c"))
    #Image for settings Background
    settings_image = PIL.Image.open("settings_image.png")
    dummy_widget3 = ctk.CTkLabel(frame2, text = "", image =ctk.CTkImage(settings_image, size=(450, 250)))
    dummy_widget3.place()

#Main Window Content - Frame Buttons labels etc
def make_main_window():
    #Pop Up-Window - Begin Touch Type Helper
    global main_window, Welcome_TTH, Begin_TTH, Settings, Credits, dummy_widget
    #main_window
    main_window = ctk.CTkFrame(root,width=400, height=500, border_width = 10) #border_color = "#13141F") )
    
    dummy_widget = ctk.CTkLabel(main_window, text="", image=ctk.CTkImage(PIL.Image.open(Path(__file__).resolve().parents[0] / "polka.png"), size=(1400,700)))
    
    # Labels Used
    Welcome_TTH = ctk.CTkLabel(main_window, text="Welcome to the Touch Type Helper", font=("Work Sans", 24), fg_color="#B89A94", corner_radius=100)

    # Buttons
    Begin_TTH = ctk.CTkButton(main_window, text="Begin", font=("Arial", 16), fg_color="#B89A94", command = create_typing)

    Settings = ctk.CTkButton(main_window, text="Settings⚙️", font=("Arial", 16), fg_color="#B89A94", command = open_settings)

    Credits = ctk.CTkButton(main_window, text="Credits", font=("Arial", 16), fg_color="#B89A94", command = credits)

    #Themes
    ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

def restart():
    global score, timer_seconds
    score = 0
    timer_seconds = 10

#Placing Main Window content
def place_main_window_content():
    main_window.pack(expand = True, fill = "both")
    dummy_widget.pack()
    Welcome_TTH.place(relx = 0.5, rely = 0.2, anchor = "c")
    Begin_TTH.place(relx = 0.5, rely = 0.4, anchor = "c")
    Settings.place(relx = 0.5, rely = 0.5, anchor = "c")
    Credits.place(relx = 0.5, rely = 0.6, anchor = "c")

# Note for you: 
# - this is a good programming practice
# - only run if you are directly executing the script
# - doesn't run if you import the script into another script
if __name__ == "__main__":
    get_words()
    timer_seconds = 10
    score = 0 #Keeps score on how many words are right
    
    root = ctk.CTk()
    root.geometry("1400x700")
    root.title("Touch Typing Helper - Gaurav Surve")
    
    make_main_window()
    place_main_window_content()
    root.mainloop()