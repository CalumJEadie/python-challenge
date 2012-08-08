#!/usr/bin/env python

def alpha_to_int(char):
    base = ord("A")
    return ord(char.upper())-base
    
def int_to_alpha(int):
    base = ord("A")
    return chr(int+base).upper()

def shift(str,n):
    return "".join(map(lambda char: int_to_alpha((alpha_to_int(char)+n)%26),str))
    
def substitution(str,permutation):
    def substitute(char):
        if char in permutation:
            return permutation[char]
        else:
            return char
            
    return "".join(map(substitute,str))
    
if __name__ == '__main__':

    # Caeser Shift Cipher +2?
        
    s = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

    s = shift(s,2)
    # Fix up punctuation.
    permutation = {'V':' ','J':'.'}
    s = substitution(s,permutation)
    print s

    # string.maketrans is recommended.
    # DE? Mapping?
    # No, mistaken translation of ().
    # Use maketrans?

    import string
    trans_table = string.maketrans("koe","mqg")
    s = "http://www.pythonchallenge.com/pc/def/map.html"
    print string.translate(s,trans_table)

    # What does shifting the whole url give you?

    s = "http://www.pythonchallenge.com/pc/def/map.html"
    s = shift(s,2)
    print s

    # Aha, just the filename should change.

    s = "map"
    s = shift(s,2)
    print s
    
# Next url: http://www.pythonchallenge.com/pc/def/ocr.html
