==============================
Working with Sequence Features
==============================

This picks up from the end of the section on `reading sequence files
<../reading_sequence_files/README.rst>`_, but looks at the feature
annotation included in some file formats like EMBL or GenBank.

Most of the time GenBank files contain a single record for a single
chromosome or plasmid, so we'll generally use the ``SeqIO.read(...)``
function. Remember the second argument is the file format, so if we
start from the code to read in a FASTA file:

.. sourcecode:: pycon

    >>> from Bio import SeqIO
    >>> record = SeqIO.read("NC_013361.fna", "fasta")
    >>> print(record.id)
    gi|556503834|ref|NC_013361.3|
    >>> print(len(record))
    4641652
    >>> print(len(record.features))
    0

Now switch the filename and the format:

.. sourcecode::	pycon

    >>> from Bio import SeqIO
    >>> record = SeqIO.read("NC_013361.gbk", "genbank")
    >>> print(record.id)
    NC_013361.3
    >>> print(len(record))
    4641652
    >>> print(len(record.features))
    23086

So what is this new ``.features`` thing? It is a Python list, containing
a Biopython ``SeqFeature`` object for each feature in the GenBank file.
For instance,

.. sourcecode:: pycon

    >>> my_gene = record.features[3]
    >>> print(my_gene)
    type: gene
    location: [336:2799](+)
    qualifiers: 
        Key: db_xref, Value: ['EcoGene:EG10998', 'GeneID:945803']
        Key: gene, Value: ['thrA']
        Key: gene_synonym, Value: ['ECK0002; Hs; JW0001; thrA1; thrA2; thrD']
        Key: locus_tag, Value: ['b0002']

Doing a print like this tries to give a human readable display. There
are three key properties, ``.type`` which is a string like ``gene``
or ``CDS``, ``.location`` which describes where on the genome this
feature is, and ``.qualifiers`` which is a Python dictionary full of
all the annotation for the feature (things like gene identifiers).

This is what this gene looks like in the raw GenBank file::

     gene            337..2799
                     /gene="thrA"
                     /locus_tag="b0002"
                     /gene_synonym="ECK0002; Hs; JW0001; thrA1; thrA2; thrD"
                     /db_xref="EcoGene:EG10998"
                     /db_xref="GeneID:945803"

Hopefully it is fairly clear how this maps to the ``SeqFeature`` structure.
The `Biopython Tutorial & Cookbook <http://biopython.org/DIST/docs/tutorial/Tutorial.html>`_
(`PDF <http://biopython.org/DIST/docs/tutorial/Tutorial.pdf>`_) goes into
more detail about this.

-----------------
Feature Locations
-----------------

We're going to focus on using the location information for different feature
types. Continuing with the same example:

.. sourcecode:: pycon

    >>> from Bio import SeqIO
    >>> record = SeqIO.read("NC_013361.gbk", "genbank")
    >>> my_gene = record.features[3]
    >>> print(my_gene.qualifiers["locus_tag"])
    ['b0002']
    >>> print(my_gene.location)
    [336:2799](+)
    >>> print(my_gene.location.start)
    336
    >>> print(my_gene.location.end)
    2799
    >>> print(my_gene.location.strand)
    1

Recall in the GenBank file this simple location was ``337..2799``, yet
in Biopython this has become a start value of 336 and 2799 as the end.
The reason for this is to match how Python counting works, in particular
how Python string slicing. In order to pull out this sequence from the full
genome we need to use slice values of 336 and 2799:

.. sourcecode:: pycon

    >>> gene_seq = record.seq[336:2799]
    >>> len(gene_seq)
    2463
    >>> print(gene_seq)
    ...

This was a very simple location on the forward strand, if it had been on
the reverse strand you'd need to take the reverse-complement. Also if the
location had been a more complicated compound location like a *join* (used
for eukaryotic genes where the CDS is made up of several exons), then the
location would have-sub parts to consider.

All these complications are taken care of for you via the ``.extract(...)``
method which takes the full length parent record's sequence as an argument:

.. sourcecode:: pycon

    >>> gene_seq = my_gene.extract(record.seq)
    >>> len(gene_seq)
    2463
    >>> print(gene_seq)
    ...

------------------------
Translating CDS features
------------------------

When dealing with GenBank files and trying to get the protein sequence of the
genes, you'll need to look at the CDS features (coding sequences) - not the
gene features (although for simple cases they'll have the same location).

Sometimes, as in the *E. coli* exmaple, you will find the translation is
provided in the qualifiers:

    >>> from Bio import SeqIO
    >>> record = SeqIO.read("NC_013361.gbk", "genbank")
    >>> my_cds = record.features[4]
    >>> print(my_cds.qualifiers["locus_tag"])
    ['b0002']
    >>> print(my_cds.qualifiers["translation"])
    ['MRVLKFGGTSVANAERFLRVADILESNARQGQVATVLSAPAKITNHLVAMIEKTISGQDALPNI...KLGV']

This has been truncated for display here - the whole protein sequence is
present. However, many times the annotation will not include the amino acid
translation - but we can get it by translating the nucleotide sequence.

    >>>	print(cds_seq.translate(table=11))
    >>> protein_seq = cds_seq.translate(table=11)
    >>>	len(protein_seq)
    821
    >>> print(protein_seq)
    MRVLKFGGTSVANAERFLRVADILESNARQGQVATVLSAPAKITNHLVAMIEKTISGQDALPNI...KLGV*

Notice because this is a bacteria, we used the NCBI translation table 11,
rather than the default (suitable for humans etc).

