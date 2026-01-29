# ============================================================
# try_except.py — Basic Exception Handling (try-except)
# ITP 270 – Python Programming (Module 7)
# ============================================================
# Errors happen! Users type wrong things, files go missing,
# networks go down. Without handling errors, your program
# CRASHES and the user sees an ugly error message.
#
# try-except lets you CATCH errors and handle them gracefully.
#
# Syntax:
#   try:
#       code that MIGHT cause an error
#   except ErrorType:
#       code to run if that error happens
#
# Think of it like a safety net:
#   try    = "attempt this risky action"
#   except = "if it fails, do this instead"
# ============================================================

# --- Without try-except (crashes!) ---
print("--- Without Error Handling ---")
print("If you type 'abc' when asked for a number, the program crashes.")
print("(We'll skip the crash and show try-except instead.)")

# This would crash if user types non-numeric input:
# number = int(input("Enter a number: "))
# print(f"You entered {number}")

# --- With try-except ---
print()
print("--- With Error Handling ---")

# Simulating user input (pretend the user typed "abc")
user_input = "abc"

try:
    # This is the "risky" code — it might fail
    number = int(user_input)             # ❌ "abc" can't become a number!
    print(f"You entered: {number}")
except ValueError:
    # This runs ONLY if a ValueError occurs
    print(f'❌ "{user_input}" is not a valid number!')
    print("   Please enter a whole number like 5 or 42.")

print("Program continues running!")  # This always prints — no crash!

# --- Successful try (no error) ---
print()
print("--- Successful Try ---")

user_input = "42"

try:
    number = int(user_input)             # ✅ "42" CAN become a number
    print(f"You entered: {number}")      # This runs
except ValueError:
    print("Not a valid number!")          # This is SKIPPED (no error)

print("Program continues.")

# --- Multiple except blocks ---
print()
print("--- Multiple Except Blocks ---")

def safe_divide(a, b):
    """Safely divide two numbers with error handling."""
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
    except ZeroDivisionError:
        print(f"❌ Cannot divide {a} by zero!")
    except TypeError:
        print(f"❌ Invalid types: can't divide {type(a)} by {type(b)}")

safe_divide(10, 3)       # Works: 10 / 3 = 3.333...
safe_divide(10, 0)       # ZeroDivisionError caught
safe_divide("10", 3)     # TypeError caught

# --- try-except-else-finally ---
print()
print("--- Full Structure: try-except-else-finally ---")

user_input = "25"

try:
    # Risky code
    age = int(user_input)
except ValueError:
    # Runs if there's an error
    print("❌ Invalid age!")
else:
    # Runs ONLY if there was NO error
    print(f"✅ Age is {age}")
finally:
    # Runs NO MATTER WHAT (error or not)
    print("Age check complete.")

# --- Practical: Safe user input function ---
print()
print("--- Practical: Safe Input ---")

def get_number(prompt_text, user_response):
    """
    Safely convert user input to a number.
    Returns the number or None if invalid.
    """
    try:
        value = int(user_response)
        print(f"✅ Got valid number: {value}")
        return value
    except ValueError:
        print(f"❌ '{user_response}' is not a valid number.")
        return None

# Test it:
result = get_number("Enter port number: ", "8080")   # Valid
print(f"Result: {result}")

result = get_number("Enter port number: ", "http")    # Invalid
print(f"Result: {result}")

print()
print("✅ try-except basics complete!")
