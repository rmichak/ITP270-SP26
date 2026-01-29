# ============================================================
# boolean_basics.py — Introduction to Boolean Values
# ITP 270 – Python Programming (Module 4)
# ============================================================
# Booleans are one of the simplest data types in Python.
# There are only two Boolean values: True and False
# They are used to make decisions in your programs.
# ============================================================

# --- Boolean values ---
# True and False must be capitalized (they are keywords)
is_logged_in = True       # The user IS logged in
is_admin = False          # The user is NOT an admin

# Print the values
print("is_logged_in:", is_logged_in)   # Output: is_logged_in: True
print("is_admin:", is_admin)           # Output: is_admin: False

# --- Check the type ---
# type() tells us what kind of data we have
print()
print("Type of True:", type(True))             # Output: <class 'bool'>
print("Type of False:", type(False))           # Output: <class 'bool'>
print("Type of is_logged_in:", type(is_logged_in))  # Output: <class 'bool'>

# --- Comparisons produce Boolean results ---
# When you compare two values, Python gives you True or False
print()
print("--- Comparison Results ---")
print("5 == 5:", 5 == 5)     # Output: True  (5 equals 5)
print("5 == 3:", 5 == 3)     # Output: False (5 does not equal 3)
print("10 > 2:", 10 > 2)     # Output: True  (10 is greater than 2)
print("1 > 100:", 1 > 100)   # Output: False (1 is NOT greater than 100)

# --- Booleans from expressions ---
# You can store comparison results in variables
age = 20
is_adult = age >= 18       # True, because 20 >= 18
print()
print("Age:", age)
print("Is adult?", is_adult)  # Output: Is adult? True

password_length = 4
is_strong = password_length >= 8   # False, because 4 is NOT >= 8
print()
print("Password length:", password_length)
print("Is strong password?", is_strong)  # Output: Is strong password? False

# --- bool() function ---
# You can convert other values to Boolean using bool()
# In Python: 0, empty string "", and None are False
# Everything else is True
print()
print("--- bool() conversions ---")
print("bool(1):", bool(1))       # Output: True  (any non-zero number)
print("bool(0):", bool(0))       # Output: False (zero is False)
print('bool("hello"):', bool("hello"))  # Output: True  (non-empty string)
print('bool(""):', bool(""))     # Output: False (empty string is False)
print("bool(None):", bool(None)) # Output: False (None is False)

print()
print("✅ Boolean basics complete!")
