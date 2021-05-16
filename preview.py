import tkinter as tk

root = tk.Tk()

def previewPress():
    label = tk.Label(root, text = "Preview button pressed")
    label.pack()

previewButton = tk.Button(root, text = "Preview", command = previewPress, height = 2, width = 15)
previewButton.pack()

root.mainloop()