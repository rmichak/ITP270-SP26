"""
ITP 270 — Module 5: Nested Loops
==================================
A nested loop is a loop INSIDE another loop.
The inner loop runs completely for each run of the outer loop.
"""

# --- Example 1: Simple nested loop ---
# Outer: 3 floors, Inner: 3 rooms
print("=== Example 1: Building Security Check ===")
for floor in range(1, 4):                   # Floors 1, 2, 3
    for room in ["A", "B", "C"]:            # Rooms A, B, C
        print(f"  Checking Floor {floor}, Room {room}")
    print(f"  --- Floor {floor} complete ---")

print(f"All floors checked.\n")

# --- Example 2: Grid/table ---
# Print a multiplication table (1-5)
print("=== Example 2: Multiplication Table ===")
print("     ", end="")
for i in range(1, 6):
    print(f"{i:>4}", end="")
print()
print("     " + "----" * 5)

for row in range(1, 6):                     # Rows 1-5
    print(f"  {row} |", end="")
    for col in range(1, 6):                 # Columns 1-5
        print(f"{row * col:>4}", end="")    # Multiply and print
    print()                                 # New line after each row

print()

# --- Example 3: Cybersecurity — IP range scan ---
# Scan a small subnet: 192.168.1.1 through 192.168.3.3
print("=== Example 3: IP Range Scan ===")
for third_octet in range(1, 4):             # .1.x, .2.x, .3.x
    print(f"  Scanning subnet 192.168.{third_octet}.x")
    for fourth_octet in range(1, 4):        # .x.1, .x.2, .x.3
        ip = f"192.168.{third_octet}.{fourth_octet}"
        print(f"    → {ip}")

print()

# --- Example 4: How many times does the inner code run? ---
# Outer runs M times, Inner runs N times → total = M × N
print("=== Example 4: Counting Iterations ===")
total_runs = 0

for i in range(4):       # Outer: 4 times
    for j in range(3):   # Inner: 3 times
        total_runs += 1

print(f"Outer loop: 4 times")
print(f"Inner loop: 3 times")
print(f"Total runs: {total_runs} (4 × 3 = 12)")
print()

# --- Example 5: Access code grid ---
# Combine letters and numbers
print("=== Example 5: Access Code Grid ===")
letters = ["A", "B", "C", "D"]
numbers = range(1, 5)

for letter in letters:
    for num in numbers:
        print(f"{letter}{num}", end="  ")
    print()  # New line after each row
