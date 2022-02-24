# echo-client.py

import socket

HOST = "10.169.92.37"  # The server's hostname or IP address
PORT = 13000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"?request=TEST1")
    data = s.recv(1024)

print(f"Received {data!r}")
