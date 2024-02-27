import sys
import os

def nl(file_path=None):
    if file_path:
        abs_file_path = os.path.abspath(file_path)
        with open(abs_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    else:
        lines = sys.stdin.readlines()
    
    for i, line in enumerate(lines, start=1):
        print(f'{i}\t{line}', end='')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        nl(sys.argv[1])
    else:
        nl()
