#Basic Import Functions
import tkinter as tk
import customtkinter as ctk
import PIL.Image
from tkinter import *
from tkinter import messagebox
import random
import keyboard
import time
from pathlib import Path
import json
import tkinter.messagebox



#Defining Commands - Making Main Frame
def create_typing():
    global x, main_window
    #Clearing Frame
    for widget in main_window.winfo_children(): #Emptying out frame 
        widget.place_forget()
    global container, typing_container, text_container
    main_window.pack_forget()
    root.geometry("1400x700")
    container = ctk.CTkFrame(root, fg_color="red")
    container.pack(expand=True, fill="both")
    typing_container = ctk.CTkFrame(container, fg_color="green")
    typing_container.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor="c")
    text_container = ctk.CTkFrame(typing_container, fg_color="yellow")
    text_container.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.45, anchor="n")
    settings_container = ctk.CTkFrame(typing_container, fg_color= "blue")
    settings_container.place(relx = 0.05, rely = 0.95, anchor = "sw", relheight = 0.4 )
    wpm_label = ctk.CTkLabel(typing_container, text = "WPM: ")
    wpm_label.place(in_ = typing_container, relx = 0.1)
    accuracy_label = ctk.CTkLabel(typing_container, text = "ACCURACY: ")
    accuracy_label.place(in_ = typing_container, relx = 0.2)
            
def credits():
    tk.messagebox.showinfo("Credits", "Made by Gaurav 12SDD2")
    

def settings():     #Command for settings button
    settings_window = ctk.CTkToplevel(root)
    settings_window.lift()
    settings_window.focus_force()
    settings_window.grab_set()
    settings_window.grab_release()
    settings_window.title("Settings - Touch Typing Helper - Gaurav Surve")
    settings_window.geometry("500x300")
    #Frame 2 Setting
    frame2 = ctk.CTkFrame(settings_window, width = 450, height = 250) #Settings Pop-up window frame
    frame2.grid(row=0, column=0, padx=25, pady=25)

#Pop Up-Window - Begin Touch Type Helper
root = ctk.CTk()
root.geometry("450x350")
root.title("Touch Typing Helper - Gaurav Surve")

#main_window
main_window = ctk.CTkFrame(root,width=400, height=500, border_width = 10, border_color = "#13141F")
main_window.pack(expand = True, fill = "both")
# Labels Used
Welcome_TTH = ctk.CTkLabel(main_window, text="Welcome to the Touch Type Helper", font=("Work Sans", 24), fg_color="#000435", corner_radius=100)
Welcome_TTH.place(relx = 0.5, rely = 0.2, anchor = "c")

# Buttons
Begin_TTH = ctk.CTkButton(main_window, text="Begin", font=("Arial", 16), fg_color="#282E78", command = create_typing)
Begin_TTH.place(relx = 0.5, rely = 0.4, anchor = "c")

Settings = ctk.CTkButton(main_window, text="Settings⚙️", font=("Arial", 16), fg_color="#282E78", command = settings)
Settings.place(relx = 0.5, rely = 0.5, anchor = "c")

Credits = ctk.CTkButton(main_window, text="Credits", font=("Arial", 16), fg_color="#282E78", command = credits)
Credits.place(relx = 0.5, rely = 0.6, anchor = "c")

#Themes
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


root.mainloop()