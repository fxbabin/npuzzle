from npuzzle import NPuzzle
import heuristic

start = [7, 6, 2, 5, 3, 1, 0, 4, 8]
goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
puzzle = NPuzzle(start, goal, heuristic.hamming)
puzzle.report()