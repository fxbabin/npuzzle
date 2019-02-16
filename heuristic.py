from math import sqrt

def manning(puzzle, goal):
	count = -1
	for i, j in zip(puzzle, goal):
		if i != j:
			count += 1
	return (count)

def manhattan(puzzle, goal):
	distance = 0
	size = int(sqrt(len(puzzle)))
	for piece in puzzle:
		if piece == 0:
			continue
		i = goal.index(piece)
		row = int(i / size)
		col = i % size
		distance += row + col
	return (distance)

def h(puzzle, goal):
	return (manning(puzzle, goal))