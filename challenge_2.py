#!/usr/bin/env python

import texts

def count_characters(s):
    
    counts = {}
    
    for char in s:
        
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
            
    return counts

if __name__ == '__main__':
        
    # Look for least common characters.

    counts = count_characters(texts.challenge_2)
    print counts
    counts_sorted = sorted(counts, key=counts.get)
    print counts_sorted
    print ''.join(counts_sorted[0:8])

    # Try to shift least common characters.

    import challenge_1

    s = ''.join(counts_sorted[0:8])
    s = challenge_1.shift(s,2)
    print s.lower()
    
    # aeilquty -> equality