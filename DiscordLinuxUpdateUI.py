import tkinter as tk
import DLU

bgcolor = "#2B2D31"
btbgcolor = "#303446"

window = tk.Tk()
window.title("Discord Update")
window.geometry("300x100")
window.resizable(False, False)
window["background"] = "#2B2D31"

# window.attributes("-topmost", 1)

def update():
    statusLabel["text"] = "Downloading..."

    try:
        DLU.downloadUpdateFile("stable")
        statusLabel["text"] = "Sucess"
    except:
        statusLabel["text"] = "Ooops, something wrong."

headerLabel = tk.Label(
    window, 
    text="Discord Updater", 
    font=("Noto Sans", 20), 
    fg="white", 
    background=bgcolor
)
headerLabel.pack()

statusLabel = tk.Label(
    window, 
    text="", 
    fg="white", 
    background=bgcolor
)
statusLabel.pack()


button = tk.Button(
    window, 
    text="Update",
    background=btbgcolor,
    fg="white", 
    command=update
)
button.configure(width="100")
button.pack()

window.mainloop()