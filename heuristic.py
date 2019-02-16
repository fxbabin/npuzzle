from math import sqrt

def hamming(puzzle, goal):
	count = -1
	for i, j in zip(puzzle, goal):
		if i != j:
			count += 1
	return (count)

def manhattan(puzzle, goal):
	distance = 0
	size = int(sqrt(len(puzzle)))
	for i_piece, piece in enumerate(puzzle):
		if piece == 0:
			continue
		i_goal = goal.index(piece)
		if i_piece != i_goal:
			row_goal = int(i_goal / size)
			row_piece = int(i_piece / size)
			distance += abs(row_goal - row_piece)
			col_goal = i_goal % size
			col_piece = i_piece % size
			distance += abs(col_goal - col_piece)
	return (distance)

def h(puzzle, goal):
	return (manhattan(puzzle, goal))
