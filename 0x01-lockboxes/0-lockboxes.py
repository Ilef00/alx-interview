#!/usr/bin/python3

""" Lock boxes solution """


def canUnlockAll(boxes):
    """Returns true if all boxes can be unlocked and false otherwise"""
    if not boxes:
        return True

    number_of_boxes = len(boxes)
    keys_to_check = set(boxes[0])  # Create a copy of the first box's keys
    set_of_numbers = {0}  # Start with the first box unlocked

    # while loop for handling dynamic changes to the keys to check
    while keys_to_check:
        current_key = (
            keys_to_check.pop()
        )  # Removes and returns an arbitrary item from the set
        if current_key < number_of_boxes:
            if current_key not in set_of_numbers:
                set_of_numbers.add(current_key)
                for key in boxes[current_key]:
                    if key not in set_of_numbers:
                        keys_to_check.add(key)

    return len(set_of_numbers) == number_of_boxes
