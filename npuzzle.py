from state import State
from priority_queue import PriorityQueue
from hash_table import HashTable


class NPuzzle:

    def __init__(self, start, h):
        self.size = 3
        self.generate_goal()
        self.h = h
        self.complexity_time = 0
        self.complexity_size = 1
        self.actual_size = 1
        self.opened = PriorityQueue()
        self.opened.push(State(self.goal, h, start, None))
        self.closed = HashTable()
        self.solution = self.solve()

    def generate_goal(self):
        self.goal = [None for i in range(self.size * self.size)]
        row = 0
        col = -1
        border_left = 0
        border_right = self.size - 1
        border_top = 1
        border_bottom = self.size - 1
        i = 1
        while True:
            while col < border_right:
                col += 1
                if i == self.size * self.size:
                    self.goal[row * self.size + col] = 0
                    return
                self.goal[row * self.size + col] = i
                i += 1
            border_right -= 1
            while row < border_bottom:
                row += 1
                if i == self.size * self.size:
                    self.goal[row * self.size + col] = 0
                    return
                self.goal[row * self.size + col] = i
                i += 1
            border_bottom -= 1
            while col > border_left:
                col -= 1
                if i == self.size * self.size:
                    self.goal[row * self.size + col] = 0
                    return
                self.goal[row * self.size + col] = i
                i += 1
            border_left += 1
            while row > border_top:
                row -= 1
                if i == self.size * self.size:
                    self.goal[row * self.size + col] = 0
                    return
                self.goal[row * self.size + col] = i
                i += 1
            border_top += 1

    def solve(self):
        while not self.opened.is_empty():
            curr = self.opened.pop()
            self.closed.push(curr)
            next = curr.get_next_state(self.goal, self.h)
            self.complexity_time += 1
            self.actual_size += len(next)
            if self.actual_size > self.complexity_size:
                self.complexity_size = self.actual_size
            for s in next:
                if s.puzzle == self.goal:
                    return (s)
                if self.closed.contain(s):
                    self.actual_size -= 1
                    continue
                e = self.opened.index(s)
                if e:
                    if s.g < e.g:
                        s.parent = e.parent
                        s.g = e.g
                        s.cost = e.cost
                    self.actual_size -= 1
                else:
                    self.opened.push(s)
        return (None)

    def report(self):
        if self.solution:
            print("Complexity in time:", self.complexity_time)
            print("Complexity in size:", self.complexity_size)
            print("Number of moves:", self.solution.g)
            print("Solution:")
            for step in self.solution.get_path():
                print(step)
        else:
            print("The puzzle is unsolvable")
