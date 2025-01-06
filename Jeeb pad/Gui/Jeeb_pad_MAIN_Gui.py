import tkinter as tk
from tkinter import filedialog
import os



window = tk.Tk()
window.title("Jeeb-pad")
window.attributes("-fullscreen", True)
window.configure(bg='#1f1f1f')
window_1_exists = True

canvas = tk.Canvas(window, width=1920, height=1080, bg="#1f1f1f", bd=0, highlightthickness=0, relief='flat')
canvas.pack()

canvas.create_line(309, 0, 309, 1080, fill="white", width=2)


project_created = False

selected_folder = tk.StringVar
selected_folder = ("Nothing")


def open_file(text_widget):
    filepath = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    if filepath:
        with open(filepath, "r") as f:
            text_content = f.read()

        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, text_content)

        root = tk.Tk()
        root.title("Jeeb-pad")
        root.attributes("-fullscreen", True)
        root.configure(bg='#1f1f1f')

        text_box = tk.Text( root, font=("Montserrat", 15),width=1920,height=1080,bg="#1f1f1f",fg="#ffffff")
        text_box.place(x=0, y=25)

        save_button = tk.Button(root, text="Save",font=("Arial", 10),borderwidth=0,relief="flat",g="#1f1f1f",fg="#ffffff",command=lambda: save_file(text_box, filepath))
        save_button.place(x=0, y=0)

        text_box.insert(tk.END, text_content)

        window.destroy

        root.mainloop()


def save_file(text_widget, filepath=None):
    if filepath:
        text_content = text_widget.get("1.0", tk.END)
        with open(filepath, "w") as f:
            f.write(text_content)
    else:
        filepath_prompt = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )
        if filepath_prompt:
            text_content = text_widget.get("1.0", tk.END)
            with open(filepath_prompt, "w") as f:
                f.write(text_content)


def new_file_txt():
    root = tk.Tk()
    root.title("Jeeb-pad")
    root.attributes("-fullscreen", True)
    root.configure(bg='#1f1f1f')

    text_box = tk.Text(root,font=("Montserrat", 15),width=1920,height=1080,bg="#1f1f1f",fg="#ffffff"
    )
    text_box.place(x=0, y=25)


    save_button = tk.Button( root, text="Save", font=("Arial", 10), borderwidth=0, relief="flat", bg="#1f1f1f",fg="#ffffff", command=lambda: save_file(text_box, None))
    save_button.place(x=0, y=0)

    window.destroy
    root.mainloop()
    





file_button = tk.Button(window, text="Create text file", font=("Arial", 10), borderwidth=0, relief="flat", bg="#1f1f1f", fg="#ffffff", command=new_file_txt)
file_button.place(x=0, y=0)

text_widget = tk.Text(window, font=("Montserrat", 15), width=1920, height=1080, bg="#1f1f1f", fg="#ffffff")
file_button = tk.Button(window, text="Open text file", font=("Arial", 10), borderwidth=0, relief="flat", bg="#1f1f1f", fg="#ffffff", command=lambda: open_file(text_widget))  
file_button.place(x=100, y=0)

file_text = tk.Label(window, text="Create new PDF", font=("Arial", 10), borderwidth=0, relief="flat", bg="#1f1f1f", fg="#878787")
file_text.place(x=200, y=3)

jeeb_pad_core_text = """Welcome to
jeeb pad There will be 
stuff here 
later when it
leaves early 
acsess""" 

jeeb_pad_core = tk.Label( window, text=jeeb_pad_core_text, font=("Arial", 20), fg="#ffffff", bg="#1f1f1f")
jeeb_pad_core.place(x=0, y=30)

jeeb_pad_random = tk.Label(window, text=jeeb_pad_core_text, font=("Arial", 20), fg="#ffffff", bg="#1f1f1f")
jeeb_pad_random.place(x=900, y=30)






window.mainloop()
