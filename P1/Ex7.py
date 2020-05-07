from Seq1 import Seq

print("----| Practice 1, Exercise 7 |----")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

for a, b in enumerate([s1, s2, s3]):
    print("Sequence ", a, ": (Length: ", b.len(), ")", b)
    print("  Bases: ", b.seq_count())
    print("  Rev:   ", b.reverse())
