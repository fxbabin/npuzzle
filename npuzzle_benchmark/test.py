
def move_right(puzzle, goal, idx, size):
    if puzzle[idx] in goal:
        idx += 1
    while(idx % size != 0 or idx == 0):
        if puzzle[idx] in goal:
            break
        goal.append(puzzle[idx])
        idx += 1
    return(idx - 1)

def move_left(puzzle, goal, idx, size):
    if puzzle[idx] in goal:
        idx -= 1
    while(idx % size != (size - 1) or idx == 0):
        if puzzle[idx] in goal:
            break
        goal.append(puzzle[idx])
        idx -= 1
    return(idx + 1)

def move_down(puzzle, goal, idx, size):
    if puzzle[idx] in goal:
        idx += size
    while(idx < (size ** 2)):
        if puzzle[idx] in goal:
            break
        goal.append(puzzle[idx])
        idx += size
    return(idx - size)

def move_up(puzzle, goal, idx, size):
    if puzzle[idx] in goal:
        idx -= size
    while(idx > 0):
        if puzzle[idx] not in goal:
            goal.append(puzzle[idx])
        idx -= size
    return(idx + size)

# def move_down(puzzle, goal, idx, size):
#     while(idx < (size ** 2)):
#         goal.append(puzzle[idx])
#         idx += 3
#     return(idx)

# goal = []
# idx = 0
# idx = move_right([1,2,3,8,0,4,7,6,5], goal, idx, 3)
# idx = move_down([1,2,3,8,0,4,7,6,5], goal, idx, 3)
# idx = move_left([1,2,3,8,0,4,7,6,5], goal, idx, 3)
# idx = move_up([1,2,3,8,0,4,7,6,5], goal, idx, 3)
# idx = move_right([1,2,3,8,0,4,7,6,5], goal, idx, 3)
# print(goal, idx)
def dd(puzzle, size):
    goal = []
    idx = 0

    while (len(goal) < (size ** 2)):
        idx = move_right(puzzle, goal, idx, size)
        idx = move_down(puzzle, goal, idx, size)
        idx = move_left(puzzle, goal, idx, size)
        idx = move_up(puzzle, goal, idx, size)
    return (goal)
puz1 = [1,2,3,4,12,13,14,5,11,0,15,6,10,9,8,7]
puz2 = [1,2,3,8,0,4,7,6,5]
res = dd([1,2,3,4,12,13,14,5,11,0,15,6,10,9,8,7], 4)
res2 = dd(puz2, 3)

def get_permutation_score(puzzle, size):
    idx = 0
    score = 0
    for e1 in puzzle:
        for e2 in puzzle[:idx]:
            if e2 > e1 and e1 != 0 and e2 != 0:
                score += 1
        idx += 1
    return (score)

print(res)
print(get_permutation_score(res, 4))
print(get_permutation_score(puz1, 4))
print(res2)
print(get_permutation_score(res2, 4))
print(get_permutation_score(puz2, 4))
#print(goal, idx)


res = dd([1, 0, 4, 15, 12, 13, 14, 5, 2, 3, 7, 8, 11, 10, 6, 9], 4)
print(get_permutation_score(res, 4))
print(get_permutation_score([1, 0, 4, 15, 12, 13, 14, 5, 2, 3, 7, 8, 11, 10, 6, 9], 4))

res2 = dd([2, 0, 13, 14, 1, 12, 15, 5, 11, 3, 8, 4, 10, 9, 7, 6], 4)
print(get_permutation_score(res2, 4))
print(get_permutation_score([2, 0, 13, 14, 1, 12, 15, 5, 11, 3, 8, 4, 10, 9, 7, 6], 4))