import sys
import os

def tail(files=None):
    if files:
        for file_path in files:
            abs_file_path = os.path.abspath(file_path)
            file_name = os.path.basename(abs_file_path)
            print(f'======> {file_name} <======')
            with open(abs_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                original_line_count = len(lines)
                print(f'original total lines of the file: {original_line_count}')
                print("the last 10 lines of the file:")
            for i, line in enumerate(lines[-10:], start=1):
                print(f'{i}\t{line}', end='')
            print()
    else:
        lines = sys.stdin.readlines()
        original_line_count = len(lines)
        print(f"original total lines of 'stdin': {original_line_count}")
        print("the last 17 lines of 'stdin':")
        for i, line in enumerate(lines[-17:], start=1):
            print(f'{i}\t{line}', end='')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        absolute_paths = [os.path.abspath(file_path) for file_path in sys.argv[1:]]
        tail(absolute_paths)
    else:
        tail()