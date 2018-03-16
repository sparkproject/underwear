import socket

def run(**args):
    ip = socket.gethostbyname(socket.gethostname())
    #print(ip)
    return ip
