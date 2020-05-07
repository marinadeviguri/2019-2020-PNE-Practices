from Seq1 import Seq

print("----| Practice 1, Exercise 10 |----")
FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
BASES = ['A', 'T', 'C', 'G']

for gene in GENES:

    seq = Seq().read_fasta(FOLDER + gene + EXT)
    counter = seq.seq_count()
    lista = list(counter.values())
    maximnumber = max(lista)

    print("Gene ", gene, ": Most frequent Base: ", BASES[lista.index(maximnumber)])

