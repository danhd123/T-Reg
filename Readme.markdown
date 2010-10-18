T-Reg: A By-Example Regular Expression Generator
================================================

Version 0.000000000001

Created by [Steve Johnson](http://www.steveasleep.com) (steve.johnson.public@gmail.com)

Tested with Python 2.7
Should work with Python 2.6 (and 2.5 with minor modifications)

What It Does
============

T-Reg attempts to generate useful regular expressions from newline-delimited text files.

Usage
=====

    python treg.py <file name>

Planned features
================

- Options to ignore whitespace and specify comment characters
- Much more processing of regex results

How It Works
============

The current algorithm is stupidly simple:

* Generate a diff between each adjacent pair of lines
* For each matching sequence, append an escaped string
* For each pair of nonmatching sequences, append a capture group containing all characters found in both nonmatching sequences
  - Unless the nonmatching sequences contain a suspiciously regular set of characters like whitespace, letters, or numbers. In that case, append a specific kind of capture group relevant to the character set.
