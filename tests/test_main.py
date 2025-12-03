from solution import find_combo

def test_site_example():
    assert find_combo(["L68", "L30", "R48", "L5", 
                       "R60", "L55", "L1", "L99", 
                       "R14", "L82"]) == 3
