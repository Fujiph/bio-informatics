import random

DNA_nuc = ['A', 'T', 'C', 'G']
DNA_comp = {'A':'T', 'T':'A', }

#1.Check DNA sequence
def validateSeq(seq):
    tmpseq = seq.uppper()


def countNucFrequency(seq):
    nuc_freq = {'A':0 ,'T':0, 'C':0, }
    
    for nuc in seq:
        nuc_freq[nuc] += 1
    
    return nuc_freq
#4. Create DNA transcription from DNA sequence
def transcription(seq):
    return seq.replace('T','U')

#5. Create a compliment from DNA sequence
def complement(seq):
    com_seq = ''.join([ DNA_com[nuc] for nuc in seq])
    return comp_seq