def manning(puzzle, goal):
	count = 0
	for i, j in zip(puzzle, goal):
		if i != j:
			count += 1
	return (count)

def h(puzzle, goal):
	return (manning(puzzle, goal))