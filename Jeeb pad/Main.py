import tkinter as tk
import os
from tkinter import filedialog
import sys

window = tk.Tk()
window.title("Jeeb Pad")
window.geometry("600x400")
window.iconbitmap('JeebPad.ico') 

exit = False
SavedFile = False
SavedFile2 = False

import os
import sys
import winreg

# def add_registry_entry():
#     try:
#         base_key = winreg.HKEY_CURRENT_USER
#         class_path = r"Software\Classes\Directory\shell\JeebPad"
#         command_path = class_path + r"\command"

#         key = winreg.CreateKey(base_key, class_path)
#         winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "Open with Jeeb Pad")
#         winreg.CloseKey(key)

#         key = winreg.CreateKey(base_key, command_path)
#         script_path = os.path.abspath(sys.argv[0])
#         command = f'"{sys.executable}" "{script_path}" "%1"'
#         winreg.SetValueEx(key, "", 0, winreg.REG_SZ, command)
#         winreg.CloseKey(key)
#         print("Registry entry added successfully.")
#     except Exception as e:
#         print("Error adding registry entry:", e)

# def registry_entry_exists():
#     try:
#         base_key = winreg.HKEY_CURRENT_USER
#         class_path = r"Software\Classes\Directory\shell\JeebPad"
#         key = winreg.OpenKey(base_key, class_path)
#         winreg.CloseKey(key)
#         return True
#     except FileNotFoundError:
#         return False

# def process_directory(directory):
#     if os.path.isdir(directory):
#         print(f"Processing directory: {directory}")
#         with open(directory, 'r') as file:
#             global SavedFile2
#             content = file.read()
#             # Clear the text widget and insert the file content
#             text_widget.delete("1.0", tk.END)
#             text_widget.insert(tk.END, content)
#             SavedFile2 = True
#     else:
#         print(f"Error: {directory} is not a valid directory.")

# def main():
#     if len(sys.argv) < 2:
#         print("Usage: python your_app.py <directory>")
#         return

#     directory = sys.argv[1]
#     process_directory(directory)


def Save(text_widget):
    Text = text_widget.get("1.0", tk.END)


    print(SavedFile)
    if SavedFile == True:
        with open(filepath_prompt, "w") as file:
            file.write(Text)
    elif SavedFile2 == True:
        with open(file_path, "w") as file:
            file.write(Text)
    
    else:
        save_file(text_widget)


def save_file(text_widget, filepath=None):

    global filepath_prompt
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
                global SavedFile
                SavedFile = True
                print("saved file:", SavedFile, "also", filepath_prompt)




def open_file():
    global file_path
    # Open a file dialog to select a file
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, 'r') as file:
            global SavedFile2
            content = file.read()
            # Clear the text widget and insert the file content
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, content)
            SavedFile2 = True
# def Edit():
#     print("edit opened")

#     root = tk.Tk()\

\

#     root.title("Jeeb-pad")
#     root.geometry("600x400")
#     root.iconbitmap('JeebPad.ico') 



#     root.mainloop()

button_frame = tk.Frame(window)
button_frame.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)


text_widget = tk.Text(window, font=("Arial", 10))
text_widget.pack(fill=tk.BOTH, expand=True)

save_button = tk.Button(button_frame, text="Save", font=("Arial", 8), width=6, height=1, padx=5, pady=5,  borderwidth=0, bg="#ffffff", command=lambda: Save(text_widget))

save_button.pack(side=tk.LEFT, padx=5)


open_button = tk.Button(button_frame, text="Open", font=("Arial", 8), width=6, height=1, padx=5, pady=5, borderwidth=0, bg="#ffffff", command=open_file)
# exit_button = tk.Button(button_frame, text="Edit", font=("Arial", 8), width=6, height=1, padx=5, pady=5, borderwidth=0, bg="#ffffff",command=Edit)


open_button.pack(side=tk.LEFT, padx=5)
# exit_button.pack(side=tk.LEFT, padx=5)

saveas_button = tk.Button(button_frame, text="Save as", font=("Arial", 8), width=6, height=1, padx=5, pady=5,  borderwidth=0, bg="#ffffff", command=lambda: save_file(text_widget, None))

saveas_button.pack(side=tk.LEFT, padx=5)

# if __name__ == "__main__":
#     if not registry_entry_exists():
#         add_registry_entry()
#     else:
#         print("Registry entry already exists.")


#     if len(sys.argv) > 1:
#         target_directory = sys.argv[1]
#         process_directory(target_directory)
#     else:
#         print("Not ran with 'open with'")



window.mainloop()

