#!/usr/bin/python3
"""lockboxes"""


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """Determines if all the boxes can be opened."""
    n = len(boxes)
    opened = [False] * n
    opened[0] = True  # The first box is unlocked
    keys = set(boxes[0])  # Start with keys from the first box

    while keys:
        new_keys = set()
        for key in keys:
            if 0 <= key < n and not opened[key]:
                opened[key] = True
                new_keys.update(boxes[key])
        keys = new_keys

    return all(opened)
