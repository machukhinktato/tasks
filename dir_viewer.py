import os


def getFiles(path=".", files=[]):
    if os.path.isfile(path):
        return files.append(path)
    for item in os.listdir(path):
        item = os.path.join(path, item)
        if os.path.isfile(item):
            files.append(item)
        else:
            files = getFiles(item, files)
    return files


def searcher(search="."):
    for f in getFiles(search):
        print(f)


if __name__ == '__main__':
    searcher()
