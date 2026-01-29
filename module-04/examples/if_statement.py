# ============================================================
# ITP 270 — Module 4: The if Statement
# ============================================================
# An if statement runs code ONLY when a condition is True.
# If the condition is False, the indented code is skipped.
# ============================================================

# --- Example 1: Simple if statement ---
print("=== Example 1: Simple if ===")
has_badge = True

if has_badge:
    print("Access granted. Welcome!")  # Only runs if has_badge is True

print("Security check complete.")      # Always runs (not indented)
print()

# --- Example 2: if with False condition ---
print("=== Example 2: Condition is False ===")
has_badge = False

if has_badge:
    print("Access granted. Welcome!")  # SKIPPED — condition is False

print("Security check complete.")      # Still runs
print()

# --- Example 3: Multiple lines in an if block ---
print("=== Example 3: Multiple Lines ===")
password = "secure123"

if password == "secure123":
    print("Password accepted!")      # Runs (condition is True)
    print("Logging you in...")       # Runs (same block)
    print("Welcome back!")           # Runs (same block)

print("Program finished.")           # Always runs (not in if block)
print()

# --- Example 4: if with user input ---
print("=== Example 4: User Input ===")
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to create an account.")

if age < 18:
    print("You must be 18 or older.")

print("Age check done.")

# --- KEY POINTS ---
# 1. The if line MUST end with a colon :
# 2. The code inside must be INDENTED (4 spaces)
# 3. Code NOT indented is outside the if block
# 4. The condition evaluates to True or False
