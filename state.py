from math import sqrt
import heuristic


class State:

    def __init__(self, goal, h, puzzle, parent):
        self.puzzle = puzzle
        self.parent = parent
        if parent:
            self.g = parent.g + 1
        else:
            self.g = 0
        self.cost = self.g + h(puzzle, goal)

    def move_piece(self, goal, h, src, dst):
        puzzle = self.puzzle.copy()
        puzzle[dst] = puzzle[src]
        puzzle[src] = 0
        state = State(goal, h, puzzle, self)
        return state

    def get_next_state(self, goal, h):
        size = goal.size
        i = self.puzzle.index(0)
        row = int(i / size)
        col = i % size
        next = []
        if row > 0:
            up = self.move_piece(goal, h, (row - 1) * size + col, i)
            next.append(up)
        if row < size - 1:
            down = self.move_piece(goal, h, (row + 1) * size + col, i)
            next.append(down)
        if col > 0:
            left = self.move_piece(goal, h, row * size + col - 1, i)
            next.append(left)
        if col < size - 1:
            right = self.move_piece(goal, h, row * size + col + 1, i)
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
