import os

def rename_files(folder, prefix):
    files = os.listdir(folder)
    count = 1

    for file in files:
        old_path = os.path.join(folder, file)

        if os.path.isfile(old_path):
            ext = os.path.splitext(file)[1]
            new_name = prefix + "_" + str(count) + ext
            new_path = os.path.join(folder, new_name)

            os.rename(old_path, new_path)
            print(file, "→", new_name)

            count += 1