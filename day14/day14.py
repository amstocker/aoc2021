from input import seed, rules


# part 1
def iterate(seed, n=1):
    if n <= 0:
        return seed
    new_seed = seed[0] + ''.join(rules[seed[i:i+2]] + seed[i+1] for i in range(len(seed) - 1))
    return iterate(new_seed, n - 1)

def score(string):
    counts = 26 * [0]
    for c in string:
        counts[ord(c) - 65] += 1
    return max(counts) - min(filter(lambda c: c > 0, counts))

print(score(iterate(seed, n=10)))


# part 2
def pair_to_index(pair):
    return (26 * (ord(pair[0]) - 65)) + (ord(pair[1]) - 65)

def index_to_pair(i):
    return chr(i // 26 + 65) + chr(i % 26 + 65)

def seed_to_pair_counts(seed):
    pair_counts = (26 * 26) * [0]
    for i in range(len(seed) - 1):
        pair_counts[pair_to_index(seed[i:i+2])] += 1
    return pair_counts

def iterate_pair_counts(counts, rules, n=1):
    if n <= 0:
        return counts
    new_counts = (26 * 26) * [0]
    for i in range(26 * 26):
        pair = index_to_pair(i)
        if not pair in rules:
            continue
        new_counts[pair_to_index(pair[0] + rules[pair])] += counts[i]
        new_counts[pair_to_index(rules[pair] + pair[1])] += counts[i]
    return iterate_pair_counts(new_counts, rules, n - 1)

def pair_counts_to_char_counts(counts, seed):
    char_counts = 26 * [0]
    for i in range(26 * 26):
        pair = index_to_pair(i)
        char_counts[ord(pair[0]) - 65] += counts[i]
        char_counts[ord(pair[1]) - 65] += counts[i]
    for j in range(26):
        if (j == (ord(seed[0]) - 65)) or (j == (ord(seed[-1]) - 65)):
            char_counts[j] = (char_counts[j] + 1) // 2
        else:
            char_counts[j]  = char_counts[j] // 2
    return char_counts

def score_pair_counts(counts, seed):
    char_counts = pair_counts_to_char_counts(counts, seed)
    return max(char_counts) - min(filter(lambda c: c > 0, char_counts))

pair_counts = iterate_pair_counts(seed_to_pair_counts(seed), rules, n=40)
print(score_pair_counts(pair_counts, seed))
