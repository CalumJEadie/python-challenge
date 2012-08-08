#!/usr/bin/env python

# downloaded banner.p
# peakhell sounds like? pickle

import pickle

banner = pickle.loads(open('data/5/banner.p').read())
print banner

# some kind of ascii art using run length encoding?

for line in banner:
    line_str = ""
    for (char,length) in line:
        line_str += char*length
    print line_str
    
# Next url: http://www.pythonchallenge.com/pc/def/channel.html
