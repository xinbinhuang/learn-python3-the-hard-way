#!/usr/bin/env python
# A script for easy copy-pasting code chunk from the original book
# This remove all trailing line numbers from the original text.
# Example usage: python utils.py input.txt output.txt
import re
from sys import argv


def clean(lines, pattern, rep=''):
    for line in lines:
        cleaned_line = re.sub(pattern, rep, line)

        # keep empty lines
        if len(cleaned_line) < 2:
            cleaned_line += '\n'
        yield cleaned_line


def read_line(file):
    with open(file) as f:

        while True:
            line = f.readline()

            # stop while-loop when reach EOF
            if line:
                yield line
            else:
                break


def write_file(lines, file):
    with open(file, 'w') as f:
        for line in lines:
            f.write(line)


if __name__ == "__main__":
    script, input, output = argv

    pattern = r'^[0-9]{1,3}\s'
    pattern = re.compile(pattern)

    line = read_line(input)
    cleaned_line = clean(line, pattern)
    write_file(cleaned_line, output)
