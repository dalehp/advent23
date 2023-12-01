from . import solution


def test_repeated():
    test_str = "one7eight9gcqmsxdlsqdtqv7"
    result = solution.get_first_and_last_indices(test_str, "7")
    expected = (3, 24)
    assert result == expected


def test_repeated_full():
    test_str = "one7eight9gcqmsxdlsqdtqv7"
    result = solution.get_calibration_value_b(test_str)
    expected = 17
    assert result == expected
