from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
my_seq = Seq('GATCGATGGGCCTATATAGGATCGAAAATCGC', IUPAC.unambiguous_dna)
len(my_seq)

my_seq.count("G")
100 * float(my_seq.count("G") + my_seq.count("C")) / len(my_seq)

