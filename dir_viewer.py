# import os
#
# sPath = '.'
#
#
# def print_directory_contents(sPath):
#     for sChild in os.listdir(sPath):
#         sChildPath = os.path.join(sPath, sChild)
#         if os.path.isdir(sChildPath):
#             print_directory_contents(sChildPath)
#         else:
#             print(sChildPath)
#
# if __name__ == '__main__':
#     print_directory_contents(sPath)



import os

def getFiles(path="/var/log", files=[]):
    if os.path.isfile(path):
        return files.append(path)
    for item in os.listdir(path):
        item = os.path.join(path, item)
        if os.path.isfile(item):
            files.append(item)
        else:
            files = getFiles(item, files)
    return files



for f in getFiles(".", []):
    print(f)