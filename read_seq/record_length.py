from Bio import SeqIO
filename = "NC_013361.faa"
for record in SeqIO.parse(filename, "fasta"):
    print("Record " + record.id + ", length " + str(len(record.seq)))
