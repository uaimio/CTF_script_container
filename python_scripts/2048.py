import socket
 
class Netcat:
    # Python 'netcat like' module

    def __init__(self, ip, port):
        self.buff = b''
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length=1024):
        # Read 1024 bytes off the socket
        return self.socket.recv(length)
 
    def read_all(self, data=b'\n'):
        # Read data into the buffer until we have data
        while not data in self.buff:
            self.buff += self.socket.recv(1024)

        print('DEBUG=')
        print(self.buff)
        #pos = self.buff.find(data)
        #rval = self.buff[:pos + len(data)]
        #self.buff = self.buff[pos + len(data):]
 
        return self.buff
 
    def write(self, data):
        self.socket.send(data)
    
    def close(self):
        self.socket.close()

def main():
    to_send = b''

    nc = Netcat('2048.challs.olicyber.it', 10007)
    s = nc.read().split(b'\n')[2]
    print(s)
    
    for _ in range(2049):
        l = [i for i in s.split(b' ')]
        if l[0] == b'SOMMA':
            to_send = int(l[1].decode("utf-8")) + int(l[2].decode("utf-8"))
        elif l[0] == b'DIFFERENZA':
            to_send = int(l[1].decode("utf-8")) - int(l[2].decode("utf-8"))
        elif l[0] == b'PRODOTTO':
            to_send = int(l[1].decode("utf-8")) * int(l[2].decode("utf-8"))
        elif l[0] == b'POTENZA':
            to_send = int(l[1].decode("utf-8")) ** int(l[2].decode("utf-8"))
        elif l[0] == b'DIVISIONE_INTERA':
            to_send = int(int(l[1].decode("utf-8")) / int(l[2].decode("utf-8")))


        to_send = (str(to_send)).encode()
        nc.write(to_send + b'\n')
        s = nc.read().rsplit(b'\n')[0]
        print(s)


if __name__ == '__main__':
    main()