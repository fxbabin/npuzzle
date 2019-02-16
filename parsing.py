

import argparse
import sys
from pathlib import Path 


def check_arguments(args=None):
    possible_heuristics = ["manhattan"]
    
    parser = argparse.ArgumentParser(description='Npuzzle program.')
    parser.add_argument('-H', '--heuristic', help='heuristic algorithm used',
                        required='True', default='manhattan')
    parser.add_argument('-f', '--file', help='input npuzzle file', required=True)
    res = parser.parse_args(args)
    
    if res.heuristic not in possible_heuristics:
        print('Error : Wrong Heuristic !\n\nPossible Heuristic values:')
        for e in possible_heuristics:
            print(e)
        sys.exit(-1)    
    if not Path(res.file).is_file():
        print("Error : File \'"+res.file+"\' does not exist !")
        sys.exit(-1)
    return (res.heuristic, res.file)


def main():
    
    # heuristic, f_npuzzle = "", ""
    heuristic, f_npuzzle = check_arguments(sys.argv[1:])   
    print(heuristic, f_npuzzle)


if __name__ == "__main__":
    main()