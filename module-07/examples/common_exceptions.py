# ============================================================
# common_exceptions.py — Common Python Exceptions
# ITP 270 – Python Programming (Module 7)
# ============================================================
# Here are the most common errors you'll encounter and
# how to handle each one with try-except.
# ============================================================

# =====================
# 1. ValueError
# =====================
# Happens when a function receives the wrong type of value
# Most common: trying to convert a non-number string to int
print("--- 1. ValueError ---")

try:
    number = int("hello")    # "hello" is not a number!
except ValueError:
    print("ValueError: Cannot convert 'hello' to a number.")

try:
    number = int("42")       # This works fine
    print(f"Converted successfully: {number}")
except ValueError:
    print("This won't print — no error occurred.")

# =====================
# 2. TypeError
# =====================
# Happens when you use the wrong data type for an operation
print()
print("--- 2. TypeError ---")

try:
    result = "5" + 3         # Can't add a string and an integer!
except TypeError:
    print("TypeError: Cannot add a string and a number.")
    print("   Fix: Use int('5') + 3, or '5' + str(3)")

try:
    result = len(42)         # len() doesn't work on numbers!
except TypeError:
    print("TypeError: Cannot get length of an integer.")
    print('   Fix: Use len("42") or len(str(42))')

# =====================
# 3. ZeroDivisionError
# =====================
# Happens when you divide by zero
print()
print("--- 3. ZeroDivisionError ---")

try:
    result = 100 / 0         # Cannot divide by zero!
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")
    print("   Always check if the divisor is 0 before dividing.")

# Safe division example
def safe_divide(a, b):
    """Divide a by b, handling division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        print(f"   Cannot divide {a} by 0")
        return None

print(f"10 / 2 = {safe_divide(10, 2)}")   # 5.0
print(f"10 / 0 = {safe_divide(10, 0)}")   # None (error handled)

# =====================
# 4. FileNotFoundError
# =====================
# Happens when you try to open a file that doesn't exist
print()
print("--- 4. FileNotFoundError ---")

try:
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("FileNotFoundError: 'nonexistent_file.txt' does not exist.")
    print("   Check the filename and path.")

# =====================
# 5. IndexError
# =====================
# Happens when you access a list index that doesn't exist
print()
print("--- 5. IndexError ---")

my_list = ["apple", "banana", "cherry"]   # Indices: 0, 1, 2

try:
    print(my_list[5])        # Index 5 doesn't exist!
except IndexError:
    print("IndexError: List index out of range.")
    print(f"   List has {len(my_list)} items (indices 0-{len(my_list)-1})")

# =====================
# 6. KeyError
# =====================
# Happens when you access a dictionary key that doesn't exist
print()
print("--- 6. KeyError ---")

user = {"name": "Alice", "role": "admin"}

try:
    print(user["email"])     # "email" key doesn't exist!
except KeyError:
    print("KeyError: 'email' key not found in dictionary.")
    print(f"   Available keys: {list(user.keys())}")

# =====================
# Catching ANY exception
# =====================
# "except Exception" catches all common errors
# Use this as a last resort — it's better to catch specific errors
print()
print("--- Catching Any Exception ---")

try:
    result = int("not a number")
except Exception as e:
    # 'e' holds the error details
    print(f"An error occurred: {e}")
    print(f"Error type: {type(e).__name__}")

print()
print("✅ Common exceptions complete!")
