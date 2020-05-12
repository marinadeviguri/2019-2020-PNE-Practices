import socket
import termcolor

PORT = 8080
IP = "192.168.124.179"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
num_connections = 0

print("The server is configured!")

while True:
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        num_connections += 1
        print(f"CONNECTION {num_connections}. Client IP,PORT: {client_ip_port}")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        print("Message received: ", end="")
        termcolor.cprint(msg, "green")
        response = "ECHO: " + msg + "\n"
        cs.send(response.encode())
        cs.close()
