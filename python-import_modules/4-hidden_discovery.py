#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    filtered_names = [name for name in names if not name.startswith("__")]
    sorted_names = sorted(filtered_names)

    for name in sorted_names:
        print(name)
