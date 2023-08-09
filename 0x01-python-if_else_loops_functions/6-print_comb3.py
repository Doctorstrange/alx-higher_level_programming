v#!/usr/bin/python3
for value1 in range(9):
    for value2 in range(value1 + 1, 10):
        print(f"{value1}{value2}", end=", " if value1 < 8 or value2 < 9 else "\n")
