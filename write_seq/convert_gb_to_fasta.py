from Bio import SeqIO
input_filename = "NC_03361.gbk"
output_filename = "NC_013361_converted.fasta"
count = SeqIO.convert(input_filename, "gb", output_filename, "fasta")
print(str(count) + " records converted")
