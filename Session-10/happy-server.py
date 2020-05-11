import socket

IP = "127.0.0.1"
PORT = 8080

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.bind((IP, PORT))

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.listen()
print("Server is configured!")

while True:


    try:
        # --- Step 4: Wait for client to connect
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server is done!")
        ls.close()
        exit()
    else:
        # --- Step 5: Receiving information from the client
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()

        print(f"Received message: ¨{msg}")

    # --- Step 6: Send a response message to the client
    response = "Hi! I am a happy server\n"
    cs.send(response.encode())
    cs.close()


