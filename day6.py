import functools

@functools.lru_cache
def simulate(x, n):
    if n <= x:
        return 1
    else:
        return simulate(7, n - x) + simulate(9, n - x)

def simulate_list(data, n):
    return sum(simulate(x, n) for x in data)

def get_data():
    with open("day6_input.txt") as f:
        return map(int, f.read().strip().split(','))

# part 1
print(simulate_list(get_data(), 80))

# part 2
print(simulate_list(get_data(), 256))
