from pathlib import Path


class Seq:

    def __init__(self, strbases='NULL'):
        if strbases == 'NULL':
            self.strbases = 'NULL'
            print('NULL sequence created')
            return
        else:
            bases = ['A', 'C', 'G', 'T']
            for element in strbases:
                if element not in bases:
                    print('INVALID Seq!')
                    self.strbases = 'ERROR'
                    return

        self.strbases = strbases
        print('New sequence created!')

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        if self.strbases == 'NULL' or self.strbases == 'ERROR':
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        return self.strbases.count(base)

    def seq_count(self):
        dict_bases = {'A': self.count_base('A'), 'C': self.count_base('C'),
                      'T': self.count_base('T'), 'G': self.count_base('G')}
        return dict_bases

    def reverse(self):
        if self.strbases == 'NULL':
            return 'NULL'
        elif self.strbases == 'ERROR':
            return 'ERROR'
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == 'NULL':
            return 'NULL'
        elif self.strbases == 'ERROR':
            return 'ERROR'
        else:
            bases = ['A', 'C', 'T', 'G']
            complement_bases = ['T', 'G', 'A', 'C']
            d = dict(zip(bases, complement_bases))
            complement_seq = ''
            for bases in self.strbases:
                for base, complement in d.items():
                    if bases == base:
                        complement_seq += complement
            return complement_seq

    def read_fasta(self, filename):
        file_contents = Path(filename).read_text().split('\n')[1:]
        self.strbases = "".join(file_contents)
        return self
