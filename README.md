# npuzzle

Usage:
```
python3 main.py --heuristic [hamming|manhattan] --file [puzzle]
```

Examples:
```
time python3 main.py --heuristic hamming --file puzzles/solvable.npuzzle
time python3 main.py --heuristic manhattan --file puzzles/solvable.npuzzle
time python3 main.py --heuristic hamming --file puzzles/unsolvable.npuzzle
time python3 main.py --heuristic manhattan --file puzzles/unsolvable.npuzzle
```