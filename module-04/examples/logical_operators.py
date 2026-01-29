# ============================================================
# ITP 270 — Module 4: Logical Operators (and, or, not)
# ============================================================
# Logical operators combine multiple conditions:
#   and — BOTH must be True
#   or  — at least ONE must be True
#   not — reverses True to False (and vice versa)
# ============================================================

# --- The AND Operator ---
print("=== AND Operator ===")
print("Both conditions must be True:")
print("True and True:", True and True)     # True
print("True and False:", True and False)   # False
print("False and True:", False and True)   # False
print("False and False:", False and False) # False
print()

# Practical example: login requires both username AND password
print("--- Login Check (and) ---")
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "secure123":
    print("✓ Login successful!")
else:
    print("✗ Invalid credentials.")
print()

# --- The OR Operator ---
print("=== OR Operator ===")
print("At least ONE condition must be True:")
print("True or True:", True or True)       # True
print("True or False:", True or False)     # True
print("False or True:", False or True)     # True
print("False or False:", False or False)   # False
print()

# Practical example: user can log in with username OR email
print("--- Login with Username OR Email ---")
login = input("Enter username or email: ")

if login == "alice" or login == "alice@nova.edu":
    print("Welcome, Alice!")
else:
    print("User not found.")
print()

# --- The NOT Operator ---
print("=== NOT Operator ===")
print("Reverses the value:")
print("not True:", not True)     # False
print("not False:", not False)   # True
print()

# Practical example: check if user is NOT banned
is_banned = False

if not is_banned:
    print("You may access the system.")
else:
    print("Your account has been banned.")
print()

# --- Combining Operators ---
print("=== Combining Operators ===")
role = "analyst"
clearance = 3
is_active = True

# Use parentheses to group conditions clearly
if (role == "admin" or role == "analyst") and clearance >= 3 and is_active:
    print("Access to security dashboard granted.")
else:
    print("Access denied.")

# --- KEY POINTS ---
# 1. and = BOTH True → True (think: two keys for a vault)
# 2. or = at least ONE True → True (think: two entrances)
# 3. not = reverses the value (think: opposite day)
# 4. Use parentheses () to make complex conditions clear
# 5. Priority: not → and → or (but use parentheses anyway!)
