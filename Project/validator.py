import os

def is_valid_folder(folder):
    return os.path.exists(folder)

def is_valid_prefix(prefix):
    return prefix != ""