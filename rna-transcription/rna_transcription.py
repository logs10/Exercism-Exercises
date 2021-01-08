# Given a DNA strand, return its RNA complement (per RNA transcription).

def to_rna(dna_strand):
    complements = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    keyset = ['G', 'C', 'T', 'A']
    rna_strand = ""

    for dna in dna_strand:
        if dna in keyset:
            value = complements.get(dna)
            rna_strand = rna_strand + value
        else:
            raise ValueError('Invalid DNA nucleotides ' +
                             dna + ' in ' + dna_strand)
    return rna_strand


print(to_rna('GCTA'))
