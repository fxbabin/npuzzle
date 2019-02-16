from state import State
from priority_queue import PriorityQueue
from hash_table import HashTable

class NPuzzle:

    def __init__(self, start, goal):
        self.goal = goal
        self.complexity_time = 0
        self.complexity_size = 1
        self.opened = PriorityQueue()
        self.opened.push(State(goal, start, None))
        self.closed = HashTable()
        self.solution = self.solve()

    def solve(self):
        while not self.opened.is_empty():
            curr = self.opened.pop()
            self.closed.push(curr)
            next = curr.get_next_state()
            self.complexity_time += 1
            self.complexity_size += len(next)
            for s in next:
                if s.puzzle == self.goal:
                    return (s)
                if self.closed.contain(s):
                    continue
                e = self.opened.index(s)
                if e:
                    if s.g < e.g:
                        s.parent = e.parent
                        s.g = e.g
                        s.cost = e.cost
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
