import socket
import termcolor


class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    @staticmethod
    def ping():
        print("OK!")

    def __str__(self):
        return f"Connection to SERVER at {self.ip}, PORT: {self.port}"

    def debug_talk(self, msg_to_server):
        msg_from_server = self.talk(msg_to_server)
        print("To Server: ", end="")
        termcolor.cprint(msg_to_server, "blue")
        print("From Server: ", end="")
        termcolor.cprint(msg_from_server, "green")
        return msg_from_server

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8")
        s.close()
        return response
