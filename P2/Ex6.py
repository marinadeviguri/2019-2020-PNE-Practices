from client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print("-----| Practice ", PRACTICE, "Exercise ", EXERCISE, " |------")

IP = "127.0.0.1"
PORT = 8080

FOLDER = "../Session-04/"
EXT = ".txt"
GENE = "FRAT1"

c = Client(IP, PORT)
print(c)
s = Seq().read_fasta(FOLDER + GENE + EXT)
bases = str(s)

print(f"Gene {GENE}: {bases}")
LENGTH = 10

c.talk(f"Sending {GENE} Gene to the server, in fragments of {LENGTH} bases...")
for i in range(5):
    frag = bases[i*LENGTH:(i+1)*LENGTH]
    print(f"Fragment {i+1}: {frag}")
    c.talk(f"Fragment {i+1}: {frag}")
