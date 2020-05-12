import socket
import termcolor

PORT = 8081
IP = "127.0.0.1"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("The server is configured!")

num_connections = 0
lista_clientes = []

while num_connections < 5:
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
print("These clients have connected to the server: ")
for i, c in enumerate(lista_clientes):
    print(f"Client {i}: {c}")


ls.close()
