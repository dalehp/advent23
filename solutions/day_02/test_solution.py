from . import solution


def test_parse():
    input_str = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    expected = solution.Game(
        id=1,
        moves=[
            {solution.Colour.BLUE: 3, solution.Colour.RED: 4},
            {solution.Colour.RED: 1, solution.Colour.GREEN: 2, solution.Colour.BLUE: 6},
            {solution.Colour.GREEN: 2},
        ],
    )
    actual = solution.parse_game(input_str)
    assert actual == expected
