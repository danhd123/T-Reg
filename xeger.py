import sys
import difflib

class Xeger(object):
    """Find regexes matching sets of sequences"""
    def __init__(self, sequences):
        self.sequences = sequences
    
    def regexes(self):
        return []
        

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        xe = Xeger(f.readlines())
        print '\n'.join(xe.regexes())
