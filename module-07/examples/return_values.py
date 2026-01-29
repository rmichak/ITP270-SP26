# ============================================================
# return_values.py — Functions That Return Values
# ITP 270 – Python Programming (Module 7)
# ============================================================
# So far, our functions only PRINT things.
# But functions can also SEND BACK a value using "return".
#
# Why return instead of print?
#   - You can store the result in a variable
#   - You can use the result in other calculations
#   - You can pass the result to another function
#
# Syntax:
#   def function_name():
#       return value
# ============================================================

# --- Simple return ---
def add(a, b):
    """Add two numbers and return the result."""
    result = a + b
    return result      # Sends the value BACK to the caller

# Store the returned value in a variable
total = add(3, 5)
print("--- Simple Return ---")
print(f"add(3, 5) returned: {total}")    # Output: 8

# You can also use the return value directly
print(f"add(10, 20) = {add(10, 20)}")    # Output: 30

# --- Return vs Print ---
print()
print("--- Return vs Print ---")

# This function PRINTS but returns nothing
def print_sum(a, b):
    """Print the sum (does NOT return it)."""
    print(f"The sum is {a + b}")

# This function RETURNS the sum
def get_sum(a, b):
    """Return the sum (does NOT print it)."""
    return a + b

# See the difference:
result1 = print_sum(3, 5)   # Prints: "The sum is 8"
result2 = get_sum(3, 5)     # Prints nothing — just returns 8

print(f"print_sum returned: {result1}")  # None! (no return statement)
print(f"get_sum returned: {result2}")    # 8 (the actual value)

# --- Return a Boolean ---
print()
print("--- Return a Boolean ---")

def is_strong_password(password):
    """Check if a password is at least 8 characters. Return True/False."""
    if len(password) >= 8:
        return True
    else:
        return False

# Use the returned Boolean in an if statement
password1 = "abc"
password2 = "SecurePass123"

if is_strong_password(password1):
    print(f'"{password1}" — Strong password')
else:
    print(f'"{password1}" — Weak password')     # This prints

if is_strong_password(password2):
    print(f'"{password2}" — Strong password')    # This prints
else:
    print(f'"{password2}" — Weak password')

# --- Return a string ---
print()
print("--- Return a String ---")

def get_threat_level(score):
    """Return the threat level based on a numeric score."""
    if score >= 90:
        return "CRITICAL"
    elif score >= 70:
        return "HIGH"
    elif score >= 40:
        return "MEDIUM"
    else:
        return "LOW"

# Store the result and use it
level = get_threat_level(85)
print(f"Score 85 → Threat Level: {level}")   # HIGH

level = get_threat_level(25)
print(f"Score 25 → Threat Level: {level}")   # LOW

# --- Using return values in calculations ---
print()
print("--- Using Returns in Calculations ---")

def calculate_risk(threats, vulnerabilities):
    """Calculate a simple risk score."""
    return threats * vulnerabilities

risk = calculate_risk(5, 10)
print(f"Risk score: {risk}")            # 50

# You can use the return value directly in expressions
if calculate_risk(8, 12) > 50:
    print("⚠️  High risk! Take action.")   # This prints (96 > 50)

# --- IMPORTANT: return stops the function ---
print()
print("--- Return Stops Execution ---")

def check_age(age):
    """Check if someone is old enough. Return stops the function."""
    if age < 0:
        return "Invalid age"     # Function STOPS here if age < 0
    if age >= 18:
        return "Adult"           # Function STOPS here if age >= 18
    return "Minor"               # Only reached if age is 0-17

print(f"Age -1: {check_age(-1)}")   # Invalid age
print(f"Age 25: {check_age(25)}")   # Adult
print(f"Age 10: {check_age(10)}")   # Minor

print()
print("✅ Return values complete!")
