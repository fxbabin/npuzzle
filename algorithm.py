import heapq
import math
import heuristic

class State:

	def __init__(self, puzzle, parent, goal):
		self.puzzle = puzzle
		self.parent = parent
		if parent == None:
			self.g = 0
		else:
			self.g = parent.g + 1
		self.cost = self.g + heuristic.h(puzzle, goal)

	def to_tuple(self):
		t = (self.cost, self)
		return (t)
	
	def move_piece(self, src, dst):
		puzzle = self.puzzle.copy()
		puzzle[dst] = puzzle[src]
		puzzle[src] = 0
		return puzzle

	def get_next_state(self):
		size = math.sqrt(self.puzzle.len)
		i = self.puzzle.index(0)
		row = i % size
		col = i / size
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

"""
curr = pop
if curr == goal
	end
else
	get_next
	for each next
		check if in closed
			if in closed skip
		check if not in opened
			put it in opened
		else
			update the cost
"""

class Solver:

	def __init__(self, start, goal):
		self.goal = goal
		self.opened = []
		self.closed = []
		self.success = False
	
	def solve(self):
		while self.opened and not self.success:
			curr = heapq.heappop(self.opened)
			if curr.puzzle == self.goal:
				return curr
			curr.get_next_state()
			
		return None


	
