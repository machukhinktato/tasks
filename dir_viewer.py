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


if __name__ == '__main__':
    dir_viewer("..")
