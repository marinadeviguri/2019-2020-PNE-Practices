from Seq0 import *

PRACTICE = 8
FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
BASES = ['A', 'T', 'C', 'G']


for gene in GENES:
    seq = seq_read_fasta(FOLDER + gene + EXT)
    d = seq_count(seq)
    ll = list(d.values())
    m = max(ll)
    print(f"Gene {gene}: Most frequent Base: {BASES[ll.index(m)]}")