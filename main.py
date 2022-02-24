# echo-client.py

from asyncio.windows_events import NULL
import socket
from datetime import datetime
from configparser import ConfigParser

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
errorLevel = ""


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
        errorLevel = ""
        print("ERROR: Invalid selection")

    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    if testType == "MANUAL":
        message = input("Enter log details\n")
    else:
        message = f"{errorLevel} test"
    query = f"?request=LOGTEST&timeStamp={timeStamp}&errorLevel={errorLevel}&message={message}&local_ip={local_ip}&hostname={hostname}"
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
        createLog(1, "AUTOMATED")
        createLog(2, "AUTOMATED")
        createLog(3, "AUTOMATED")
        createLog(4, "AUTOMATED")
    elif choice == "3":
        print("\n ")
    elif choice == "4":
        print("\n Goodbye")
        choice = False
    elif choice != "":
        print("\n Not Valid Choice Try again")
