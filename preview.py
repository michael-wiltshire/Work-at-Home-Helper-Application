import tkinter as tk

root = tk.Tk()

def previewPress():
    label = tk.Label(root, text = "Preview button pressed")
    label.pack()

def exportPress():
    label = tk.Label(root, text = "Export button pressed")
    label.pack()

previewButton = tk.Button(root, text = "Preview", command = previewPress, height = 3, width = 15)
previewButton.pack()

exportButton = tk.Button(root, text = "Export", command = exportPress, height = 3, width = 15)
exportButton.pack()

root.mainloop()
