import tkinter as tk

def create_dropdown_button(window, button, menu_items):
    
    dropdown_menu = tk.Menu(window, tearoff=0)

    def add_items(menu, items):
        for name, command_or_submenu in items.items():
            if isinstance(command_or_submenu, dict): 
                submenu = tk.Menu(menu, tearoff=0)
                add_items(submenu, command_or_submenu)
                menu.add_cascade(label=name, menu=submenu)
            else:  
                menu.add_command(label=name, command=command_or_submenu)

    add_items(dropdown_menu, menu_items)

    button.config(command=lambda: dropdown_menu.post(button.winfo_rootx(), button.winfo_rooty() + button.winfo_height()))

def Save_Error_Popup():
    popup = tk.Toplevel(root)  # Create a new window
    popup.title("Popup Window")
    popup.geometry("200x100")  # Set the size of the popup

    # Add a label to the popup
    label = tk.Label(popup, text="ERROR: Please create a project before you try to save.")
    label.pack(pady=10)

    # Add a close button
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=5)

