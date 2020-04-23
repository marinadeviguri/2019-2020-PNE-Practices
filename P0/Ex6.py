from Seq0 import *

FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "U5"]
BASES = ['A', 'C', 'T', 'G']

GENE = GENES[0]
print(f"Gene {GENE}:")
seq = seq_read_fasta(FOLDER + GENE + EXT)[:20]
rev = seq_reverse(seq)
print("Frag", seq)
print("Rev", rev)
