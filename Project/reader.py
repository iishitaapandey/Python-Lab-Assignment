import os

def get_files(folder):
    try:
        return os.listdir(folder)
    except:
        print("Invalid folder path")
        return []