# ============================================================
# ITP 270 — Module 4: The if-else Statement
# ============================================================
# if-else creates TWO paths:
#   - if block runs when condition is True
#   - else block runs when condition is False
# Exactly one path always runs — never both, never neither.
# ============================================================

# --- Example 1: Login Check ---
print("=== Example 1: Login Check ===")
password = input("Enter password: ")

if password == "cyber2025":
    print("✓ Login successful!")
    print("Welcome to the system.")
else:
    print("✗ Access denied.")
    print("Incorrect password.")

print("Program ended.")
print()

# --- Example 2: Age Check ---
print("=== Example 2: Age Check ===")
age = int(input("Enter your age: "))

if age >= 18:
    print("You can create a security account.")
else:
    print("You must be 18 or older.")
    print("Come back in", 18 - age, "years!")

print()

# --- Example 3: Even or Odd ---
print("=== Example 3: Even or Odd ===")
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is EVEN.")
else:
    print(number, "is ODD.")

# --- KEY POINTS ---
# 1. else does NOT have a condition (no comparison after else)
# 2. else catches everything the if didn't catch
# 3. else: must have a colon
# 4. The else block must be indented too
# 5. if and else are at the SAME indentation level
