from client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
print(c)
FOLDER = "../Session-04/"
GENE = "U5"
EXT = ".txt"
s = Seq().read_fasta(FOLDER + GENE + EXT)
c.debug_talk(f"Sending {GENE} Gene to the server...")
c.debug_talk(str(s))
