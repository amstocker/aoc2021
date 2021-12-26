with open("input.txt") as f:
    data = [list(map(int, line)) for line in f.read().strip().splitlines()]

width = len(data[0])
height = len(data)
