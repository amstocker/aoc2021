with open("day2_input.txt") as f:
    data = [(l[0], int(l[1])) for l in map(lambda s: s.split(), f.read().strip().splitlines())]

# part 1
x = 0; y = 0
for s, d in data:
    if s == "up":           y -= d
    elif s == "down":       y += d
    elif s == "forward":    x += d
print(x * y)

# part 2
x = 0; y = 0; a = 0
for s, d in data:
    if s == "up":           a -= d
    elif s == "down":       a += d
    elif s == "forward":    x += d; y += (a * d)
print(x * y)