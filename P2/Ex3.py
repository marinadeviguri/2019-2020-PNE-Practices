from client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "87.223.31.172"
PORT = 8080
c = Client(IP, PORT)
print(c)
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print("Response: ", response)
