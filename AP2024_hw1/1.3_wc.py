import sys
import os

def wc(files=None):
    total_lines = 0
    total_words = 0
    total_chars = 0

    if files:
        for file_path in files:
            abs_file_path = os.path.abspath(file_path)
            file_name = os.path.basename(abs_file_path)
            with open(abs_file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                num_lines = len(lines)
                num_words = sum(len(line.split()) for line in lines)
                num_chars = sum(len(line) for line in lines)
                
                total_lines += num_lines
                total_words += num_words
                total_chars += num_chars

                print(f'{num_lines}\t{num_words}\t{num_chars}\t{file_name}')

        if len(files) > 1:
            print(f'{total_lines}\t{total_words}\t{total_chars}\ttotal')
    else:
        lines = sys.stdin.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_chars = sum(len(line) for line in lines)

        print(f'{num_lines}\t{num_words}\t{num_chars}\t')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        absolute_paths = [os.path.abspath(file_path) for file_path in sys.argv[1:]]
        wc(absolute_paths)
    else:
        wc()