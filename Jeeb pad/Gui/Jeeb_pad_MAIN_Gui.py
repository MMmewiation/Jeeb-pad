import tkinter as tk
from functionality import change_bg_mode


window = tk.Tk()
window.title("Jeeb-pad")

window.attributes("-fullscreen", True)


new_file = tk.Button(window, text="button", font=("Arial", 10), borderwidth=0, relief="flat", command=lambda: change_bg_mode(window))
new_file.place(x=0, y=0)

color_mode = tk.Button(window, text="button", font=("Arial", 20), borderwidth=0, relief="flat", command=lambda: change_bg_mode(window))
color_mode.place(x=1830, y=0)


jeeb_pad_core = tk.Label(window, text="Jeeb", font=("Arial", 20))
jeeb_pad_core.place(x=0, y=30)


window.mainloop()
