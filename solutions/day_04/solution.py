from collections import deque

FILE = "solutions/day_04/input.txt"
TEST_FILE = "solutions/day_04/test_input.txt"


def parse_line(line: str) -> tuple[set, set]:
    _, numbers = line.split(":")
    win_nos_str, your_nos_str = numbers.split("|")
    return set(win_nos_str.split()), set(your_nos_str.split())


def solve_part_b():
    sum = 0
    extras = deque()
    with open(FILE) as f:
        for line in f:
            copies = 1
            if extras:
                copies += extras.popleft()
            win_nos, your_nos = parse_line(line.rstrip())
            wins = len(win_nos.intersection(your_nos))
            sum += copies
            if wins:
                for i in range(wins):
                    if i + 1 > len(extras):
                        extras.append(copies)
                    else:
                        extras[i] += copies
    print(sum)


def solve_part_a():
    sum = 0
    with open(FILE) as f:
        for line in f:
            win_nos, your_nos = parse_line(line.rstrip())
            match_nos = win_nos.intersection(your_nos)
            if match_nos:
                sum += 2 ** (len(match_nos) - 1)
    print(sum)


def run():
    solve_part_a()
    solve_part_b()
