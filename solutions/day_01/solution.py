FILE = "solutions/day_01/input.txt"
TEST_FILE = "solutions/day_01/test_input.txt"

DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def get_first_and_last_indices(line: str, substr: str) -> tuple[int, int]:
    first_idx = line.find(substr)
    first, last = first_idx, first_idx
    while (curr_idx := line.find(substr, last + 1)) != -1:
        last = curr_idx
    return first, last


def get_calibration_value_b(line: str) -> int:
    first_index = len(line)
    last_index = -1
    first_number, last_number = "", ""
    for s in DIGITS.keys():
        idx_first, idx_s_last = get_first_and_last_indices(line, s)
        if idx_first != -1 and idx_first < first_index:
            first_number = DIGITS[s]
            first_index = idx_first
        if idx_s_last != -1 and idx_s_last > last_index:
            last_number = DIGITS[s]
            last_index = idx_s_last

    return int(f"{first_number}{last_number}")


def solve_part_b():
    count = 0
    with open(FILE) as f:
        for line in f:
            value = get_calibration_value_b(line)
            print(value)
            count += value
    print(count)


def solve_part_a():
    count = 0
    with open(FILE) as f:
        for line in f:
            numbers = "".join((c for c in line.rstrip() if c.isdigit()))
            first_number = numbers[0]
            last_number = numbers[-1]
            combined = int(f"{first_number}{last_number}")
            count += combined
    print(count)


def run():
    solve_part_a()
    solve_part_b()
