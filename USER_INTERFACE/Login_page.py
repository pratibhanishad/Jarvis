import customtkinter as ctk
from tkinter import messagebox
import subprocess
import sys
import os


def start_jarvis_ui():
    # Close Tkinter login window
    app.destroy()

    # Run the PyQt5 Jarvis UI
    current_directory = os.path.dirname(os.path.abspath(__file__))
    ui_file = os.path.join(current_directory, "ui.py")  # <- yaha apne PyQt file ka naam likhna
    subprocess.Popen([sys.executable, ui_file])


def check_login():
    user = entry_user.get()
    password = entry_pass.get()

    if user == "Pratibha_Nishad" and password == "1234":  # apna username/password
        messagebox.showinfo("Login Success", "Welcome to Jarvis!")
        start_jarvis_ui()
    else:
        messagebox.showerror("Error", "Invalid Credentials")


# -------------- LOGIN WINDOW ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Jarvis Login Page")
app.geometry("600x400")

frame = ctk.CTkFrame(master=app, width=350, height=250, corner_radius=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

title = ctk.CTkLabel(master=frame, text="PRATIBHA NISHAD", font=("Arial", 20, "bold"))
title.pack(pady=20)

entry_user = ctk.CTkEntry(master=frame, placeholder_text="Enter User ID", width=250)
entry_user.pack(pady=10)

entry_pass = ctk.CTkEntry(master=frame, placeholder_text="Enter Password", show="*", width=250)
entry_pass.pack(pady=10)

login_btn = ctk.CTkButton(master=frame, text="Login", command=check_login, width=120)
login_btn.pack(pady=20)

app.mainloop()
