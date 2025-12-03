from solution import find_combo, find_combo_two

def test_puzzle_1():
    assert find_combo(["L68", "L30", "R48", "L5", 
                       "R60", "L55", "L1", "L99", 
                       "R14", "L82"]) == 3

def test_puzzle_2():
    assert find_combo_two(["L68", "L30", "R48", "L5", 
                       "R60", "L55", "L1", "L99", 
                       "R14", "L82"]) == 6
