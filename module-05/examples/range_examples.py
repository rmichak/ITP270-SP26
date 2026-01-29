"""
ITP 270 — Module 5: range() Examples
======================================
The range() function generates numbers.
Think of it as a number-making machine.
You control where it starts, stops, and how it counts.
"""

# --- range(stop) — One argument ---
# Starts at 0, counts up to (but NOT including) the number
print("=== range(5) — Starts at 0, stops before 5 ===")
for i in range(5):
    print(i, end="  ")  # end="  " keeps output on one line
print()  # New line after the loop
# Output: 0  1  2  3  4

print()

# --- range(start, stop) — Two arguments ---
# Starts at the first number, stops before the second
print("=== range(1, 6) — Starts at 1, stops before 6 ===")
for i in range(1, 6):
    print(i, end="  ")
print()
# Output: 1  2  3  4  5

print()

# --- range(start, stop, step) — Three arguments ---
# Third number is the STEP (how much to add each time)

# Count by 2s (even numbers)
print("=== range(0, 20, 2) — Even numbers 0-18 ===")
for i in range(0, 20, 2):
    print(i, end="  ")
print()
# Output: 0  2  4  6  8  10  12  14  16  18

print()

# Count by 5s
print("=== range(0, 51, 5) — Count by 5s ===")
for i in range(0, 51, 5):
    print(i, end="  ")
print()
# Output: 0  5  10  15  20  25  30  35  40  45  50

print()

# Count BACKWARDS (negative step)
print("=== range(10, 0, -1) — Countdown 10 to 1 ===")
for i in range(10, 0, -1):
    print(i, end="  ")
print()
# Output: 10  9  8  7  6  5  4  3  2  1

print()

# --- Cybersecurity example: Port range ---
print("=== Cyber Example: Port Range 80-90 ===")
for port in range(80, 91):
    print(f"Port {port}")
