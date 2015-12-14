=========================
Introduction to Biopython
=========================

This is a basic introduction to Biopython.It assumes you have been introduced 
to both working at the command line, and some basic Python.

The content was created as part of the Workshop session for SciPy India 2015.
The slides can be accessed `here <https://docs.google.com/presentation/d/1rPxLAGNZKULCPxkVFvh4h8J476Om43eMBiE7kKe0REg/edit#slide=id.p>`_

The Biopython website http://www.biopython.org has more information including the 
`Biopython Tutorial & Cookbook <http://biopython.org/DIST/docs/tutorial/Tutorial.html>`_
(html, `PDF available <http://biopython.org/DIST/docs/tutorial/Tutorial.pdf>`_),
which is worth going through once you have mastered the basics of Python.

=================
Workshop Sections
=================

I've broken up the workshop into sections:

* `Reading sequence files <reading_sequence_files/README.rst>`_.
* `Writing sequence files <writing_sequence_files/README.rst>`_.
* `Working with sequence features <using_seqfeatures/README.rst>`_.


This material focuses on Biopython's `SeqIO <http://biopython.org/wiki/SeqIO>`_
and `AlignIO <http://biopython.org/wiki/AlignIO>`_ modules (these links
include an overview and tables of supported file formats), each of which
also has a whole chapter in the `Biopython Tutorial & Cookbook
<http://biopython.org/DIST/docs/tutorial/Tutorial.html>`_
(`PDF <http://biopython.org/DIST/docs/tutorial/Tutorial.pdf>`_)
which would be worth reading after this workshop to learn more.

========
Notation
========

Text blocks starting with ``$`` show something you would type and run at the
command line prompt, where the ``$`` itself represents the prompt. For example:

.. sourcecode:: console

    $ python -V
    Python 2.7.5

Depending how your system is configured, rather than just ``$`` you may see your
user name and the current working directory. Here you would only type ``python -V``
(python space minus capital V) to find out the default version of Python installed.

Lines starting ``>>>`` represent the interactive Python prompt, and something
you would type inside Python. For example:

.. sourcecode:: pycon

    $ python
    Python 2.7.3 (default, Nov  7 2012, 23:34:47) 
    [GCC 4.4.6 20120305 (Red Hat 4.4.6-4)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 7 * 6
    42
    >>> quit()

Here you would only need to type ``7 * 6`` (and enter) into Python, the ``>>>``
is already there. To quit the interactive Python prompt use ``quit()`` (and enter).
This example would usually be shortened to just:

.. sourcecode:: pycon

    >>> 7 * 6
    42

These text blocks are also used for entire short Python scripts, which you can
copy and save as a plain text file with the extension ``.py`` to run them.

===========================
Prerequisites & Sample Data
===========================

If you are reading this on GitHub.com, you can view, copy/paste or download
individual examples from your web browser.

To make a local copy of the entire workshop, you can use the ``git``
command line tool:

.. sourcecode:: console

    $ git clone https://github.com/souravsingh/learning_biopython.git

Alternatively, depending on your firewall settings, use:

.. sourcecode:: console

    $ git clone git@github.com:souravsingh/learning_biopython.git

To learn more about ``git`` and software version control, I recommend attending using
`Try Git <https://try.github.io/levels/1/challenges/1>`_
or similar courses.

This should make a new sub-directory, ``learning_biopython/`` which we will now
change into:

.. sourcecode:: console

    $ cd learning_biopython

Most of the examples use real biological data files. You should download them
now using the `provided shell script <fetch_sample_data.sh>`_:

.. sourcecode:: console

    $ bash fetch_sample_data.sh

We assume you have Python and Biopython 1.63 or later installed and working.
Biopython 1.63 supports Python 2.6, 2.7 and 3.3 (and should work on more recent
versions). The examples here assume you are using Python 2.6 or 2.7, but in
general should work with Python 3 with minimal changes. Check this works:

.. sourcecode:: console

    $ python -c "import Bio; print(Bio.__version__)"
    1.63

