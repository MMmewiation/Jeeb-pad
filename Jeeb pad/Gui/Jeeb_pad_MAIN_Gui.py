import tkinter as tk
from functionality import create_dropdown_button 
import functionality as func

# Initialize the main window
window = tk.Tk()
window.title("Jeeb-pad")
window.attributes("-fullscreen", True)
window.configure(bg='#1f1f1f')
window_1_exists = True

project_created = False


def open_file():
    print("Open File")

def save_file():
    if project_created == False:
        func.Save_Error_Popup


def new_file_txt():
    root = tk.Tk()
    root.title("Jeeb-pad")
    root.attributes("-fullscreen", True)
    root.configure(bg='#1f1f1f')
    window.destroy()
    
    window_1_exists = False
    text_box = tk.Text(root, font=("Montserrat", 15), width=1920, height=1080, bg="#1f1f1f", fg="#ffffff")
    text_box.place(x=20,y=0)
    poo_items = {
        "New": {
            "Txt file": lambda: new_file_txt(),
            "Jpb file (jeeb pad file)": lambda: print("Option 2 selected"),
            "Pdf file": lambda: print("pdf file")
        },
        "Open": open_file,
    
    
    }
    file_button = tk.Button(window, text="File", font=("Arial", 10), borderwidth=0, relief="flat", bg="#1f1f1f", fg="#ffffff")
    file_button.place(x=0, y=0)

    create_dropdown_button(window, file_button, poo_items)
    


menu_items = {
    "New": {
        "Txt file": lambda: new_file_txt(),
        "Jpb file (jeeb pad file)": lambda: print("Option 2 selected"),
        "Pdf file": lambda: print("pdf file")
    },
    "Open": open_file,
    
    
}

file_button = tk.Button(window, text="File", font=("Arial", 10), borderwidth=0, relief="flat", bg="#1f1f1f", fg="#ffffff")
file_button.place(x=0, y=0)

create_dropdown_button(window, file_button, menu_items)


jeeb_pad_core_text = """Welcome to
jeeb pad start a proj-
ect to continue or you
can pull from a repo o-
r group project if you
would like to learn all
of the things a detail-
ed guide can be found
by going to "what is 
jeeb pad > how to use"
if you want a video 
guide you can go to 
the offical website
for jeeb-pad """ 

jeeb_pad_core = tk.Label(window, text=jeeb_pad_core_text, font=("Arial", 20), fg="#ffffff", bg="#1f1f1f")
jeeb_pad_core.place(x=0, y=30)

jeeb_pad_core_2 = tk.Label(window, text=jeeb_pad_core_text, font=("Arial", 20), fg="#ffffff", bg="#1f1f1f")
jeeb_pad_core.place(x=0, y=30)

canvas = tk.Canvas(window, width=0, height=1080, bg="#1f1f1f")
canvas.place(x=300, y=0)

x_position = 100
canvas.create_line(x_position, 100, x_position, 190, fill="white", width=2,)



window.mainloop()
