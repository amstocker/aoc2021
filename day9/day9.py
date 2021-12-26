from collections import deque

from input import data, width, height


def neighbors(i, j):
    if i + 1 < width: yield (i + 1, j)
    if j + 1 < height: yield (i, j + 1)
    if i - 1 >= 0: yield (i - 1, j)
    if j - 1 >= 0: yield (i, j - 1)


# part 1
risk = 0
for j in range(height):
    for i in range(width):
        if not any(data[l][k] <= data[j][i] for k, l in neighbors(i, j)):
            risk += data[j][i] + 1
print(risk)


# part 2
paths = {}
for j in range(height):
    for i in range(width):
        increases = []
        for k, l in neighbors(i, j):
            if 9 > data[l][k] > data[j][i]:
                increases.append((k, l))
        paths[(i, j)]  = increases

def basin_size(c):
    front = deque(paths[c])
    explored = set([c])
    size = 1
    while len(front) > 0:
        t = front.popleft()
        if t not in explored:
            size += 1
            explored.add(t)
            front.extend(paths[t])
    return size

l = sorted(basin_size((i, j)) for i in range(width) for j in range(height))
print(l[-1] * l[-2] * l[-3])