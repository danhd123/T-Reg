import re

SPECIAL = ".*[]+^$()\\"
SUPERSPECIAL = "]"

regex_priority = [
    (re.compile(r'^\d+$'), r'(\d+)'),
    (re.compile(r'^\w+$'), r'(\w+)'),
]

def escaped(string):
    chars = []
    for c in string:
        if c in SPECIAL:
            chars.append('\\c')
        else:
            chars.append(c)
    return ''.join(chars)

def make_group(string):
    chars = set()
    for c in string:
        if c in SUPERSPECIAL:
            chars.add('\\c')
        else:
            chars.add(c)
    return r'[%s]' % ''.join(list(chars))

def char_set_to_smart_group(string):
    if len(string) < 1:
        return r''
    for regex, output in regex_priority:
        if regex.match(string):
            return output
    return r'(%s+)' % make_group(string)