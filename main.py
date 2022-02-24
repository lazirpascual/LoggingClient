# echo-client.py

import socket

HOST = "10.169.92.182"  # The server's hostname or IP address
PORT = 13000  # The port used by the server


def socketConnection():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"?request=TEST1")
        data = s.recv(1024)
        print(f"Received {data!r}")


choice = True
while choice:
    print("""
    1. Test Logging Service
    2. Automated Test
    3. Abuse Test
    4. Change Log Format
    5. Exit/Quit
    """)
    choice = input("What would you like to do? ")
    if choice == "1":
        socketConnection()
    elif choice == "2":
        print("\n ")
    elif choice == "3":
        print("\n ")
    elif choice == "4":
        print("\n ")
    elif choice == "5":
        print("\n Goodbye")
        choice = False
    elif choice != "":
        print("\n Not Valid Choice Try again")
