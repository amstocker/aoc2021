from functools import lru_cache

from input import data


@lru_cache
def fish(x, n):
    if n <= x:  return 1
    else:       return fish(7, n - x) + fish(9, n - x)

# part 1
print(sum(fish(x, 80) for x in data))

# part 2
print(sum(fish(x, 256) for x in data))
