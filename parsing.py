

import argparse
import sys
from pathlib import Path
from puzzle import puzzle


def check_arguments(args=None):
    """
    Check the input arguments of the program
        :param args=None: arguments of the program
    """
    possible_heuristics = ["manhattan"]
    parser = argparse.ArgumentParser(description='Npuzzle program.')
    parser.add_argument('-H', '--heuristic', help='heuristic algorithm used',
                        required='True', default='manhattan')
    parser.add_argument('-f', '--file', help='input npuzzle file',
                        required=True)
    res = parser.parse_args(args)

    if res.heuristic not in possible_heuristics:
        print('Error : Wrong Heuristic !\n\nPossible Heuristic values:')
        for e in possible_heuristics:
            print(e)
        sys.exit(-1)
    if not Path(res.file).is_file():
        print("Error : File \'{}\' is not a file !".format(res.file))
        sys.exit(-1)
    return (res.heuristic, res.file)


def puzzle_parsing(npuzzle_filename: str):
    """
    docstring here
        :param npuzzle_filename:str: filename for npuzzle file
    """
    pzl = puzzle()
    with open(npuzzle_filename, 'r') as in_file:
        for line in in_file:
            if line[0] == '#':
                continue
            line_split = line.split(' ')
            if len(line_split) == 1:
                pzl.size = int(line_split[0])
                break

        for line in in_file:
            for letter in line:
                if letter not in "0123456789 \n":
                    print("Error : \'{}\' wrong character "
                          "in puzzle line".format(letter))
                    sys.exit(-1)
            line_split = line.split(' ')
            if len(line_split) != pzl.size:
                print("Error : line size differs from the "
                      "indicated size of puzzle")
                sys.exit(-1)
            for e in line_split:
                pzl.puzzle.append(int(e))
    return (pzl)


def main():
    heuristic, npuzzle_filename = check_arguments(sys.argv[1:])
    pzl = puzzle_parsing(npuzzle_filename)
    print(pzl.size, pzl.puzzle)

if __name__ == "__main__":
    main()
