import socket

class Socket:
    def __init__(self, host, port, bufsize=8192):
        self.address = (host, port)
        self.bufsize = bufsize
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def send(self, msg, append_null_terminator=True):
        if append_null_terminator:
            msg = msg + "\0"
        self.sock.sendto(msg, self.address)
    
    def recv(self, conform_address=True):
        data, address = self.sock.recvfrom(self.bufsize)
        if conform_address:
            self.address = address
        return data
