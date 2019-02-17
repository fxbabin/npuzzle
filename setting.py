import argparse
import sys
from pathlib import Path
import heuristic


class Setting:

    def __init__(self):
        self.heuristic = ''
        self.file = ''
        self.check_arguments(sys.argv[1:])
        self.h = self.choose_heuristic_function()
        self.start = []
        self.size = 0
        self.puzzle_parsing(self.file)

    def check_arguments(self, args=None):
        """
        Check the input arguments of the program
            :param args=None: arguments of the program
        """
        possible_heuristics = ["hamming", "manhattan"]
        parser = argparse.ArgumentParser(description='Npuzzle program.')
        parser.add_argument('-H', '--heuristic', help='heuristic function',
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
        self.heuristic = res.heuristic
        self.file = res.file

    def puzzle_parsing(self, npuzzle_filename: str):
        """
        docstring here
            :param npuzzle_filename:str: filename for npuzzle file
        """
        with open(npuzzle_filename, 'r') as in_file:
            for line in in_file:
                if line[0] == '#':
                    continue
                line_split = line.split(' ')
                if len(line_split) == 1:
                    self.size = int(line_split[0])
                    break

            for line in in_file:
                for letter in line:
                    if letter not in "0123456789 \n":
                        print("Error : \'{}\' wrong character "
                              "in puzzle line".format(letter))
                        sys.exit(-1)
                line_split = line.split(' ')
                if len(line_split) != self.size:
                    print("Error : line size differs from the "
                          "indicated size of puzzle")
                    sys.exit(-1)
                for e in line_split:
                    self.start.append(int(e))

    def choose_heuristic_function(self):
        if self.heuristic == 'hamming':
            return (heuristic.hamming)
        elif self.heuristic == 'manhattan':
            return (heuristic.manhattan)
