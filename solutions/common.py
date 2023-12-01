from __future__ import annotations

from dataclasses import astuple, dataclass
from typing import Callable, Generic, Iterator, Optional, TextIO, TypeVar


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0

    def __add__(self, o: Point) -> Point:
        return Point(x=self.x + o.x, y=self.y + o.y)

    def __mul__(self, o: int) -> Point:
        return Point(x=o * self.x, y=o * self.y)

    def __rmul__(self, o: int) -> Point:
        return self.__mul__(o)

    def __iter__(self):
        return iter(astuple(self))


T = TypeVar("T")


class Grid(Generic[T]):
    def __init__(self):
        self.grid: dict[Point, T] = {}

    def __iter__(self) -> Iterator[tuple[Point, T]]:
        for position, value in self.grid.items():
            yield position, value

    def __getitem__(self, p: Point) -> T:
        return self.grid[p]

    def __setitem__(self, p: Point, v: T):
        self.grid[p] = v

    def __contains__(self, p: Point) -> bool:
        return p in self.grid

    def __len__(self) -> int:
        return len(self.grid)

    def __add__(self, o: Grid) -> Grid:
        return self.from_dict({**self.grid, **o.grid})

    def get(self, p: Point) -> Optional[T]:
        return self.grid.get(p)

    @staticmethod
    def from_dict(d: dict[Point, T]) -> Grid:
        grid: Grid[T] = Grid()
        grid.grid = d
        return grid

    @staticmethod
    def from_file(f: TextIO, value_factory: Callable[[str], T]) -> Grid:
        grid: Grid[T] = Grid()
        for j, line in enumerate(f):
            for i, character in enumerate(line.rstrip()):
                grid[Point(i, j)] = value_factory(character)
        return grid

    def __str__(self) -> str:
        min_point, max_point = self.bounds
        min_x = min_point.x
        max_x = max_point.x
        min_y = min_point.y
        max_y = max_point.y

        return (
            "\n".join(
                "".join(str(self[Point(i, j)]) for i in range(min_x, max_x + 1))
                for j in range(min_y, max_y + 1)
            )
            + "\n"
        )

    @property
    def bounds(self) -> tuple[Point, Point]:
        min_x = min(p.x for p in self.grid.keys())
        max_x = max(p.x for p in self.grid.keys())
        min_y = min(p.y for p in self.grid.keys())
        max_y = max(p.y for p in self.grid.keys())
        return Point(min_x, min_y), Point(max_x, max_y)


ULDR = (Point(0, -1), Point(0, 1), Point(-1, 0), Point(1, 0))


def get_adjacent_values(grid: Grid[T], point: Point) -> list[T]:
    return [h for p in ULDR if (h := grid.get(point + p)) is not None]


def adjacent_points_and_values(grid: Grid[T], point: Point) -> list[tuple[Point, T]]:
    return [(point + p, h) for p in ULDR if (h := grid.get(point + p)) is not None]
