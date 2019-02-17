from goal import Goal
from hash_table import HashTable
from priority_queue import PriorityQueue
from state import State


class NPuzzle:

    def __init__(self, setting):
        self.size = setting.size
        self.goal = Goal(self.size)
        self.h = setting.h
        self.complexity_time = 0
        self.complexity_size = 1
        self.actual_size = 1
        self.opened = PriorityQueue()
        self.opened.push(State(self.goal, self.h, setting.start, None))
        self.opened_hash = HashTable()
        self.closed = HashTable()
        self.solution = self.solve()

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
                if s.puzzle == self.goal.puzzle:
                    return (s)
                if self.closed.contain(s):
                    self.actual_size -= 1
                    continue
                e = self.opened_hash.get(s)
                if e:
                    if s.g < e.g:
                        s.parent = e.parent
                        s.g = e.g
                        s.cost = e.cost
                    self.actual_size -= 1
                else:
                    self.opened.push(s)
                    self.opened_hash.push(s)
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
