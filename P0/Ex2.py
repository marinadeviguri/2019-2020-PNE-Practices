from Seq0 import *

FOLDER = "../Session-04/"
FILENAME = "U5.txt"
DNA_FILE = FOLDER + FILENAME

seq = seq_read_fasta(DNA_FILE)
print("DNA file: ", FILENAME)
print("The first 20 bases are: ")
print(seq[:20])
