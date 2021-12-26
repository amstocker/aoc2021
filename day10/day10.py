from input import data

open_brackets = ('(', '[', '{', '<')
close_brackets = (')', ']', '}', '>')

bracket_score = {')': 3, ']': 57, '}': 1197, '>': 25137}


def bracket_type(symbol):
    if symbol in open_brackets:
        return open_brackets.index(symbol)
    elif symbol in close_brackets:
        return close_brackets.index(symbol)

def score_stack(stack):
    s = 0
    for c in reversed(stack):
        s *= 5
        s += open_brackets.index(c) + 1
    return s

def score_string(line):
    stack = []
    for c in line:
        if c in open_brackets:
            stack.append(c)
        elif c in close_brackets:
            if bracket_type(c) != bracket_type(stack[-1]):
                return bracket_score[c], score_stack(stack)
            else:
                stack.pop()
    return 0, score_stack(stack)


scores = [score_string(line) for line in data]

# part 1
print(sum(t[0] for t in scores))

# part 2
l = sorted([t[1] for t in scores if t[0] == 0])
print(l[len(l)//2])