# echo-client.py

import socket
from datetime import datetime

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 13000  # The port used by the server


def socketConnection(queryString):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(queryString)
        data = s.recv(1024)
        print(f"Received {data!r}")


choice = True
timeStamp = datetime.now().strftime("%m/%d/%Y,%H:%M:%S")
errorLevel = ""


def createLog():
    print("""
        1. INFO
        2. WARNING
        3. ERROR
        4. FATAL
        """)
    level = input("Please select your log level ")

    if level == "1":
        errorLevel = "INFO"
        # print(errorLevel)
    elif level == "2":
        errorLevel = "WARNING"
        # print(errorLevel)
    elif level == "3":
        errorLevel = "ERROR"
        # print(errorLevel)
    elif level == "4":
        errorLevel = "FATAL"
        # print(errorLevel)
    else:
        errorLevel = ""
        print("ERROR: Invalid selection")

    message = input("Enter log details\n")
    query = f"?request=LOGTEST&timeStamp={timeStamp}&errorLevel={errorLevel}&message={message}"
    socketConnection(bytes(query, "utf-8"))


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
        createLog()
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
