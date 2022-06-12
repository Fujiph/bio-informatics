from DNAToolkit import *

dna = validateSeq( 'ATCGaaaaTCCCxxxxx' )
print(dna)

dna = validateSeq( 'ATCGaaaaTCCCattgcaa' )
print(dna)