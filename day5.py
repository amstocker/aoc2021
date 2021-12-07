from re import search

with open("day5_input.txt") as f:
    lines = f.read().strip().split('\n')

segments = []
pattern = r'(.*),(.*) -> (.*),(.*)'
for line in lines:
    m = search(pattern, line)
    segments.append(((int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))))

coords = {}
for s in segments:
    start = s[0]
    end = s[1]
    d = abs(start[0] - end[0]) + abs(start[1] - end[1])
    dx = (end[0] - start[0])/d
    dy = (end[1] - start[1])/d
    if dx != 0 and dy != 0:
        # continue (Part 1)
        dx *= 2
        dy *= 2

    x = start[0]
    y = start[1]

    while (x != end[0]) or (y != end[1]):
        if (x, y) not in coords:
            coords[(x, y)]  = 1
        else:
            coords[(x, y)] += 1
        x = int(x + dx)
        y = int(y + dy)
    if (end[0], end[1]) not in coords:
        coords[(end[0], end[1])]  = 1
    else:
        coords[(end[0], end[1])] += 1

c = 0
for k, v in coords.items():
    if v > 1:
        c += 1

print(c)