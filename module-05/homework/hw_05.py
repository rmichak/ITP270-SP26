"""
ITP 270 — Module 5: Homework
==============================
Login Attempt Simulator & Loop Practice

Complete all 6 problems. Each problem is independent.
Test your code after EACH problem — don't wait until the end!

If you get an infinite loop (program won't stop), press Ctrl+C.

Name: ___________________
Date: ___________________
"""

# ==============================================================
# Problem 1 — Security Countdown (10 points)
# Count down from 10 to 1, then print "SYSTEM LOCKED"
# Use a for loop with range() and a negative step.
# ==============================================================
print("=== Problem 1: Security Countdown ===")

# TODO: Write a for loop that counts from 10 down to 1
# Hint: range(10, 0, -1) goes 10, 9, 8, ..., 1

# TODO: After the loop, print "🔒 SYSTEM LOCKED"


print()


# ==============================================================
# Problem 2 — Password Character Counter (15 points)
# Ask for a password, then count uppercase, lowercase,
# digits, and special characters.
# ==============================================================
print("=== Problem 2: Password Analysis ===")

# TODO: Ask the user to enter a password using input()

# TODO: Create four counter variables (all start at 0):
#   upper_count, lower_count, digit_count, special_count

# TODO: Write a for loop that goes through each character
#   Use these methods to check:
#     char.isupper() → True if uppercase
#     char.islower() → True if lowercase
#     char.isdigit() → True if digit (0-9)
#     else → special character

# TODO: Print the results:
#   Uppercase letters: X
#   Lowercase letters: X
#   Digits: X
#   Special characters: X


print()


# ==============================================================
# Problem 3 — Network Packet Size Calculator (15 points)
# Ask for packet sizes one at a time. Track count and total.
# Use a while loop.
# ==============================================================
print("=== Problem 3: Packet Calculator ===")

# TODO: Create variables:
#   packet_count = 0
#   total_size = 0
#   keep_going = "yes"

# TODO: Write a while loop that runs while keep_going == "yes"
#   Inside the loop:
#     - Ask for a packet size (convert to float)
#     - Add it to total_size
#     - Add 1 to packet_count
#     - Ask "Add another? (yes/no):" and store the answer

# TODO: After the loop, print:
#   - Number of packets
#   - Total size
#   - Average size (total / count) — be careful about dividing by 0!


print()


# ==============================================================
# Problem 4 — Log Entry Filter (15 points)
# Loop through log entries. Skip "INFO", stop on "CRITICAL".
# ==============================================================
print("=== Problem 4: Log Filter ===")

log_entries = ["INFO", "WARNING", "INFO", "ERROR", "INFO", "CRITICAL", "WARNING"]

# TODO: Create a counter for displayed entries (start at 0)

# TODO: Write a for loop with a position counter
#   For each entry:
#     - If "INFO": use continue to skip it
#     - Otherwise: print the entry with its position number
#                  and add 1 to displayed counter
#     - If "CRITICAL": print a stop message and break

# TODO: After the loop, print how many entries were displayed


print()


# ==============================================================
# Problem 5 — Access Code Grid (15 points)
# Use nested loops to print letter+number combinations.
# ==============================================================
print("=== Problem 5: Access Code Grid ===")
print("Access Code Grid:")

# TODO: Outer loop through letters: ["A", "B", "C"]
#   Inner loop through numbers: range(1, 5) → 1, 2, 3, 4
#     Print each combination (like A1, A2, etc.) on the SAME LINE
#     Hint: print(f"{letter}{number}", end="  ")
#   After the inner loop: print() to start a new line


print()


# ==============================================================
# Problem 6 — Login Attempt Simulator (30 points)
# Build a login system with 3 attempts and lockout.
# This is the main assignment!
# ==============================================================
print("=" * 40)
print("=== Problem 6: Login Simulator ===")
print("=" * 40)

# TODO: Set up variables:
#   correct_password = "CyberSafe2026"
#   max_attempts = 3
#   attempt = 0
#   access_granted = False

# TODO: Print a welcome message

# TODO: Write a while loop that continues while:
#   - attempt is less than max_attempts
#   - AND access has NOT been granted
#
#   Inside the loop:
#     1. Add 1 to attempt
#     2. Print which attempt this is (e.g., "Attempt 1 of 3")
#     3. Ask for the password using input()
#     4. If the password is correct:
#        - Set access_granted to True
#        - Print "Access Granted!" message
#        - Use break to exit the loop
#     5. If the password is wrong:
#        - Calculate remaining attempts (max_attempts - attempt)
#        - Print "Incorrect" with remaining attempts

# TODO: After the loop, check:
#   - If access was NOT granted:
#     - Print "ACCOUNT LOCKED" message
#     - Print "Contact your system administrator."


print()
print("Program complete.")
