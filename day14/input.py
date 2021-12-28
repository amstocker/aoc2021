with open("input.txt") as f:
    lines = f.read().strip().splitlines()

seed = lines[0]
rules = {}
for l in lines[2:]:
    s, t = l.split(" -> ")
    rules[s] = t