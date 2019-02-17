from npuzzle import NPuzzle
import heuristic

# unsolvable
# start = [5, 2, 7, 1, 3, 6, 0, 4, 8]
# easy
start = [1, 2, 3, 8, 4, 5, 0, 7, 6]
puzzle = NPuzzle(start, heuristic.hamming)
puzzle.report()