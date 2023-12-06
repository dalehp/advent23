from dataclasses import dataclass
from enum import Enum, auto
from functools import reduce

FILE = "solutions/day_02/input.txt"
TEST_FILE = "solutions/day_02/test_input.txt"


class Colour(Enum):
    BLUE = auto()
    RED = auto()
    GREEN = auto()


Move = dict[Colour, int]


@dataclass
class Game:
    id: int
    moves: list[Move]


def parse_game(s: str) -> Game:
    game_str, moves_str = s.split(": ")
    _, id_str = game_str.split("Game ")
    move_str_list = moves_str.split("; ")

    moves: list[Move] = []
    for move_str in move_str_list:
        colours_strs = move_str.split(", ")
        move: Move = {}
        for colour_str in colours_strs:
            q_str, c_str = colour_str.split(" ")
            move[Colour[c_str.upper()]] = int(q_str)
        moves.append(move)

    return Game(id=int(id_str), moves=moves)


def solve_part_b():
    count = 0
    with open(FILE) as f:
        for line in f:
            game = parse_game(line.rstrip())
            min_cubes: Move = {c: 0 for c in Colour}
            for move in game.moves:
                for c in Colour:
                    min_cubes[c] = max(min_cubes[c], move.get(c, 0))
            count += reduce(lambda x, y: x * y, min_cubes.values())
    print(count)


def solve_part_a():
    max_red = 12
    max_green = 13
    max_blue = 14

    count = 0
    with open(FILE) as f:
        for line in f:
            game = parse_game(line.rstrip())
            count += game.id * int(
                all(
                    m.get(Colour.RED, 0) <= max_red
                    and m.get(Colour.GREEN, 0) <= max_green
                    and m.get(Colour.BLUE, 0) <= max_blue
                    for m in game.moves
                )
            )
    print(count)


def run():
    solve_part_a()
    solve_part_b()
