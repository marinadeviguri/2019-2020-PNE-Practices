from Seq1 import *


FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
BASES = ['A', 'T', 'C', 'G']

print("-----| Practice 7, Exercise 10 |------")

for gene in GENES:
    sequence = Seq().read_fasta(FOLDER + gene + EXT)
    counter = sequence.seq_count()
    lista = list(counter.values())
    maximum = max(lista)

    print("Gene ", gene, ": Most frequent Base:", BASES[lista.index(maximum)])
