#!/usr/bin/env python

import texts
import re

if __name__ == '__main__':

    # Looking for "one small letter surrounded by exactly three big bodyguards""".
    # Looking for y in xXXXyXXXx.

    text = texts.challenge_3

    pattern = '[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]'
    match = re.search(pattern,texts.challenge_3)
    
    print match.groups()
    
    # l -> but there are more
    
    pattern = '[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]'
    match = re.findall(pattern,texts.challenge_3)
    
    print match
    print ''.join(match)