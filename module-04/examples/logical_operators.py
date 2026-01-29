# ============================================================
# logical_operators.py — Logical Operators: and, or, not
# ITP 270 – Python Programming (Module 4)
# ============================================================
# Logical operators combine multiple conditions:
#
#   and  → True only if BOTH conditions are True
#   or   → True if AT LEAST ONE condition is True
#   not  → Reverses True to False, or False to True
#
# Think of it like security gates:
#   and = you need BOTH keys to get in
#   or  = you need at least ONE key
#   not = flips the lock status
# ============================================================

# =====================
# AND operator
# =====================
# Both conditions must be True → result is True
print("--- AND Operator ---")
print("True and True:", True and True)     # True — both are True
print("True and False:", True and False)   # False — one is False
print("False and True:", False and True)   # False — one is False
print("False and False:", False and False) # False — both are False

# Security example: Must have valid username AND valid password
print()
username_valid = True
password_valid = True

if username_valid and password_valid:
    print("✅ Login successful — both credentials are correct.")
else:
    print("❌ Login failed — check your username and password.")

# =====================
# OR operator
# =====================
# At least one condition must be True → result is True
print()
print("--- OR Operator ---")
print("True or True:", True or True)       # True
print("True or False:", True or False)     # True — at least one
print("False or True:", False or True)     # True — at least one
print("False or False:", False or False)   # False — neither is True

# Security example: Alert if EITHER firewall or antivirus is disabled
print()
firewall_disabled = False
antivirus_disabled = True

if firewall_disabled or antivirus_disabled:
    print("⚠️  SECURITY ALERT: A protection system is disabled!")
else:
    print("✅ All security systems are active.")

# =====================
# NOT operator
# =====================
# Reverses a Boolean value
print()
print("--- NOT Operator ---")
print("not True:", not True)     # False
print("not False:", not False)   # True

# Security example: Check if user is NOT authorized
print()
is_authorized = False

if not is_authorized:
    print("🚫 Access denied — you are NOT authorized.")
else:
    print("✅ Access granted.")

# =====================
# Combining operators
# =====================
print()
print("--- Combined Example: MFA Login ---")

password_correct = True
mfa_code_correct = True
account_locked = False

# All three conditions must be right:
# password correct AND mfa correct AND account NOT locked
if password_correct and mfa_code_correct and not account_locked:
    print("✅ Multi-factor authentication successful!")
    print("   Welcome to the secure system.")
else:
    print("❌ Authentication failed.")

# =====================
# Practical: Network access check
# =====================
print()
print("--- Network Access Check ---")

is_employee = True
is_on_vpn = False
is_in_office = True

# Access allowed if employee AND (on VPN OR in office)
if is_employee and (is_on_vpn or is_in_office):
    print("✅ Network access granted.")
    print("   Employee verified with valid connection.")
else:
    print("❌ Network access denied.")

# Note: Parentheses ( ) control the order of evaluation,
# just like in math: 2 + 3 * 4 vs (2 + 3) * 4

print()
print("✅ Logical operators complete!")
