sorting_hat
-----------

Sorts indels into classes defined as follows:
  - homopolymer run (HR): mutation is in a region where there are 6 or more
    copies of the nucleotide being inserted or deleted
  - change in copy count (CCC): the allele being inserted or deleted has 1 or
    more repeats in the mutation region
  - no change in copy count (non-CCC): the allele being inserted or deleted is
    not repeated in the mutation region

In order to use sorting_hat, you must ensure the following are installed:
  - `Python >=3.5.0`_
  - `bedtools >=2.27.0`_











.. _Python >=3.5.0: https://www.python.org/downloads/release/python-350/
.. _bedtools >=2.27.0: http://bedtools.readthedocs.io/en/latest/
