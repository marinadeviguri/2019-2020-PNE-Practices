import socket

IP = "127.0.0.1"
PORT = 8080

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.bind((IP, PORT))

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.listen()

print("Server is configured!")


ls.close()
