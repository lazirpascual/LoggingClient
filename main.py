# echo-client.py

from asyncio.windows_events import NULL
import socket
from datetime import datetime
from configparser import ConfigParser
import time
import os

configuration = ConfigParser()
configuration.read('config.ini')


HOST = configuration['Address']['IP_address']
PORT = configuration['Address']['PORT']


def socketConnection(queryString):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, int(PORT)))
        s.sendall(queryString)
        data = s.recv(1024)
        print(f"{data!r}")


choice = True
timeStamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")


def createLog(level, testType):

    if testType == "MANUAL":
        print("""
        1. INFO
        2. WARNING
        3. ERROR
        4. FATAL
        """)
        level = int(input("Please select your log level "))

    if level == 1:
        errorLevel = "INFO"
    elif level == 2:
        errorLevel = "WARNING"
    elif level == 3:
        errorLevel = "ERROR"
    elif level == 4:
        errorLevel = "FATAL"
    else:
        errorLevel = "INVALID"
        print("ERROR: Invalid selection")

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    if testType == "MANUAL" and errorLevel != "INVALID":
        message = input("Enter log details\n")
    elif errorLevel == "INVALID":
        message = "Invalid selection from the menu"
    else:
        message = f"{errorLevel} test"

    query = f"?request=LOGGING&errorLevel={errorLevel}&message={message}&local_ip={local_ip}" \
            f"&hostname={hostname}"
    socketConnection(bytes(query, "utf-8"))


while choice:
    print("""
    1. Test Logging Service
    2. Automated Test
    3. Abuse Test
    4. Exit/Quit
    """)
    choice = input("What would you like to do? ")
    if choice == "1":
        createLog(NULL, "MANUAL")
    elif choice == "2":
        print("Testing with INFO level message")
        createLog(1, "AUTOMATED")
        time.sleep(1)

        print("\n\nTesting with WARNING level message")
        createLog(2, "AUTOMATED")
        time.sleep(1)

        print("\n\nTesting with ERROR level message")
        createLog(3, "AUTOMATED")
        time.sleep(1)

        print("\n\nTesting with FATAL level message")
        createLog(4, "AUTOMATED")
        time.sleep(1)

        print("\n\nTesting with INVALID selection")
        createLog(5, "AUTOMATED")
        time.sleep(1)
    elif choice == "3":
        print("\n ")
    elif choice == "4":
        print("\n Goodbye")
        choice = False
    elif choice != "":
        print("\n Not Valid Choice Try again")
