from pathlib import Path


def seq_ping():
    print("OK")


def seq_read_fasta(filename):
    contents = Path(filename).read_text()
    body = contents.split('\n')[1:]
    return "".join(body)


def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
    return seq.count(base)


def seq_count(seq):
    res = {'A': seq_count_base(seq, 'A'), 'T': seq_count_base(seq, 'T'),
           'C': seq_count_base(seq, 'C'), 'G': seq_count_base(seq, 'G')}
    return res


def seq_perc(seq):
    num = seq_count(seq)
    for b in ['A', 'T', 'C', 'G']:
        num[b] = round(100.0 * num[b] / seq_len(seq), 1)
    return num


def seq_reverse(seq):
    return seq[::-1]


def seq_complement(sequence):
    bases = ['A', 'C', 'T', 'G']
    complement_bases = ['T', 'G', 'A', 'C']
    d = dict(zip(bases, complement_bases))
    complement_seq = ''
    for bases in sequence:
        for base, complement in d.items():
            if bases == base:
                complement_seq += complement
    return complement_seq


