import tkinter as tk
from tkinter import ttk


class AutocompleteCombobox(ttk.Combobox):
    def set_completion_list(self, completion_list):
        self._completion_list = sorted(
            completion_list, key=str.lower
        )  # Work with a sorted list
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind("<KeyRelease>", self.handle_keyrelease)
        self["values"] = self._completion_list
        self._autocomplete_mode = False

    def autocomplete(self, delta=0):
        """Autocomplete the Combobox."""
        if not self._autocomplete_mode:
            return

        if (
            delta
        ):  # need to delete selection otherwise we would fix the current position
            self.delete(self.position, tk.END)
        else:  # set position to end so selection starts where text entry ended
            self.position = len(self.get())

        # Collect hits
        _hits = []
        for item in self._completion_list:
            if item.lower().startswith(self.get().lower()):
                _hits.append(item)

        # If we have a new hit list, keep this in mind
        if _hits != self._hits:
            self._hit_index = 0
            self._hits = _hits

        # Only allow cycling if we are in a known hit list
        if _hits == self._hits and self._hits:
            self._hit_index = (self._hit_index + delta) % len(self._hits)

        # Now on to the actual auto completion
        if self._hits:
            self._autocomplete_mode = True
            self.delete(0, tk.END)
            self.insert(0, self._hits[self._hit_index])
            self.select_range(self.position, tk.END)

    def handle_keyrelease(self, event):
        """Event handler for the keyrelease event on this widget."""
        if event.keysym == "BackSpace":
            self.delete(self.index(tk.INSERT), tk.END)
            self.position = self.index(tk.END)
            self._autocomplete_mode = False
        if event.keysym == "Left":
            self.delete(self.index(tk.INSERT), tk.END)
            self.position = self.index(tk.END)
            self._autocomplete_mode = False
        if event.keysym == "Right":
            self.position = self.index(tk.END)  # Go to end (no selection)
            self._autocomplete_mode = False
        if len(event.keysym) == 1:
            self.autocomplete()
