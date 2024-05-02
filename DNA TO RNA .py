dna_nucleotides='GATGGAACTTGACTACGTAAATT'
def dna_to_rna(dna_nucleotides):
    rna_nucleotides=''
    for i in dna_nucleotides:
        rna_nucleotides=dna_nucleotide.replace('T', 'U')
        return rna_nucleotides
print(dna_to_rna(dna_nucleotides))
        