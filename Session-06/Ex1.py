class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        bases = ['A', 'C', 'G', 'T']
        self.strbases = strbases
        for base in strbases:
            if base not in bases:
                print("ERROR!!")
                self.strbases = "ERROR"
                return
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

# - main program
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")

print("Sequence 1: ", s1)
print("Sequence 2: ", s2)
