import re

def pretty_message(s):
    a = []
    s = s.split()
    for i in s:
        c = re.sub(r'([a-z]+?)\1+', r'\1', i)
        a.append(c)
    return ' '.join(a)

print(pretty_message('Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss'))
