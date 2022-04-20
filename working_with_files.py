#given a file, return a new file of all even lines of original file. Assume 1 based numbering.

import sys
from IPython.core.ultratb import ColorTB
sys.excepthook = ColorTB()

def even_lines(file):
    input_txt = open(file, "r")
    output_txt = open("output.txt", "w")
    pointer = 1
    for line in input_txt:
        if pointer % 2 == 0:
            output_txt.write(line)
        pointer += 1

even_lines("working_with_files_exercise.txt")