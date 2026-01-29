"""
ITP 270 — Module 5: for Loop Basics
====================================
This file shows the simplest for loops — printing numbers,
going through sequences, and understanding how loops repeat.
"""

# --- Example 1: Print "Hello" 5 times ---
# The loop runs 5 times (i = 0, 1, 2, 3, 4)
# We don't even use i here — we just want to repeat
print("=== Example 1: Repeat 5 Times ===")
for i in range(5):
    print("Hello, cybersecurity student!")

print()  # Blank line for spacing

# --- Example 2: Print numbers 1 to 10 ---
# range(1, 11) gives us 1, 2, 3, ..., 10
# Remember: range stops BEFORE the second number!
print("=== Example 2: Numbers 1-10 ===")
for number in range(1, 11):
    print(number)

print()

# --- Example 3: Loop through a list of items ---
# A list holds multiple values in order
# The for loop visits each item one by one
print("=== Example 3: Loop Through a List ===")
protocols = ["HTTP", "HTTPS", "FTP", "SSH", "DNS"]

for protocol in protocols:
    print(f"Protocol: {protocol}")

print()

# --- Example 4: What's inside the loop vs. outside ---
# Only INDENTED code is inside the loop
# Anything NOT indented runs AFTER the loop finishes
print("=== Example 4: Inside vs. Outside the Loop ===")
for i in range(3):
    print(f"  Inside the loop — i = {i}")  # Runs 3 times

print("Outside the loop — this runs once, after the loop ends")
