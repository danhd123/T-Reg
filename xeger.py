import sys
import difflib
import collections

class Xeger(object):
    """Find regexes matching sets of sequences"""
    def __init__(self, sequences):
        self.sequences = sequences
        self.diffs = None
    
    def _generate_diffs(self):
        self.diffs = collections.defaultdict(dict)
        s_prev = None
        for s, i in zip(self.sequences, xrange(len(self.sequences))):
            if s_prev:
                matcher = difflib.SequenceMatcher(lambda x: False, s_prev, s)
                diff = matcher.get_matching_blocks()
                matches = [s_prev[i:i+n] for i, j, n in diff]
                self.diffs[i-1][i] = matches
            s_prev = s
    
    def regexes(self):
        if not self.diffs:
            self._generate_diffs()
        regexes = []
        for diff_dict in self.diffs.viewvalues():
            for diff in diff_dict.viewvalues():
                regexes.append(diff)
        return regexes
    

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        xe = Xeger(f.readlines())
        for r in xe.regexes():
            print r
