with open("input.txt") as f:
    data = [tuple(line.split('-')) for line in f.read().strip().splitlines()]