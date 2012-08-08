#!/usr/bin/env python

import os
import re
import zipfile

# <!-- zip
# zip.html "yes. find the zip."

# will admit needed a bit of help to go from zip to downloading channel.zip!!

list_dir="data/6/channel"

def get_node_path(node_id):

    return os.path.join(list_dir,str(node_id)+".txt")

def get_next_id(curr_id):
    
    # Specify pattern and enforce int conversion to catch out any notable outlying messages.
    
    node_text = open(get_node_path(curr_id)).read()
    pattern = "Next nothing is ([0-9]+)"
    ids = re.findall(pattern,node_text)
    # To try and catch out
    next_id = int(ids[0])
    return next_id
        
def walk_linked_list(start_id):

    curr_id = start_id
    while True:
        curr_id = get_next_id(curr_id)
        print curr_id
        
def get_all_ids():

    all_files = os.listdir(list_dir)
    all_files.remove("readme.txt")
    extract_id = lambda x : int(x[:-4])
    all_ids = map(extract_id,all_files)
    return set(all_ids)
    
def get_accessible_ids(start_id):

    accessible_ids = []
    curr_id = start_id
    while True:
        accessible_ids.append(curr_id)
        try:
            curr_id = get_next_id(curr_id)
        except Exception:
            break        
    return set(accessible_ids)

def get_comment(zip_file,node_id):
    
    return zip_file.getinfo("%s.txt"%node_id).comment
    
def collect_comments(start_id):

    zip_file = zipfile.ZipFile(open("data/6/channel.zip"))

    comments = []
    curr_id = start_id
    while True:
        comments.append(get_comment(zip_file,curr_id))
        try:
            curr_id = get_next_id(curr_id)
        except Exception:
            break
    return comments
    
def print_comments(comments):

    print ''.join(comments)

if __name__ == '__main__':

    # Approach 1: Traverse the list.

    # Start with 90052, see how far through the list this will take us.
    #start_id = 90052
    #walk_linked_list(start_id)
    
    # Got up to 46145. "collect the comments."
    
    # Approach 2: Determine if there are any unwalked nodes.
    
    #start_id = 90052
    #all_ids = get_all_ids()
    #print "len(all_ids) = %s" % len(all_ids)
    #accessible_ids = get_accessible_ids(start_id)
    #print "len(accessible_ids) = %s" % len(accessible_ids)
    #not_accessible_ids = all_ids - accessible_ids
    #print "len(not_accessible_ids) = %s" % len(not_accessible_ids)
    
    # All nodes accessible.
    
    # Approach 3: Aha, a zip file can contain a comment!
    
    start_id = 90052
    comments = collect_comments(start_id)
    print_comments(comments)
    
    # hockey
