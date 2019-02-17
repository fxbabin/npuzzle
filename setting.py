import argparse
import sys
from pathlib import Path
import heuristic
import re

class Setting:

    def __init__(self):
        self.heuristic = ''
        self.file = ''
        self.check_arguments(sys.argv[1:])
        self.h = self.choose_heuristic_function()
        self.start = []
        self.size = 0
        self.puzzle_parsing(self.file)
        self.check_solvability()

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
                line = line.strip()
                if line[0] == '#':
                    continue
                line_split = re.sub(' +',' ', line).split(' ')
                if len(line_split) == 1:
                    self.size = int(line_split[0])
                    break

            for line in in_file:
                line = line.strip()
                for letter in line:
                    if letter not in "0123456789 \n":
                        print("Error : \'{}\' wrong character "
                              "in puzzle line".format(letter))
                        sys.exit(-1)
                line_split = re.sub(' +',' ', line).split(' ')
                if len(line_split) != self.size:
                    print("Error : line size differs from the "
                          "indicated size of puzzle")
                    sys.exit(-1)
                for letter in line_split:
                    self.start.append(int(letter))
    
    def check_solvability(self):
        permutations = 0
        i = 0
        for curr_tile in self.start:
            for tile in self.start[i+1:]:
                if curr_tile > tile and tile != 0:
                    permutations += 1
            i += 1
        if permutations % 2 == 0:
            print("Error : unsolvable puzzle !")
            sys.exit(-1)
        return (True)

    def choose_heuristic_function(self):
        if self.heuristic == 'hamming':
            return (heuristic.hamming)
        elif self.heuristic == 'manhattan':
            return (heuristic.manhattan)
