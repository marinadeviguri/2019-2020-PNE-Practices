class Seq:
    def __init__(self, strbases):

        self.strbases = strbases

    def get_strbases(self):
        return self.strbases

    def len(self):
        tl = len(self.strbases)
        return tl

    def count(self, base):
        return self.strbases.count(base)

    def perc(self, base):
        if len(self.strbases) < 0:
            return "Not a valid sequence"

        elif len(self.strbases) > 0:
            perc= round(100.0 * self.strbases.count(base) / len(self.strbases), 1)
            return perc

    def complement(self):
        r = ""
        for i in self.strbases:
            if i == "A":
                r+="T"
            elif i == "T":
                r+="A"
            elif i == "C":
                r+="G"
            elif i == "G":
                r+="C"

        return str

    def reverse(self):
        return (self.strbases[::-1])
