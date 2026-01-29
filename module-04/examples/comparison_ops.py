# ============================================================
# comparison_ops.py — Comparison Operators in Python
# ITP 270 – Python Programming (Module 4)
# ============================================================
# Comparison operators compare two values and return
# True or False. These are essential for decision-making.
#
# Operator  | Meaning                | Example
# ----------|------------------------|----------
#   ==      | Equal to               | 5 == 5  → True
#   !=      | Not equal to           | 5 != 3  → True
#   <       | Less than              | 3 < 5   → True
#   >       | Greater than           | 5 > 3   → True
#   <=      | Less than or equal     | 5 <= 5  → True
#   >=      | Greater than or equal  | 5 >= 3  → True
# ============================================================

# --- Equal to (==) ---
# IMPORTANT: == checks equality, = assigns a value!
print("--- Equal To (==) ---")
print("5 == 5:", 5 == 5)           # True — same value
print("5 == 3:", 5 == 3)           # False — different values
print('"cat" == "cat":', "cat" == "cat")   # True — same string
print('"cat" == "Cat":', "cat" == "Cat")   # False — capitalization matters!

# --- Not equal to (!=) ---
print()
print("--- Not Equal To (!=) ---")
print("5 != 3:", 5 != 3)           # True — they ARE different
print("5 != 5:", 5 != 5)           # False — they are the same
print('"yes" != "no":', "yes" != "no")   # True — different strings

# --- Less than (<) ---
print()
print("--- Less Than (<) ---")
print("3 < 5:", 3 < 5)             # True — 3 is less than 5
print("5 < 3:", 5 < 3)             # False — 5 is NOT less than 3
print("5 < 5:", 5 < 5)             # False — 5 is NOT less than 5 (equal)

# --- Greater than (>) ---
print()
print("--- Greater Than (>) ---")
print("10 > 2:", 10 > 2)           # True — 10 is greater than 2
print("2 > 10:", 2 > 10)           # False — 2 is NOT greater than 10
print("5 > 5:", 5 > 5)             # False — 5 is NOT greater than 5 (equal)

# --- Less than or equal (<=) ---
print()
print("--- Less Than or Equal (<=) ---")
print("3 <= 5:", 3 <= 5)           # True — 3 is less than 5
print("5 <= 5:", 5 <= 5)           # True — 5 IS equal to 5
print("7 <= 5:", 7 <= 5)           # False — 7 is NOT less than or equal to 5

# --- Greater than or equal (>=) ---
print()
print("--- Greater Than or Equal (>=) ---")
print("10 >= 5:", 10 >= 5)         # True — 10 is greater than 5
print("5 >= 5:", 5 >= 5)           # True — 5 IS equal to 5
print("3 >= 5:", 3 >= 5)           # False — 3 is NOT >= 5

# --- Practical cybersecurity example ---
print()
print("--- Cybersecurity Example ---")

password_length = 6
min_required = 8

# Check if password meets minimum length
meets_requirement = password_length >= min_required
print(f"Password length: {password_length}")
print(f"Minimum required: {min_required}")
print(f"Meets requirement? {meets_requirement}")  # False — 6 < 8

# Check login attempts
login_attempts = 3
max_attempts = 5

too_many = login_attempts >= max_attempts
print(f"\nLogin attempts: {login_attempts}")
print(f"Max allowed: {max_attempts}")
print(f"Account locked? {too_many}")  # False — 3 < 5

print()
print("✅ Comparison operators complete!")
