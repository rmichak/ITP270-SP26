"""
Program:  First Program — Exploring print() Statements
Course:   ITP 270 — Programming for Cybersecurity
Author:   [Your Name]
Date:     [Today's Date]

Purpose:  This program demonstrates multiple print statements,
          blank lines, and special characters (escape characters).
"""

# --- Part 1: Multiple Print Statements ---
# Each print() creates one line of output.
# Python runs these from top to bottom.
print("Welcome to ITP 270!")
print("Programming for Cybersecurity")
print("Instructor: Randy Michak")

# --- Part 2: Blank Lines for Spacing ---
# Calling print() with nothing inside prints a blank line.
print()

# --- Part 3: Using Special Characters ---
# \n creates a new line INSIDE a string
print("=== Security Alert ===\nUnauthorized access detected\nIP: 192.168.1.100")

print()

# \t creates a tab (indented space)
print("Device Report:")
print("\tRouter:\t\tOnline")
print("\tFirewall:\tOnline")
print("\tServer:\t\tOffline")

print()

# \\ prints a literal backslash (useful for Windows file paths)
print("Log file location: C:\\Users\\Admin\\logs\\security.log")

print()

# \" lets you include double quotes inside a double-quoted string
print("The admin said \"Change your password immediately!\"")

# You can also use single quotes to avoid the escape character
print('The admin said "Change your password immediately!"')
