def hamming(puzzle, goal):
    count = -1
    for i, j in zip(puzzle, goal.puzzle):
        if i != j:
            count += 1
    return (count)


def manhattan(puzzle, goal):
    distance = 0
    for i, val in enumerate(puzzle):
        if val == 0:
            continue
        row = int(i / goal.size)
        col = i % goal.size
        if goal.hash[val][0] != row:
            distance += abs(row - goal.hash[val][0])
        if goal.hash[val][1] != col:
            distance += abs(col - goal.hash[val][1])
    return (distance)
