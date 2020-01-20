import socket
import sys

class CreateTcpServer():
    def start_tcp_socket(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server_address = (ip, port)
        print("start listen on ip %s, port %s") % self.server_address
        self.sock.bind()

        try:
            self.sock.listen(1)
        except socket.error as e:
            print("fail to listen on port %s") % e
            sys.exit(1)
        while True:
            print
            "waiting for connection"
            client, addr = self.sock.accept()
            client.send("{get out}")
            client.close()

if __name__ == '__main__':
    create = CreateTcpServer()
    create.start_tcp_socket("10.10.10.33", 8998)