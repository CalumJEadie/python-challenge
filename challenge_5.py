#!/usr/bin/env python

# downloaded banner.p
# peakhell sounds like? pickle

import pickle
import texts

banner = pickle.loads(texts.challenge_5)
print banner

# some kind of ascii art using run length encoding?

for line in banner:
    line_str = ""
    for (char,length) in line:
        line_str += char*length
    print line_str
    
# channel
