from Seq0 import *

FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "U5"]
BASES = ['A', 'C', 'T', 'G']


for gene in GENES:
    seq = seq_read_fasta(FOLDER + gene + EXT)
    print(f"Gene {gene}: {seq_count(seq)}")
