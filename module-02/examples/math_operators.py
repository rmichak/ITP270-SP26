# ============================================
# ITP 270 — Module 2: Math Operators
# ============================================
# Python has 7 math operators:
#   +   Addition
#   -   Subtraction
#   *   Multiplication
#   /   Division (always gives a float)
#   //  Floor Division (drops the decimal)
#   %   Modulus (remainder)
#   **  Exponent (power)
# ============================================

# --- Addition (+) ---
print("=== Addition ===")
login_attempts = 5
new_attempts = 3
total_attempts = login_attempts + new_attempts
print("Total attempts:", total_attempts)     # Output: 8

# --- Subtraction (-) ---
print("\n=== Subtraction ===")
max_attempts = 10
used_attempts = 7
remaining = max_attempts - used_attempts
print("Remaining attempts:", remaining)      # Output: 3

# --- Multiplication (*) ---
print("\n=== Multiplication ===")
devices = 8
ports_per_device = 4
total_ports = devices * ports_per_device
print("Total ports:", total_ports)           # Output: 32

# --- Division (/) ---
# IMPORTANT: Division always gives a float (decimal number)!
print("\n=== Division ===")
total_bandwidth = 100     # Mbps
users = 4
speed_per_user = total_bandwidth / users
print("Speed per user:", speed_per_user, "Mbps")  # Output: 25.0
print("Type:", type(speed_per_user))               # <class 'float'>

# Even "clean" division gives a float:
print("10 / 2 =", 10 / 2)                  # Output: 5.0 (float!)

# --- Floor Division (//) ---
# Drops the decimal part (does NOT round!)
print("\n=== Floor Division ===")
print("10 // 3 =", 10 // 3)                # Output: 3
print("7 // 2 =", 7 // 2)                  # Output: 3
print("15 // 4 =", 15 // 4)                # Output: 3

# Practical example: how many full days in 100 hours?
total_hours = 100
full_days = total_hours // 24
print("100 hours =", full_days, "full days") # Output: 4 full days

# --- Modulus (%) ---
# Gives the REMAINDER after division.
print("\n=== Modulus (Remainder) ===")
print("10 % 3 =", 10 % 3)                  # Output: 1 (10÷3 = 3 remainder 1)
print("7 % 2 =", 7 % 2)                    # Output: 1 (odd number)
print("8 % 2 =", 8 % 2)                    # Output: 0 (even number)

# Practical example: remaining hours after full days
remaining_hours = total_hours % 24
print("100 hours =", full_days, "days and", remaining_hours, "hours")
# Output: 100 hours = 4 days and 4 hours

# --- Exponent (**) ---
# Raises a number to a power.
print("\n=== Exponent (Power) ===")
print("2 ** 8 =", 2 ** 8)                  # Output: 256
print("2 ** 16 =", 2 ** 16)                # Output: 65536
print("2 ** 32 =", 2 ** 32)                # Output: 4294967296

# Practical example: password combinations
charset = 26        # lowercase letters only
length = 4
combinations = charset ** length
print("\nPassword combinations:")
print(charset, "characters,", length, "long =", combinations, "possibilities")
# Output: 26 characters, 4 long = 456976 possibilities

# --- Summary: All 7 Operators ---
print("\n=== All 7 Operators Summary ===")
a = 10
b = 3
print(f"{a} + {b} = {a + b}")       # 13
print(f"{a} - {b} = {a - b}")       # 7
print(f"{a} * {b} = {a * b}")       # 30
print(f"{a} / {b} = {a / b}")       # 3.333...
print(f"{a} // {b} = {a // b}")     # 3
print(f"{a} % {b} = {a % b}")       # 1
print(f"{a} ** {b} = {a ** b}")     # 1000
