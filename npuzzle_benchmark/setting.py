import os
from tqdm import tqdm
import argparse
import sys
import time
import numpy as np
import subprocess

class Setting:

    def __init__(self):
        self.occurences = 0
        self.size = 0
        self.iterations = 0
        self.check_arguments(sys.argv[1:])
        self.generate_puzzles()
        self.testing_puzzle(solvable="unsolvable", heuristic="manhattan")
        self.testing_puzzle(solvable="unsolvable", heuristic="hamming")
        #self.testing_puzzle(solvable="solvable", heuristic="manhattan")
        #self.testing_puzzle(solvable="solvable", heuristic="hamming")

    def check_arguments(self, args=None):
        parser = argparse.ArgumentParser(description='Npuzzle benchmarking program.')
        parser.add_argument('-O', '--occurences', help='occurences of solvable/unsolvable npuzzles',
                            required='True', default=5)
        parser.add_argument('-S', '--size', help='npuzzle size',
                            default=5)
        parser.add_argument('-I', '--iterations', help='npuzzle iterations for generation',
                            default=100)
        res = parser.parse_args(args)
        self.occurences =  int(res.occurences)
        self.size = int(res.size)
        self.iterations = int(res.iterations)

    def generate_puzzles(self):
        os.system("mkdir -p tests")
        print('''
Benchmarking of solvable and unsolvable npuzzles parameters:

    Occurences : '''+str(self.occurences)+'''
    Iterations : '''+str(self.iterations)+'''
    Size : '''+str(self.size)+'''
        ''')
        print("Generating solvable and unsolvable puzzles ...")
        for i in tqdm(range(self.occurences)):
            os.system("python2.7 puzzle_generator.py -s -i "+str(self.iterations)+" "+str(self.size)+" > tests/solvable_"+str(i)+".txt")
            os.system("python2.7 puzzle_generator.py -u -i "+str(self.iterations)+" "+str(self.size)+" > tests/unsolvable_"+str(i)+".txt")
    
    def testing_puzzle(self, solvable="solvable", heuristic="manhattan"):
        unsolvable_outputs = []
        print("Testing "+solvable+" puzzles for "+heuristic+" heuristic ...")
        for i in range(self.occurences):
            subprocess.run(["python ../main.py -H "+heuristic+" -f tests/"+solvable+"_"+str(i)+".txt"], shell=True)
            #unsolvable_outputs.append(subprocess.run(["time python ../main.py -H "+heuristic+" -f tests/"+solvable+"_"+str(i)+".txt"], shell=True, capture_output=True))
        sys.exit(-1)
        for elem in unsolvable_outputs:
            print(elem.stdout)
        unsolvable_times = np.array([float(elem.stderr.split()[3][2:-1]) for elem in unsolvable_outputs])
        error = 0
        total = 0
        for elem in unsolvable_outputs:
            if (elem.stdout[:7]).decode("utf-8") == "Error :":
                error += 1
            total += 1
            
        print('''
Results for '''+solvable+''' npuzzles:

    success_rate : '''+str(100 * (total - error) / total)+'''%

    average_time : '''+str(np.around(unsolvable_times.mean(), decimals=4))+''' seconds
    minimum_time : '''+str(np.around(unsolvable_times.min(), decimals=4))+''' seconds
    maximum_time : '''+str(np.around(unsolvable_times.max(), decimals=4))+''' seconds
    standard deviation : '''+str(np.around(unsolvable_times.std(), decimals=4))+''' seconds

        ''')