import sys
import difflib
import collections

import retools

class TReg(object):
    """Find regexes matching sets of sequences"""
    def __init__(self, sequences):
        self.sequences = sequences
        self.diffs = None
    
    def _generate_diffs(self):
        self.diffs = collections.defaultdict(dict)
        s_prev = None
        for s, i in zip(self.sequences, xrange(len(self.sequences))):
            if s.endswith('\n'):
                s = s[:-1]
            if s_prev:
                matcher = difflib.SequenceMatcher(lambda x: False, s_prev, s)
                diff = matcher.get_matching_blocks()
                self.diffs[i-1][i] = diff
            s_prev = s
    
    def regexes(self):
        if not self.diffs:
            self._generate_diffs()
        regexes = []
        for s0_id, diff_dict in self.diffs.viewitems():
            for s1_id, diff in diff_dict.viewitems():
                s0, s1 = self.sequences[s0_id], self.sequences[s1_id]
                bookmark_i = 0
                bookmark_j = 0
                this_regex = [r'^']
                for i, j, n in diff:
                    nonmatches_i = s0[bookmark_i:i]
                    nonmatches_j = s1[bookmark_j:j]
                    mismatch_group = retools.char_set_to_smart_group(nonmatches_i + nonmatches_j)
                    this_regex.append(mismatch_group)
                    match_group = retools.escaped(s0[i:i+n])
                    this_regex.append(match_group)
                    bookmark_i = i+n
                    bookmark_j = j+n
                this_regex.append(r'$')
                regexes.append(''.join(this_regex))
        return regexes
    

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        tr = TReg(f.readlines())
        for r in tr.regexes():
            print r
