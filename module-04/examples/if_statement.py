# ============================================================
# if_statement.py — The Simple if Statement
# ITP 270 – Python Programming (Module 4)
# ============================================================
# The if statement lets your program make decisions.
# It runs a block of code ONLY when a condition is True.
#
# Syntax:
#   if condition:
#       code to run (indented)
#
# KEY RULES:
# 1. The condition must end with a colon (:)
# 2. The code inside must be INDENTED (4 spaces)
# 3. The indented code only runs if condition is True
# ============================================================

# --- Basic if statement ---
temperature = 100

# This code ONLY runs if temperature is above 90
if temperature > 90:
    print("WARNING: Temperature is too high!")   # This prints because 100 > 90

print("System check complete.")  # This ALWAYS prints (not indented under if)

# --- Another example ---
print()
print("--- Login Attempt Example ---")

login_attempts = 3

# Check if attempts exceeded the limit
if login_attempts >= 3:
    print("⚠️  Too many login attempts!")    # This prints because 3 >= 3
    print("Account is temporarily locked.")   # This also prints (same indent)

print("Returning to login screen.")  # This ALWAYS prints

# --- Example where condition is False ---
print()
print("--- False Condition Example ---")

score = 50

# This code will NOT run because 50 is not greater than 100
if score > 100:
    print("This will NOT print.")  # Skipped! 50 is NOT > 100

print("Score check done.")  # This ALWAYS prints

# --- Multiple if statements (each checked independently) ---
print()
print("--- Multiple Independent Checks ---")

password_length = 10

# Each if is checked separately — they don't affect each other
if password_length >= 8:
    print("✅ Password is long enough.")       # Prints (10 >= 8)

if password_length >= 12:
    print("✅ Password is extra strong.")       # Does NOT print (10 < 12)

if password_length >= 6:
    print("✅ Password meets minimum length.")  # Prints (10 >= 6)

# --- Common beginner mistake ---
print()
print("--- Indentation Matters! ---")

is_admin = True

if is_admin:
    print("Welcome, administrator!")   # Only prints if is_admin is True
    print("You have full access.")     # Also only prints if is_admin is True

# If you forget to indent, it's NOT part of the if block:
# print("This always runs")  ← NOT indented, so it runs regardless

print()
print("✅ if statement examples complete!")
