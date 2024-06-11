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
from zipfile import ZipFile
import requests

def make_sha_filename(basename, ext):
    """
    Generate a filename with the current git commit SHA.
    
    Args:
        basename (str): The base name of the file.
        ext (str): The file extension.
    
    Returns:
        str: Filename with SHA and potential '-dirty' suffix if uncommitted changes are present.
    """
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



def unzip_one_file(zipfile, filename, destination_file):
    """
    Unzip one file from a zip-archive.

    Args:
        zipfile (str): Path to the zip file.
        filename (str): Name of the file within the zip-archive to unzip, including any paths.
        destination_file (str): Path and file where to place the extracted file.
    """
    os.makedirs(os.path.dirname(destination_file), exist_ok=True)

    with ZipFile(zipfile, 'r') as z:
        with z.open(filename) as source, open(destination_file, 'wb') as target:
            target.write(source.read())

def download_file(url, dir_path, filename, force_download=False):
    """
    Download a file if it has not been downloaded already.
    
    Args:
        url (str): The URL to download from.
        dir_path (str): Directory to save the file.
        filename (str): Name of the file to save.
        force_download (bool): Force download even if the file is present.
    
    Returns:
        str: Full path of the downloaded file.
    """
    dirfile = os.path.join(dir_path, filename)
    os.makedirs(dir_path, exist_ok=True)
    
    if os.path.isfile(dirfile) and not force_download:
        print(" ... already downloaded ... ")
    else:
        if os.path.isfile(dirfile):
            os.remove(dirfile)
        print(" ... downloading ... ")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(dirfile, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    return dirfile