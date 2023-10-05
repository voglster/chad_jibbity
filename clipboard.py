import subprocess
import tkinter as tk
from tkinter import ttk


def set_clipboard(data):
    process = subprocess.Popen(["xclip", "-selection", "c"], stdin=subprocess.PIPE)
    process.communicate(data.encode("utf-8"))


def get_clipboard_content(root):
    """Retrieve the clipboard content."""
    try:
        return root.clipboard_get()
    except tk.TclError:
        return ""


def add_clipboard_label_to_window(root):
    """Add a label to the window displaying the clipboard content."""
    clipboard_text = get_clipboard_content(root)
    label = ttk.Label(
        root,
        text=clipboard_text,
        anchor="w",
        justify="left",
        width=100,  # Adjust this value as needed
        font=("Courier", 10),  # Set the font to 'Courier' with size 10
    )
    label.pack(pady=10, padx=20, fill="x")
    return label
