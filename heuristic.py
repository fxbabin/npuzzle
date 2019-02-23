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


#%%
def get_conflict(puzzle_row, goal_row, size):
    count = [0] * size
    conflict = []
    for j, tj in enumerate(puzzle_row):
        conflict.append([])
        for k, tk in enumerate(puzzle_row):
            if tj == 0 or tk == 0:
                continue
            if j <= k:
                continue
            if tj not in goal_row or tk not in goal_row:
                continue
            if goal_row.index(tj) >= goal_row.index(tk):
                continue
            count[j] += 1
            count[k] += 1
            conflict[j].append(k)
            conflict[k].append(j)
    return (count, conflict)

row1 = [0, 2, 1]
row2 = [5, 4, 3]
row3 = [3, 4, 5]
size = 3
goal_row1 = [0, 1, 2]
goal_row2 = [3, 4, 5]

print(get_conflict(row1, goal_row1, size))
print(get_conflict(row2, goal_row2, size))
print(get_conflict(row3, goal_row2, size))


#%%
def calculate_lc(puzzle_row, goal_row, size):
    lc = 0
    count, conflict = get_conflict(puzzle_row, goal_row, size)
    while sum(count) > 0:
        max_index = count.index(max(count))
        count[max_index] = 0
        for i in conflict[max_index]:
            count[i] -= 1
        lc += 1
    return (lc)

print(calculate_lc(row1, goal_row1, size))
print(calculate_lc(row2, goal_row2, size))
print(calculate_lc(row3, goal_row2, size))

#%%
def generate_rows_cols(puzzle_list, size):
    rows = []
    for i in range(size):
        tmp = puzzle_list[i * size:(i + 1) * size]
        rows.append(tmp)

    cols = []
    for i in range(size):
        tmp = []
        for y in range(size):
            tmp.append(puzzle_list[i + (y * size)])
        cols.append(tmp)

    return rows, cols

puzzle1 = [0, 2, 1, 7, 4, 5, 6, 3, 8]
size = 3
generate_rows_cols(puzzle1, size)

#%%
def linear_conflict(puzzle, goal, size):
    rows, cols = generate_rows_cols(puzzle, size)
    goal_rows, goal_cols = generate_rows_cols(goal, size)
    total_lc = 0
    for i, row in enumerate(rows):
        total_lc += calculate_lc(row, goal_rows[i], size)
    for i, col in enumerate(cols):
        total_lc += calculate_lc(col, goal_cols[i], size)
    #cost = manhattan(puzzle, goal) + total_lc * 2
    cost = total_lc
    return (cost)

goal = list(range(0, 9))
puzzle1 = [0, 2, 1, 7, 4, 5, 6, 3, 8]
puzzle2 = [0, 2, 1, 5, 4, 3, 6, 7, 8]
puzzle3 = [2, 7, 0, 5, 4, 3, 8, 1, 6]
size = 3
linear_conflict(puzzle1, goal, size)
linear_conflict(puzzle2, goal, size)
linear_conflict(puzzle3, goal, size)
