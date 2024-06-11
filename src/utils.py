# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:08:22 2024

@author: BontL

T09
Tooling for reproducible model runs: a function which returns a file name with git commit hash

A simple way to store results in a reproducible way, is to add the git-hash (the thing you see in git log) to the file name. If you ever want to reproduce it, you know where to go back to.

    make a file src/utils.* and include/load it in your main model script
    make a function `(basename, ext) -> "basename-xxxxxxxxxx[-dirty].ext" where xxxxxxxxxx is the git hash shortened to 10 digits. It should append "-dirty" if there are not committed changes in the repository.
    use this in simple.* to store tables and plots

--> the tasks in utils.* and simple.* can be done concurrently!
"""

import os
from git import Repo

def make_sha_filename(basename, ext):
    # Open the git-repository in the current directory
    repo = Repo('.')  ## in the current directoty (Repo('.'))
    
    # Get the object ID of the HEAD commit
    head_commit_id = repo.head.commit.hexsha
    # Take the first 10 characters of the hexadecimal string
    short_hash = head_commit_id[:10]
    
    # Check if there are uncommitted changes
    if repo.is_dirty():
        postfix = f"{short_hash}-dirty"
    else:
        postfix = short_hash
    
    # Return the constructed filename
    return f"{basename}-{postfix}{ext}"

# Example usage

# basename = "file"
# ext = ".txt"
# filename = make_sha_filename(basename, ext)
# print(filename)

## Kontrolle aus git log:  7e725f2e72b539f820bcd69c24c02d77d794e484

## filename
## Out[14]: 'file-7e725f2e72.txt'