# common_exceptions.py — Module 7 Example: Common Python Exceptions
# ITP 270 — Programming for Cybersecurity
# ============================================================

# Python has many built-in exception types.
# Here are the most common ones you'll encounter.

# ============================================================
# EXAMPLE 1: ValueError
# Happens when a value is the wrong format
# ============================================================

print("--- ValueError ---")
try:
    number = int("hello")       # "hello" can't become an integer
except ValueError as e:
    print(f"ValueError: {e}")

try:
    number = int("12.5")        # "12.5" can't be int directly (use float first)
except ValueError as e:
    print(f"ValueError: {e}")

print()

# ============================================================
# EXAMPLE 2: TypeError
# Happens when an operation is used on the wrong type
# ============================================================

print("--- TypeError ---")
try:
    result = "age: " + 25       # Can't add string + integer
except TypeError as e:
    print(f"TypeError: {e}")

try:
    result = len(42)            # Can't get length of an integer
except TypeError as e:
    print(f"TypeError: {e}")

print()

# ============================================================
# EXAMPLE 3: ZeroDivisionError
# Happens when dividing by zero
# ============================================================

print("--- ZeroDivisionError ---")
try:
    result = 100 / 0            # Math says no!
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

try:
    result = 50 % 0             # Modulo by zero too
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

print()

# ============================================================
# EXAMPLE 4: FileNotFoundError
# Happens when opening a file that doesn't exist
# ============================================================

print("--- FileNotFoundError ---")
try:
    file = open("nonexistent_security_log.txt", "r")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

print()

# ============================================================
# EXAMPLE 5: NameError
# Happens when using a variable that hasn't been defined
# ============================================================

print("--- NameError ---")
try:
    print(undefined_variable)   # Never created this variable
except NameError as e:
    print(f"NameError: {e}")

print()

# ============================================================
# EXAMPLE 6: IndexError
# Happens when accessing a list index that doesn't exist
# ============================================================

print("--- IndexError ---")
try:
    ip_list = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]
    print(ip_list[10])          # Only 3 items (index 0, 1, 2)
except IndexError as e:
    print(f"IndexError: {e}")

print()

# ============================================================
# EXAMPLE 7: Handling multiple types in one function
# ============================================================

print("--- Practical Example: Robust Security Function ---")

def safe_lookup(data_list, index_str):
    """Safely look up an item by index from user input.
    Handles: ValueError (bad index), IndexError (out of range)."""
    try:
        index = int(index_str)          # Might raise ValueError
        item = data_list[index]         # Might raise IndexError
        return item
    except ValueError:
        print(f"'{index_str}' is not a valid number.")
        return None
    except IndexError:
        print(f"Index {index_str} is out of range (0-{len(data_list)-1}).")
        return None

servers = ["web-01", "db-01", "fw-01"]
print(f"Lookup 0: {safe_lookup(servers, '0')}")     # web-01
print(f"Lookup 5: {safe_lookup(servers, '5')}")     # Out of range
print(f"Lookup x: {safe_lookup(servers, 'x')}")     # Not a number

print()
print("--- Common Exceptions Demo Complete ---")
