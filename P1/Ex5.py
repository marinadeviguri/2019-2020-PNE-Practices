from Seq1 import Seq

print("----| Practice 1, Exercise 5 |----")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

for i, s in enumerate([s1, s2, s3]):
    print(f"Sequence {i}: (Length: {s.len()}) {s}")
    for b in ['A', 'C', 'T', 'G']:
        print(f"  {b}: {s.count_base(b)}", end=", ")
    print()

