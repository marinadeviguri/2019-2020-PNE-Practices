from Seq0 import *

FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "U5"]
BASES = ["A", "C", "T", "G"]

for gene in GENES:
    seq = seq_read_fasta(FOLDER + gene + EXT)
    print()
    print(f"Gene {gene}:")
    for base in BASES:
        print(f"  {base}: {seq_count_base(seq, base)}")
