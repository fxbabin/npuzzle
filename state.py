from math import sqrt
from heuristic import h

class State:

    def __init__(self, goal, puzzle, parent):
        self.goal = goal
        self.puzzle = puzzle
        self.parent = parent
        if parent:
            self.g = parent.g + 1
        else:
            self.g = 0
        self.cost = self.g + h(puzzle, goal)
        
    def move_piece(self, src, dst):
        puzzle = self.puzzle.copy()
        puzzle[dst] = puzzle[src]
        puzzle[src] = 0
        state = State(self.goal, puzzle, self)
        return state

    def get_next_state(self):
        size = int(sqrt(len(self.puzzle)))
        i = self.puzzle.index(0)
        row = int(i / size)
        col = i % size
        next = []
        if row > 0:
            up = self.move_piece((row - 1) * size + col, i)
            next.append(up)
        if row < size - 1:
            down = self.move_piece((row + 1) * size + col, i)
            next.append(down)
        if col > 0:
            left = self.move_piece(row * 3 + col - 1, i)
            next.append(left)
        if col < size - 1:
            right = self.move_piece(row * 3 + col + 1, i)
            next.append(right)
        return (next)
    
    def get_path(self):
        path = []
        curr = self
        while curr:
            path.append(curr.puzzle)
            curr = curr.parent
        path.reverse()
        return (path)
            