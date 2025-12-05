from solution import find_combo, find_combo_two, _find_zeros_and_pos
import math


def test_puzzle_1():
    assert (
        find_combo(["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"])
        == 3
    )


def test_puzzle_2():
    assert (
        find_combo_two(
            ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
        )
        == 6
    )


#def test_puzzle_3():
 #   number = int(
  #      math.floor(423423 - 50) / 100
  #      + int(math.floor((132412 + (423423 - 50) % 100) / 100))
  #  )
  #  assert find_combo_two(["L423423", "R132412"]) == number


def test_puzzle_4():
    # Hint used from https://www.reddit.com/r/adventofcode/comments/1pdq3yc/comment/ns6wkcv/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    assert find_combo_two(["L50", "R101"]) == 2


def test_puzzle_5():
    assert _find_zeros_and_pos("L55", 55) == (1, 0)


def test_puzzle_6():
    assert _find_zeros_and_pos("R48", 52) == (1, 0)


def test_puzzle_7():
    assert _find_zeros_and_pos("R48", 53) == (1, 1)


def test_puzzle_8():
    assert _find_zeros_and_pos("R148", 53) == (2, 1)


def test_puzzle_9():
    assert _find_zeros_and_pos("L155", 55) == (2, 0)


def test_puzzle_10():
    assert _find_zeros_and_pos("L55", 54) == (1, 99)


def test_puzzle_11():
    assert _find_zeros_and_pos("L155", 54) == (2, 99)

def test_puzzle_12():
    assert _find_zeros_and_pos("L5", 0) == (0, 95)
