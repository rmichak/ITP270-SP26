# ============================================================
# ITP 270 — Module 4: Comparison Operators
# ============================================================
# Comparison operators compare two values and return True/False.
# Python has six comparison operators.
# ============================================================

print("=== Comparison Operators ===")
print()

# --- Equal To (==) ---
# Checks if two values are the same
print("--- Equal To (==) ---")
print("5 == 5:", 5 == 5)       # True
print("5 == 3:", 5 == 3)       # False
print("'cat' == 'cat':", "cat" == "cat")   # True
print()

# --- Not Equal To (!=) ---
# Checks if two values are different
print("--- Not Equal To (!=) ---")
print("5 != 3:", 5 != 3)       # True  (5 is different from 3)
print("5 != 5:", 5 != 5)       # False (5 is not different from 5)
print()

# --- Less Than (<) ---
print("--- Less Than (<) ---")
print("3 < 5:", 3 < 5)         # True
print("5 < 3:", 5 < 3)         # False
print("5 < 5:", 5 < 5)         # False (not LESS than, it's equal)
print()

# --- Greater Than (>) ---
print("--- Greater Than (>) ---")
print("5 > 3:", 5 > 3)         # True
print("3 > 5:", 3 > 5)         # False
print()

# --- Less Than or Equal To (<=) ---
print("--- Less Than or Equal To (<=) ---")
print("3 <= 5:", 3 <= 5)       # True
print("5 <= 5:", 5 <= 5)       # True  (equal counts!)
print("6 <= 5:", 6 <= 5)       # False
print()

# --- Greater Than or Equal To (>=) ---
print("--- Greater Than or Equal To (>=) ---")
print("5 >= 3:", 5 >= 3)       # True
print("5 >= 5:", 5 >= 5)       # True  (equal counts!)
print("3 >= 5:", 3 >= 5)       # False
print()

# --- Comparing Strings ---
# Strings are compared character by character
# CASE MATTERS!
print("=== String Comparisons ===")
username = "alice"
print("username == 'alice':", username == "alice")   # True  (exact match)
print("username == 'Alice':", username == "Alice")   # False (case differs!)
print("username != 'bob':", username != "bob")       # True  (different)
print()

# --- COMMON MISTAKE: = vs == ---
# = (single) assigns a value
# == (double) compares values
# x = 5    means "store 5 in x"
# x == 5   means "is x equal to 5?"
print("=== Remember: = vs == ===")
x = 5         # Assignment: store 5 in x
print("x == 5:", x == 5)   # Comparison: is x equal to 5? True
print("x == 3:", x == 3)   # Comparison: is x equal to 3? False
