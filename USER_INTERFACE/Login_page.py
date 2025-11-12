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


# ---------------- LOGIN WINDOW ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Jarvis Login Page")

# 🔹 Make window larger (HD size)
app.geometry("900x600")   # was 600x400

# Optional: Disable resizing (for fixed layout)
app.resizable(False, False)

# 🔹 Main frame (centered)
frame = ctk.CTkFrame(master=app, width=500, height=400, corner_radius=25)
frame.place(relx=0.5, rely=0.5, anchor="center")

# 🔹 Title
title = ctk.CTkLabel(
    master=frame,
    text="WELCOME TO JARVIS",
    font=("Arial Rounded MT Bold", 28, "bold"),
    text_color="cyan"
)
title.pack(pady=(40, 20))

# 🔹 Subtitle
subtitle = ctk.CTkLabel(
    master=frame,
    text="Login as Pratibha Nishad",
    font=("Arial", 16),
    text_color="#AAAAAA"
)
subtitle.pack(pady=(0, 20))

# 🔹 Username entry
entry_user = ctk.CTkEntry(
    master=frame,
    placeholder_text="Enter User ID",
    width=300,
    height=40,
    corner_radius=10,
    font=("Arial", 14)
)
entry_user.pack(pady=15)

# 🔹 Password entry
entry_pass = ctk.CTkEntry(
    master=frame,
    placeholder_text="Enter Password",
    show="*",
    width=300,
    height=40,
    corner_radius=10,
    font=("Arial", 14)
)
entry_pass.pack(pady=15)

# 🔹 Login button (bigger & stylish)
login_btn = ctk.CTkButton(
    master=frame,
    text="LOGIN",
    command=check_login,
    width=200,
    height=45,
    corner_radius=15,
    font=("Arial Rounded MT Bold", 18),
    fg_color="#0078D7",
    hover_color="#005999"
)
login_btn.pack(pady=(30, 10))

# 🔹 Optional footer text
footer = ctk.CTkLabel(
    master=frame,
    text="Powered by Pratibha's Jarvis AI",
    font=("Arial", 12),
    text_color="#888888"
)
footer.pack(side="bottom", pady=10)

app.mainloop()
