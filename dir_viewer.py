import os


def scanner(path=".", files=[]):
    """The function takes a directory name and prints out its contents
    in the form of "path and file name", as well as any other
    files in subdirectories."""

    if os.path.isfile(path):
        return files.append(path)
    for item in os.listdir(path):
        item = os.path.join(path, item)
        if os.path.isfile(item):
            files.append(item)
        else:
            files = scanner(item, files)
    return files


def dir_viewer(search="."):
    for f in scanner(search):
        print(f)


def get_directory_contents(path):
    """alternative option"""

    def get_directory_files(path):
        struct = []
        for file_or_directory in os.listdir(path):
            full_name = os.path.join(os.path.abspath(path), file_or_directory)
            if os.path.isfile(full_name):
                struct.append((os.path.abspath(path), file_or_directory))
            else:
                struct.extend(get_directory_files(full_name))
        return struct

    return get_directory_files(path)


if __name__ == '__main__':
    # dir_viewer("..")
    print(get_directory_contents('.'))
