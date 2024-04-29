import socket

def kill_gui():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("remote_machine_ip", 8080))  # connect to the GUI machine's socket
    sock.sendall(b"kill")  # send the kill signal
    sock.close()

if __name__ == "__main__":
    kill_gui()
