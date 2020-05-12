from P2 .client0 import Client

PORT = 8081
IP = "127.0.0.1"

for i in range(0, 5):
    c = Client(IP, PORT)
    c.debug_talk(f"Message: {i}")
