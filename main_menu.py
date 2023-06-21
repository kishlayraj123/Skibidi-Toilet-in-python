import tkinter as tk
from PIL import ImageTk, Image
import subprocess

def play_button_clicked():
    file_path = r"C:\Users\SUJEET KUMAR\OneDrive\Desktop\Python_Project\Skibidi_Toilet.py"
    subprocess.Popen(["python", file_path])

def quit_button_clicked():
    root.destroy()

def toggle_buttons():
    play_button_state = play_button.cget("state")
    quit_button_state = quit_button.cget("state")

    play_button.config(state=tk.NORMAL if play_button_state == tk.DISABLED else tk.DISABLED)
    quit_button.config(state=tk.NORMAL if quit_button_state == tk.DISABLED else tk.DISABLED)

    root.after(500, toggle_buttons)

root = tk.Tk()
root.title("Skibidi Toilet")

# Set the desired width and height for the background image
background_width = 1500
background_height = 850

# Load the background image
image = Image.open("image/background.png")
image = image.resize((background_width, background_height), Image.ANTIALIAS)  # Resize the image
background_image = ImageTk.PhotoImage(image)

# Create a Canvas widget and add the background image
canvas = tk.Canvas(root, width=background_width, height=background_height)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=background_image)

play_button = tk.Button(root, text="Play", command=play_button_clicked, font=("Arial", 34), width=7, height=1)
play_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

quit_button = tk.Button(root, text="Quit", command=quit_button_clicked, font=("Arial", 34), width=6, height=1)
quit_button.place(relx=0.56, rely=0.8, anchor=tk.SE)

toggle_buttons()  # Start the flickering effect

root.mainloop()
