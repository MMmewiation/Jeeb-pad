import tkinter as tk
from functionality import create_dropdown_button 
import functionality as func
from tkinter import messagebox
from tkinter import filedialog
import os


# Initialize the main window
window = tk.Tk()
window.title("Jeeb-pad")
window.attributes("-fullscreen", True)
window.configure(bg='#1f1f1f')
window_1_exists = True

project_created = False

selected_folder = tk.StringVar
selected_folder = ("Nothing")

def open_file():
    print("Open File")
    openpath = filedialog.askopenfile

def save_file(text_widget):
    # Prompt for filename
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    if filepath:
        # Write the text from the widget to the chosen file
        text_content = text_widget.get("1.0", tk.END)
        with open(filepath, "w") as f:
            f.write(text_content)

def new_file_txt():
    root = tk.Tk()
    root.title("Jeeb-pad")
    root.attributes("-fullscreen", True)
    root.configure(bg='#1f1f1f')

    # Create a text widget
    text_box = tk.Text(
        root,
        font=("Montserrat", 15),
        width=1920,
        height=1080,
        bg="#1f1f1f",
        fg="#ffffff"
    )
    text_box.place(x=0, y=25)

    # Create a save button
    save_button = tk.Button(
        root,
        text="Save",
        font=("Arial", 10),
        borderwidth=0,
        relief="flat",
        bg="#1f1f1f",
        fg="#ffffff",
        command=lambda: save_file(text_box)
    )
    save_button.place(x=0, y=0)

    # Start the Tk event loop
    root.mainloop()




    



    


file_button = tk.Button(window, text="Create text file", font=("Arial", 10), borderwidth=0, relief="flat", bg="#1f1f1f", fg="#ffffff", command=new_file_txt)
file_button.place(x=0, y=0)

file_button = tk.Button(window, text="Open", font=("Arial", 10), borderwidth=0, relief="flat", bg="#1f1f1f", fg="#ffffff", command=new_file_txt)
file_button.place(x=100, y=0)


file_text = tk.Label(window, text="Create new PDF", font=("Arial", 10), borderwidth=0, relief="flat", bg="#1f1f1f", fg="#878787")
file_text.place(x=150, y=3)

jeeb_pad_core_text = """Welcome to
jeeb pad There will be 
stuff here 
later when it
leaves early 
acsess""" 

jeeb_pad_core = tk.Label(window, text=jeeb_pad_core_text, font=("Arial", 20), fg="#ffffff", bg="#1f1f1f")
jeeb_pad_core.place(x=0, y=30)


jeeb_pad_random = tk.Label(window, text=jeeb_pad_core_text, font=("Arial", 20), fg="#ffffff", bg="#1f1f1f")
jeeb_pad_random.place(x=900, y=30)

canvas = tk.Canvas(window, width=0, height=1080, bg="#1f1f1f")
canvas.place(x=300, y=0)

x_position = 100
canvas.create_line(x_position, 100, x_position, 190, fill="white", width=2,)



window.mainloop()
