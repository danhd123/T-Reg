T-Reg: A By-Example Regular Expression Generator
================================================

Version 0.000000000001

Created by [Steve Johnson](http://www.steveasleep.com)  
steve.johnson.public@gmail.com

Tested with Python 2.7  
Should work with Python 2.6 (and 2.5 with minor modifications)

What It Does
============

T-Reg attempts to generate useful regular expressions from newline-delimited text files. For example, this input:

    item 1: bananas
    item 2: carrots

produces the regular expression ``^item (\d+): (\w+)a(\w+)s$``. (This is extremely early-stage output, and ``n`` strings will produce ``n-1`` regular expressions.)

Usage
=====

    python treg.py <file name>

Planned features
================

- Options to ignore whitespace, specify comment characters, and give delimiter hints
- Much more processing of regex results
- Meta-regexes for higher level processing (It's turtles all the way down!)
- Interactive mode to make results more or less specific

How It Works
============

The current algorithm is stupidly simple:

* For each diff between each adjacent pair of lines
    * Begin with the string ``"^"``
    * For each matching sequence, append an escaped string
    * For each pair of nonmatching sequences, append a capture group containing all characters found in both nonmatching sequences
        *Unless the nonmatching sequences contain a suspiciously regular set of characters like whitespace, letters, or numbers. In that case, append a specific kind of capture group relevant to the character set.
    * Append the string ``"$"``
    * Output the string
