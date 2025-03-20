import tkinter as tk
import os
from tkinter import filedialog
import sys
import winreg
import tkinter.font as tkFont
from tkinter import Tk
import webview



window = tk.Tk()
window.title("Jeeb Pad")
window.geometry("600x400")
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

icon_path = os.path.join(base_path, "JeebPad.ico")
window.iconbitmap(icon_path)

SavedFile = False
SavedFile2 = False
fonts = sorted(tkFont.families())
selected_font = tk.StringVar(window)
selected_font.set("Arial") 
IsDarkMode = tk.IntVar()

def ShowTut():
    html_content = """
    <html>
    <head>
        <title>Jeeb pad setup</title>
    </head>
    <body>
        <style>
            body {
                text-align: center;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
        </style>
        <h1>Please set up jeeb pad</h1>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/jzVJVBLUUZ4" 
        frameborder="0" allowfullscreen></iframe>
        <p>If you installed jeeb pad please follow the video or right click a .txt file (or any other file format that utelized the text format) and then click open with than click choose another app and scroll all the way down and click choose an app on your pc than it will open a file explorer window, than set the file path at the top to C:\Program Files (x86)\Meowsin Studios\Jeeb pad and select JeebPad.exe and click open, than select always</p>
    </body>
    </html>
    """
    window = webview.create_window("Jeeb Pad Setup", html=html_content)
    webview.start()
    window = tk.Tk()
    window = tk.Toplevel()
    window.title("Edit")
    window.geometry("600x400")
    text = window(text='Please follow the instruction, if you dont want to click "i dont want to"')
    text.pack()
    Button = window(text="I dont want to", command=NO)
    Button.pack()
def add_registry_entry():
    try:
        base_key = winreg.HKEY_CURRENT_USER
        class_path = r"Software\Classes\SystemFileAssociations\.txt\shell\JeebPad"
        command_path = class_path + r"\command"

        key = winreg.CreateKey(base_key, class_path)
        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "Open with Jeeb Pad")
        winreg.CloseKey(key)

        key = winreg.CreateKey(base_key, command_path)
        script_path = os.path.abspath(sys.argv[0])
        command = f'"{sys.executable}" "{script_path}" "%1"'
        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, command)
        winreg.CloseKey(key)
        print("Registry entry added successfully.")
    except Exception as e:
        print("Error adding registry entry:", e)

def registry_entry_exists():
    try:
        base_key = winreg.HKEY_CURRENT_USER
        class_path = r"Software\Classes\SystemFileAssociations\.txt\shell\JeebPad"
        key = winreg.OpenKey(base_key, class_path)
        winreg.CloseKey(key)
        return True
    except FileNotFoundError:
        return False

def process_file(filepath):
    if os.path.isfile(filepath):
        try:
            with open(filepath, 'r') as file:
                content = file.read()
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, content)
        except Exception as e:
            print("Error reading file:", e)
    else:
        print(f"Error: {filepath} is not a valid file.")

def Save():
    global SavedFile, filepath_prompt, file_path, SavedFile2
    text_content = text_widget.get("1.0", tk.END)
    if SavedFile:
        with open(filepath_prompt, "w") as file:
            file.write(text_content)
    elif SavedFile2:
        with open(file_path, "w") as file:
            file.write(text_content)
    else:
        save_file()

def save_file(filepath=None):
    global filepath_prompt, SavedFile
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
            SavedFile = True
            print("Saved file:", SavedFile, "Path:", filepath_prompt)

def open_file():
    global file_path, SavedFile2
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, content)
        SavedFile2 = True




def Edit():
    global text_widget
    window = tk.Toplevel()
    window.title("Edit")
    window.geometry("600x400")
    try:
        window.iconbitmap('JeebPad.ico')
    except Exception as e:
        print(e)



    Customization = tk.Label(window, text="Cutomization", font=("Arial", 25), borderwidth=0)
    Customization.pack()
    fontTTTTT = tk.Label(window, text="Font", font=("Arial", 15), width=6, height=1, borderwidth=0)
    fontTTTTT.pack()
    fonts = sorted(tkFont.families())
    selected_font = tk.StringVar(window)
    if "Arial" in fonts:
        selected_font.set("Arial")
    else:
        selected_font.set(fonts[0])
    option_menu = tk.OptionMenu(window, selected_font, *fonts)
    option_menu.config(width=10, font=(selected_font.get(), 12), fg="black", borderwidth=1)
    option_menu.pack()
    def on_font_change(*args):
        font_name = selected_font.get()
        option_menu.config(font=(font_name, 12), fg="black")
        print("Selected Font:", font_name)
        text_widget.config(font=(selected_font.get(), 12))
    selected_font.trace("w", on_font_change)
    


button_frame = tk.Frame(window)
button_frame.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)  

text_widget = tk.Text(window, font=(selected_font, 10))
text_widget.pack(fill=tk.BOTH, expand=True)



save_button = tk.Button(button_frame, text="Save", font=("Arial", 8), width=6, height=1, padx=5, pady=5,  borderwidth=0, bg="#ffffff", command=lambda: Save(text_widget))
save_button.pack(side=tk.LEFT, padx=5)
open_button = tk.Button(button_frame, text="Open", font=("Arial", 8), width=6, height=1, padx=5, pady=5, borderwidth=0, bg="#ffffff", command=open_file)
open_button.pack(side=tk.LEFT, padx=5)
saveas_button = tk.Button(button_frame, text="Save as", font=("Arial", 8), width=6, height=1, padx=5, pady=5,  borderwidth=0, bg="#ffffff", command=lambda: save_file(text_widget, None))
saveas_button.pack(side=tk.LEFT, padx=5)
edit_button = tk.Button(button_frame, text="Edit", font=("Arial", 8), width=6, height=1, padx=5, pady=5, borderwidth=0, bg="#ffffff", command=Edit)
edit_button.pack(side=tk.LEFT, padx=5)

def delete_registry_entry():
    try:
        base_key = winreg.HKEY_CURRENT_USER
        class_path = r"Software\Classes\SystemFileAssociations\.txt\shell\JeebPad"
        command_path = class_path + r"\command"

        winreg.DeleteKey(base_key, command_path)
        winreg.DeleteKey(base_key, class_path)
        print("Registry entry deleted successfully.")
    except FileNotFoundError:
        print("Registry entry not found; nothing to delete.")
    except Exception as e:
        print("Error deleting registry entry:", e)



if __name__ == "__main__":
    if not registry_entry_exists():
        add_registry_entry()
        ShowTut()
    else:
        print("Registry entry already exists.")


    if len(sys.argv) > 1:
        target_file = sys.argv[1]
        process_file(target_file)
    else:
        print("No file provided via 'Open with'.")

#this is commented out because its not for release
DevModeOption = input("Enter (1) to delete registry entry: ")
try:
    if int(DevModeOption) == 1:
        delete_registry_entry()
except ValueError:
    print("Invalid input. Please enter a number.")



window.mainloop()
