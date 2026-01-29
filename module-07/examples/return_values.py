# return_values.py — Module 7 Example: Return Values
# ITP 270 — Programming for Cybersecurity
# ============================================================

# --- What is a return value? ---
# A return value is data that a function sends BACK to the code
# that called it. We use the 'return' keyword.

# ============================================================
# EXAMPLE 1: Returning True or False
# ============================================================

def check_password_length(password):
    """Check if a password meets minimum length (8 characters)."""
    if len(password) >= 8:
        return True         # Sends True back to the caller
    else:
        return False        # Sends False back to the caller

# Capture the return value in a variable
result = check_password_length("Cyber2025!")
print(f"'Cyber2025!' meets length? {result}")    # True

result2 = check_password_length("abc")
print(f"'abc' meets length? {result2}")           # False

print()

# ============================================================
# EXAMPLE 2: Returning a number
# ============================================================

def count_digits(text):
    """Count how many digit characters are in a string."""
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count                # Returns an integer

digits = count_digits("P@ss123word456")
print(f"Digits found: {digits}")    # 6

# You can use the return value directly in conditions:
if count_digits("P@ss123") >= 2:
    print("Good — password has enough numbers!")

print()

# ============================================================
# EXAMPLE 3: Returning a string
# ============================================================

def classify_threat(score):
    """Classify a threat level based on a numeric score."""
    if score >= 8:
        return "CRITICAL"
    elif score >= 5:
        return "WARNING"
    elif score >= 3:
        return "LOW"
    else:
        return "NONE"

# Use the returned string
level = classify_threat(7)
print(f"Threat level: {level}")     # WARNING

# Use directly in an f-string
print(f"Score 9 = {classify_threat(9)}")   # CRITICAL
print(f"Score 2 = {classify_threat(2)}")   # NONE

print()

# ============================================================
# EXAMPLE 4: What happens without return?
# ============================================================

def display_status(status):
    """Print a status message (no return statement)."""
    print(f"Status: {status}")
    # No return — this function returns None automatically

result = display_status("Active")
print(f"Return value: {result}")    # None

print()

# ============================================================
# EXAMPLE 5: print() vs. return
# ============================================================

# print() = shows text to the HUMAN on screen
# return  = sends data back to the PROGRAM

def add_with_print(a, b):
    """Prints the sum (but doesn't return it)."""
    print(a + b)        # Shows on screen, but can't be used later

def add_with_return(a, b):
    """Returns the sum (so the program can use it)."""
    return a + b        # Sends data back to the caller

# With print — can't use the result
result1 = add_with_print(5, 3)     # Prints 8
print(f"result1 = {result1}")       # None — useless!

# With return — can use the result
result2 = add_with_return(5, 3)     # Nothing printed
print(f"result2 = {result2}")       # 8 — useful!
total = result2 * 2
print(f"Double: {total}")           # 16
