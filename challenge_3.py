#!/usr/bin/env python

import re
import utils

if __name__ == '__main__':

    # Looking for "one small letter surrounded by exactly three big bodyguards""".
    # Looking for y in xXXXyXXXx.

    text = utils.get_text(3)

    pattern = '[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]'
    match = re.search(pattern,text)
    
    print match.groups()
    
    # l -> but there are more
    
    pattern = '[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]'
    match = re.findall(pattern,text)
    
    print match
    print ''.join(match)
    
# Next url: http://www.pythonchallenge.com/pc/def/linkedlist.html
