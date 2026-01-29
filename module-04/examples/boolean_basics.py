# ============================================================
# ITP 270 — Module 4: Boolean Basics
# ============================================================
# Boolean values are either True or False (capitalized!)
# They are the foundation of all decision-making in programs.
# ============================================================

# --- Creating Boolean Variables ---
# Boolean variables store True or False
is_logged_in = True
is_admin = False
has_permission = True

# Print the values
print("=== Boolean Values ===")
print("is_logged_in:", is_logged_in)     # Output: True
print("is_admin:", is_admin)             # Output: False
print("has_permission:", has_permission) # Output: True

# --- Checking the Type ---
# Boolean values have the type 'bool'
print()
print("=== Boolean Type ===")
print("Type of is_logged_in:", type(is_logged_in))   # <class 'bool'>
print("Type of is_admin:", type(is_admin))             # <class 'bool'>

# --- Booleans from Comparisons ---
# When you compare two values, Python gives you a Boolean
print()
print("=== Booleans from Comparisons ===")
age = 20
print("age > 18:", age > 18)           # True (20 is greater than 18)
print("age == 20:", age == 20)         # True (20 equals 20)
print("age < 10:", age < 10)           # False (20 is not less than 10)

# --- Important: Capitalization Matters! ---
# True and False MUST be capitalized
# true (lowercase) will cause a NameError
print()
print("=== Remember ===")
print("True is a Boolean:", True)
print("False is a Boolean:", False)
# print(true)   # This would cause: NameError: name 'true' is not defined
