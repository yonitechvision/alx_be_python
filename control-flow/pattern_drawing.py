#!/bin/bash
# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))
# Draw the pattern
row = 0
while row < size:
    for _ in range(size):
        print("*", end="")
    print()  # Newline after each row
    row += 1
