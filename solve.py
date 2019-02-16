from state import State
from priority_queue import PriorityQueue

def solve(start, goal):
    opened = PriorityQueue()
    opened.push(State(goal, start, None))
    closed = []
    success = False

    while opened and not success:
        curr = opened.pop()
        closed.append(curr)
        next = curr.get_next_state()
        for s in next:
            if s.puzzle == goal:
                return s
            opened.push(s)
    return None

start = [1, 2, 3, 8, 4, 5, 0, 7, 6]
goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
print("start:", start)
print("goal :", goal)
solution = solve(start, goal)
if solution:
    for step in solution.get_path():
        print(step)