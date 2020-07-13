from pathlib import Path
import sys


def find(root_path, extension):
    p = Path(root_path)
    dir_files = p.glob(f'**/*.{extension}')
    return dir_files


""" 
either relative or absolute path from command line
"""
# root_path = 'D:\YnonPerek\python-bootcamp\exercises\lesson19'
# root_path = '..\lesson19'
root_path = sys.argv[1]
extension = 'json'
extension_files = find(root_path, extension)

while True:
    try:
        print(next(extension_files))
    except StopIteration:
        break







