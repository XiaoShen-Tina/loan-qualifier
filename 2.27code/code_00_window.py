# code_00_window.py
import tkinter as tk
# Create the main window
root = tk.Tk()
root.title("My first GUI window")

#Create label
label = tk.Label(
    root,
    text = 'Hello, MGS3001 W01'
)
#Lay out the window
label.pack()
#Run forever
root.mainloop()