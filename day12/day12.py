from functools import lru_cache
from collections import defaultdict

from input import data


Start = "start"
End = "end"

Paths = defaultdict(list)
for t in data:
    Paths[t[0]].append(t[1])
    Paths[t[1]].append(t[0])

# part 1
@lru_cache
def count_paths(a, b, history=()):
    if a in history:
        return 0
    if a == b:
        return 1
    if a[0].islower():
        history += (a,)
    return sum(count_paths(t, b, history) for t in Paths[a])

print(count_paths(Start, End))

# part 2
@lru_cache
def count_paths2(a, b, history=(), twice=False):
    if a in history:
        if twice or a == Start:
            return 0
        else:
            twice = True
    if a == b:
        return 1
    if a[0].islower():
        history += (a,)
    return sum(count_paths2(t, b, history, twice) for t in Paths[a])

print(count_paths2(Start, End))