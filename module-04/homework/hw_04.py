# ============================================================
# hw_04.py — Homework: Password Strength Validator
# ITP 270 – Python Programming (Module 4)
# ============================================================
# Build a password validator step by step!
# Each task builds on the previous one.
#
# INSTRUCTIONS:
#   - Replace each TODO with your code
#   - Test after each task by running the file
#   - The password to test is stored in the variable below
# ============================================================

# This is the password you will validate:
password = "MyP@ss7"

print("=" * 50)
print("   🔐 PASSWORD STRENGTH VALIDATOR")
print("=" * 50)
print(f"   Testing password: {password}")
print("=" * 50)


# ============================================================
# TASK 1: Password Length Check
# ============================================================
# Check if the password is at least 8 characters long.
# Use the len() function to get the length.
#
# If it IS long enough:
#   Print "✅ Length: PASS (X characters)"
# If it is NOT long enough:
#   Print "❌ Length: FAIL (X characters, need at least 8)"
#
# Replace X with the actual length.
# ============================================================

print()
print("--- Length Check ---")
# TODO: Write your length check here.
# Hint: len(password) gives you the number of characters.


# ============================================================
# TASK 2: Uppercase Letter Check
# ============================================================
# Check if the password contains at least one uppercase letter.
#
# Use a Boolean variable:
#   has_upper = False
#   Loop through each character and check if it's uppercase.
#   If you find one, set has_upper = True
#
# Print "✅ Uppercase: PASS" or "❌ Uppercase: FAIL"
#
# Hint: Use a for loop and the .isupper() method:
#   for char in password:
#       if char.isupper():
#           has_upper = True
# ============================================================

print()
print("--- Uppercase Check ---")
# TODO: Write your uppercase check here.


# ============================================================
# TASK 3: Number Check
# ============================================================
# Check if the password contains at least one digit (0-9).
#
# Same approach as Task 2, but use .isdigit() instead.
#
# Print "✅ Number: PASS" or "❌ Number: FAIL"
# ============================================================

print()
print("--- Number Check ---")
# TODO: Write your number check here.


# ============================================================
# TASK 4: Combined Strength Checker
# ============================================================
# Using the results from Tasks 1-3, determine the password
# strength. You should have three Boolean-like results.
#
# Strength levels:
#   - All 3 checks pass → "STRONG 💪"
#   - 2 of 3 checks pass → "MEDIUM 🟡"
#   - 1 or 0 checks pass → "WEAK 🔴"
#
# Hint: You can count how many passed:
#   checks_passed = 0
#   if length is good: checks_passed = checks_passed + 1
#   if has uppercase: checks_passed = checks_passed + 1
#   if has number: checks_passed = checks_passed + 1
#
# Then use if-elif-else on checks_passed.
# ============================================================

print()
print("--- Password Strength ---")
# TODO: Write your combined strength checker here.


# ============================================================
# TASK 5: Full Password Validator with Feedback
# ============================================================
# Put it all together! Create a complete validator that:
#
# 1. Checks length (at least 8 characters)
# 2. Checks for uppercase letter
# 3. Checks for lowercase letter (NEW! use .islower())
# 4. Checks for digit
# 5. Checks for special character (!@#$%^&*)
#
# Print a summary with ALL results, then a final verdict:
#   "✅ Password APPROVED — meets all requirements"
#   or
#   "❌ Password REJECTED — fix the issues above"
#
# Hint for special characters:
#   special_chars = "!@#$%^&*"
#   has_special = False
#   for char in password:
#       if char in special_chars:
#           has_special = True
# ============================================================

print()
print("=" * 50)
print("   FULL VALIDATION REPORT")
print("=" * 50)
# TODO: Write your complete password validator here.
# Check all 5 criteria and print the results.


print()
print("=" * 50)
print("   Validation complete.")
print("=" * 50)

# ============================================================
# BONUS (Optional):
# Try changing the password variable at the top and run again!
# Test with these:
#   "abc"          → Should fail most checks
#   "ABCDEFGH"     → Long enough, has uppercase, but no number
#   "Str0ng!Pass"  → Should pass everything
# ============================================================
