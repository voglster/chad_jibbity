import multiprocessing
import threading
import tkinter as tk
from time import sleep
import time

from autocomplete import AutocompleteCombobox
from chadjibbity import send_to_llm
from chat_templates import templates
from clipboard import add_clipboard_label_to_window
from pynput.keyboard import Controller as KeyboardController, Key

from loguru import logger


keyboard = KeyboardController()


def show_form():
    root = tk.Tk()
    root.title("Select an Option")

    talk_label = tk.Label(root, text="Talking to GPT")
    talk_label.pack(pady=10, padx=20)

    timer_label = tk.Label(root, text="0:00")
    timer_label.pack(pady=10, padx=20)

    def update_timer():
        print("starting update timer")
        start_time = time.time()
        while True:
            time_elapsed = int(time.time() - start_time)
            minutes = int(time_elapsed / 60)
            seconds = int(time_elapsed % 60)
            timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            root.update()
            time.sleep(0.1)

    def cancel():
        root.destroy()

    cancel_button = tk.Button(root, text="Cancel", command=cancel)
    cancel_button.pack(pady=10, padx=20)

    talk_label.pack_forget()
    timer_label.pack_forget()
    cancel_button.pack_forget()

    template_label = tk.Label(root, text=templates["Code"], anchor="w", justify="left")
    template_label.pack(pady=10, padx=20)

    clipboard_label = add_clipboard_label_to_window(root)

    combo = AutocompleteCombobox(root)
    combo.set_completion_list(list(templates.keys()))
    combo.pack(pady=20, padx=20)
    combo.set("Code")
    combo.focus_set()

    textbox = tk.Text(root, height=10, wrap=tk.WORD)
    textbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    def send_it():
        talk_label.pack()
        timer_label.pack()
        cancel_button.pack()
        template_label.pack_forget()
        clipboard_label.pack_forget()
        combo.pack_forget()
        textbox.pack_forget()
        root.update()
        threading.Thread(target=update_timer, daemon=True).start()

        content = f"{template_label['text']}\n{clipboard_label['text']}\n{textbox.get(1.0, tk.END)}"
        process = multiprocessing.Process(target=send_to_llm, args=(content,))
        process.start()

        def check_process():
            if process.is_alive():
                root.after(100, check_process)
            else:
                root.withdraw()
                sleep(0.2)
                keyboard.type('gv"+p:w')
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                root.destroy()

        check_process()  # start the check

    def on_select(event):
        selected_option = combo.get()
        template_content = templates.get(selected_option, "")
        template_label.config(text=template_content)
        logger.info(f"Selected: {selected_option}")

    def handle_key_event(event):
        if event.keysym == "Return" and event.state & 0x4:  # Check for Ctrl key
            send_it()

    combo.bind("<<ComboboxSelected>>", on_select)
    combo.bind("<Control-Return>", handle_key_event)
    textbox.bind("<Control-Return>", handle_key_event)
    root.mainloop()
