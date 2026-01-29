# try_except.py — Module 7 Example: Try-Except Error Handling
# ITP 270 — Programming for Cybersecurity
# ============================================================

# --- What is an exception? ---
# An exception is an error that happens WHILE your program is running.
# Without handling, your program CRASHES.
# try-except lets you CATCH errors and handle them gracefully.

# ============================================================
# EXAMPLE 1: Without try-except (program crashes)
# ============================================================

print("--- Example 1: What happens without try-except ---")
# Uncomment this to see the crash:
# number = int("abc")    # ValueError: invalid literal for int()
# print("This line never runs because the program crashed above")

print("(Uncomment the lines above to see the crash)")
print()

# ============================================================
# EXAMPLE 2: Basic try-except
# ============================================================

print("--- Example 2: Basic try-except ---")

try:
    age_input = "twenty"        # Simulating bad user input
    age = int(age_input)        # This will fail!
    print(f"You are {age} years old.")
except ValueError:
    print("That's not a valid number. Please try again.")

print("Program keeps running! 🎉")
print()

# ============================================================
# EXAMPLE 3: Try-except with user input
# ============================================================

print("--- Example 3: Safe user input ---")

try:
    port = int(input("Enter a port number: "))
    print(f"You entered port {port}.")
except ValueError:
    print("Invalid input — please enter a number next time.")

print()

# ============================================================
# EXAMPLE 4: Try-except INSIDE a function
# ============================================================

print("--- Example 4: Function with error handling ---")

def get_port_number():
    """Safely get a port number from the user."""
    try:
        port = int(input("Enter port number (1-65535): "))
        if 1 <= port <= 65535:
            return port
        else:
            print("Port must be between 1 and 65535.")
            return None
    except ValueError:
        print("Invalid input — please enter a number.")
        return None

result = get_port_number()
if result:
    print(f"Scanning port {result}...")
else:
    print("No valid port entered.")

print()

# ============================================================
# EXAMPLE 5: Multiple except blocks
# ============================================================

print("--- Example 5: Multiple except blocks ---")

def safe_divide(a, b):
    """Divide two numbers safely."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Both values must be numbers!")
        return None

print(f"100 / 4 = {safe_divide(100, 4)}")
print(f"100 / 0 = {safe_divide(100, 0)}")
print(f"100 / 'abc' = {safe_divide(100, 'abc')}")

print()

# ============================================================
# EXAMPLE 6: Catching the error message with 'as'
# ============================================================

print("--- Example 6: Capturing error details ---")

try:
    value = int("not_a_number")
except ValueError as e:
    print(f"Error caught: {e}")
    # Output: Error caught: invalid literal for int() with base 10: 'not_a_number'

print()
print("--- Try-Except Demo Complete ---")
print("Key lesson: try-except = safety net for your code! 🥅")
