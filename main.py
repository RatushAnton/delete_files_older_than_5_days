import os
import time


def delete_old_files(root_dir_path, days):
    files_list = os.listdir(root_dir_path)
    current_time = time.time()
    for file in files_list:
        file_path = os.path.join(root_dir_path, file)
        if os.path.isfile(file_path):
            if (current_time - os.path.getmtime(file_path)) > (days * 24 * 60 * 60):
                os.remove(file_path)


if __name__ == '__main__':
    directory = input("Enter a directory: ")
    delete_old_files(directory, 5)
