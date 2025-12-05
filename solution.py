import argparse
import math


def _find_zeros_and_pos(instruction: str, currentpos: int) -> (int, int):
    """
    Given an instruction and position it calculates the number of times we pass zero, and the new position

    Args:
        Instruction str: "R43" Dial goes "right" 43 positions
        Currentpos int: a integer indicating where the dial is at now

    Returns:
        num_zeros and new position (int int)
    """
    magnitude = int(instruction[1:])
    if instruction[0] == "R":
        newpos = (magnitude + currentpos) % 100
        print(magnitude+currentpos)
        num_zero = (magnitude + currentpos) // 100

    if instruction[0] == "L":
        if currentpos == 0:
            newpos = (100 - magnitude) % 100
            num_zero = (magnitude // 100)
        elif magnitude > currentpos:
            newpos = (100 - (magnitude - currentpos)) % 100
            num_zero = ((magnitude - currentpos) // 100) + 1 
        else:
            newpos = currentpos - magnitude
            if newpos == 0:
                num_zero = 1
            else:
                num_zero = 0
    return num_zero, newpos


def find_combo_two(instruct: list[str]) -> int:
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
    print("RAH")
    for ins in instruct:
        print(retval, ins, currentpos)
        delta_retval, currentpos = _find_zeros_and_pos(ins, currentpos)
        retval += delta_retval
        print(retval, currentpos)
    return retval


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
    function = int(args.fun)
    if function == 2:
        num_zero = find_combo_two(instruct)
    else:
        num_zero = find_combo(instruct)
    print(f"Your instructions are: {instruct}")
    print(f"The number of zeroes your instructions make the dial pass is {num_zero}")
    print(function)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--instructions", required=True, nargs="*")
    parser.add_argument("--fun")
    args = parser.parse_args()
    main()
