# ============================================
# ITP 270 — Module 2: User Input
# ============================================
# The input() function lets your program ask
# the user to type something.
#
# IMPORTANT: input() ALWAYS returns a string!
# You must convert to int or float for numbers.
# ============================================

# --- Basic Input (String) ---
# input() displays a message and waits for the user.
# Whatever they type is stored as a string.

print("=== Basic Input ===")
username = input("Enter your username: ")
print("Hello,", username)
print("Type of username:", type(username))   # Always <class 'str'>

# --- Input with Integer Conversion ---
# If you need a whole number, wrap input() with int().

print("\n=== Integer Input ===")
age = int(input("Enter your age: "))
print("You are", age, "years old")
print("Type of age:", type(age))            # <class 'int'>

# --- Input with Float Conversion ---
# If you need a decimal number, wrap input() with float().

print("\n=== Float Input ===")
gpa = float(input("Enter your GPA: "))
print("Your GPA is", gpa)
print("Type of gpa:", type(gpa))            # <class 'float'>

# --- Why Conversion Matters ---
# Without conversion, you can't do math with input!

print("\n=== Why Conversion Matters ===")
# Try this: enter a number like 10
number_text = input("Enter a number: ")     # This is a STRING
print("Your input:", number_text)
print("Type:", type(number_text))           # <class 'str'>

# Now convert it to do math
number = int(number_text)
doubled = number * 2
print("Doubled:", doubled)                  # Now math works!

# --- Complete Example: Cybersecurity Input ---
print("\n=== Network Scanner Setup ===")
target_ip = input("Enter target IP address: ")
port = int(input("Enter port number to scan: "))
timeout = float(input("Enter timeout in seconds: "))

print("\n--- Scan Configuration ---")
print("Target:", target_ip)
print("Port:", port)
print("Timeout:", timeout, "seconds")
