#!/usr/bin/env python

import urllib
#from BeautifulSoup import BeautifulSoup
import re

def get_node_url(node_id):

    node_url_template = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
    return node_url_template % node_id

def extract_next_id(curr_id):

    node_html = urllib.urlopen(get_node_url(curr_id)).read()
    #soup = BeautifulSoup(node_html)
    #body = soup.body
    print "Page contents: %s" % node_html
    #next_id = node_html.split(" ")[-1]
    #return next_id
    pattern = "next nothing is ([0-9]+)"
    ids = re.findall(pattern,node_html)
    # Check is integer
    next_id = int(ids[0])
    return next_id
    
def walk_linked_list(start_id):

    visited_nodes = set()
    curr_id = start_id
    
    for i in range(0,400):
        curr_id = extract_next_id(curr_id)
        print "Extracted node id: %s" % curr_id
        
        if curr_id in visited_nodes:
            print "Already visited %s" % curr_id
            break
        else:
            visited_nodes.add(curr_id)

if __name__ == '__main__':

        
    # Loops around again at some point?
    #walk_linked_list(12345)
            
    # Hidden message?
    # Checking messages need to continue from 16044/2
    #walk_linked_list(16044/2)
        
    # Misleading numbers. Reached 91763 without any misleading.
    # Try 82683 for example of misleading.
    #walk_linked_list(82683)
    walk_linked_list(91763)
    
    # peak.html
