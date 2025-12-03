import argparse


def find_combo(instruct: list[str]) -> int:
    """
    Calculates the number of zero's we pass on a 99 dial combination lock.
    The dial starts at 50.

    Args:
        instruct (list[str]): list of instructions, where the first character is the direction the lock/dial is turning, and the following 1 or 2 digit number is the number of times the dial is turned. 

    Returns: 
        int: number of times the number 0 is passed on the dial during the following of the instructions
    """
    retval = 0
    currentpos = 50
    for ins in instruct:
        print("instruction is ", ins)
        print("Current position is ", currentpos)
        print("Retval is ", retval)
        if ins[0] == "L":
            direction = -1
        else:
            direction = 1
        # for L38 shift should be -38, and for R38 shift should be 38
        shift = direction * int(ins[1:])
        intpos = currentpos + shift
        while intpos > 99 or intpos < 0:
            if intpos < 0:
                intpos = 100 + intpos
            if intpos > 99:
                intpos = intpos - 100
        currentpos = intpos
        if currentpos == 0:
            retval += 1
    return retval


def main():
    instruct = args.instructions
    print(f"Your instructions are: {instruct}")
    num_zero = find_combo(instruct)
    print(f"The number of zeroes your instructions make the dial pass is {num_zero}")


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--instructions', required=True, nargs="*")
    args = parser.parse_args()
    main()
