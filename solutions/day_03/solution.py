from collections import defaultdict
from typing import Iterator

from solutions.common import Grid, Point

FILE = "solutions/day_03/input.txt"
TEST_FILE = "solutions/day_03/test_input.txt"


def yield_nos(grid: Grid[str]) -> Iterator[tuple[int, Point, Point]]:
    """Yields numbers from grid and the first
    and last points of their location.
    """
    _, (max_x, max_y) = grid.bounds
    for y in range(max_y + 1):
        parts: list[tuple[Point, str]] = []
        for x in range(max_x + 1):
            char = grid[Point(x, y)]
            if not char.isnumeric() and parts:
                p_no = int("".join((d for _, d in parts)))
                first_point, _ = parts[0]
                last_point, _ = parts[-1]
                yield p_no, first_point, last_point
                parts.clear()
            elif char.isnumeric():
                parts.append((Point(x, y), char))
        if parts:
            p_no = int("".join((d for _, d in parts)))
            first_point, _ = parts[0]
            last_point, _ = parts[-1]
            yield p_no, first_point, last_point
            parts.clear()


def get_surrounding_points(start: Point, end: Point) -> list[Point]:
    if start.y != end.y or start.x > end.x:
        raise ValueError(
            "Start and end points must be in horizontal line, left to right"
        )
    top_row = [Point(i, start.y - 1) for i in range(start.x - 1, end.x + 2)]
    bottom_row = [Point(i, start.y + 1) for i in range(start.x - 1, end.x + 2)]
    sides = [Point(start.x - 1, start.y), Point(end.x + 1, end.y)]
    return top_row + bottom_row + sides


def is_part_no(grid: Grid[str], start: Point, end: Point) -> bool:
    """Given start and end point of a number, checks adjacent
    squares in grid to see if it's a part number.
    """
    return any(
        (
            grid.get(pt) is not None
            and not grid.get(pt).isnumeric()
            and grid.get(pt) != "."
            for pt in get_surrounding_points(start, end)
        )
    )


def get_adjacent_gears(grid: Grid[str], start: Point, end: Point) -> list[Point]:
    return [pt for pt in get_surrounding_points(start, end) if grid.get(pt) == "*"]


def solve_part_b():
    # Location of gear to part number values
    gears_to_parts: dict[Point, list[int]] = defaultdict(list)
    with open(FILE) as f:
        grid: Grid[str] = Grid.from_file(f)
        for p_no, start_pt, end_pt in yield_nos(grid):
            for gear_pt in get_adjacent_gears(grid, start_pt, end_pt):
                gears_to_parts[gear_pt].append(p_no)

    sum = 0
    for adjacent_parts in gears_to_parts.values():
        if len(adjacent_parts) == 2:
            sum += adjacent_parts[0] * adjacent_parts[1]
    print(sum)


def solve_part_a():
    sum = 0
    with open(FILE) as f:
        grid: Grid[str] = Grid.from_file(f)
        for p_no, start_pt, end_pt in yield_nos(grid):
            sum += int(is_part_no(grid, start_pt, end_pt)) * p_no
    print(sum)


def run():
    solve_part_a()
    solve_part_b()
