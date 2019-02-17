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
        if self.parent and self.puzzle[src] == self.parent.puzzle[dst]:
            return (None)
        puzzle = self.puzzle.copy()
        puzzle[dst] = puzzle[src]
        puzzle[src] = 0
        state = State(goal, h, puzzle, self)
        return (state)

    def get_next_state(self, goal, h):
        size = goal.size
        i = self.puzzle.index(0)
        row = int(i / size)
        col = i % size
        next = []
        if row > 0:
            up = self.move_piece(goal, h, i - size, i)
            if up:
                next.append(up)
        if row < size - 1:
            down = self.move_piece(goal, h, i + size, i)
            if down:
                next.append(down)
        if col > 0:
            left = self.move_piece(goal, h, i - 1, i)
            if left:
                next.append(left)
        if col < size - 1:
            right = self.move_piece(goal, h, i + 1, i)
            if right:
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
