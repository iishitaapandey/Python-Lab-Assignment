from reader import get_files
from renamer import rename_files
from validator import is_valid_folder, is_valid_prefix

folder = input("Enter folder path: ")

if not is_valid_folder(folder):
    print("Folder not found")
    exit()

prefix = input("Enter prefix: ")

if not is_valid_prefix(prefix):
    print("Invalid prefix")
    exit()

files = get_files(folder)

print("\nFiles found:")
for f in files:
    print(f)

choice = input("\nDo you want to rename files? (yes/no): ")

if choice.lower() == "yes":
    rename_files(folder, prefix)
    print("\nRenaming completed")
else:
    print("Operation cancelled")