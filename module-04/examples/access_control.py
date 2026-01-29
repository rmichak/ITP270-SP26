# ============================================================
# access_control.py — Full Access Control System Example
# ITP 270 – Python Programming (Module 4)
# ============================================================
# This example combines everything from Module 4:
#   - Boolean values
#   - Comparison operators
#   - if / elif / else
#   - Logical operators (and, or, not)
#
# Scenario: A simple security system that checks credentials
# and assigns access based on the user's role.
# ============================================================

print("=" * 50)
print("   🔐 SECURE ACCESS CONTROL SYSTEM")
print("=" * 50)

# --- Step 1: Check username and password ---
# In a real system, you'd never hardcode passwords!
# This is just for learning purposes.

# Stored credentials (pretend these are in a database)
stored_username = "analyst01"
stored_password = "Cyber2026!"

# User's input (simulated — in real code, you'd use input())
entered_username = "analyst01"
entered_password = "Cyber2026!"

# Check if BOTH username AND password match
print()
print("Checking credentials...")

if entered_username == stored_username and entered_password == stored_password:
    print("✅ Credentials verified.")
    login_success = True
else:
    print("❌ Invalid username or password.")
    login_success = False

# --- Step 2: Check account status ---
account_locked = False
account_expired = False

print()
print("Checking account status...")

if account_locked:
    print("🔒 Account is LOCKED. Contact your administrator.")
    login_success = False   # Override — can't log in if locked
elif account_expired:
    print("⏰ Account has EXPIRED. Please renew your account.")
    login_success = False   # Override — can't log in if expired
else:
    print("✅ Account is active.")

# --- Step 3: Role-based access (only if login was successful) ---
print()

if login_success:
    print("Login successful! Determining access level...")
    print()

    # User's assigned role
    role = "analyst"

    # Determine access based on role
    if role == "admin":
        print("👑 Role: Administrator")
        print("   Access: FULL SYSTEM ACCESS")
        print("   - View all logs")
        print("   - Modify system settings")
        print("   - Manage user accounts")
        print("   - Run security scans")

    elif role == "analyst":
        print("🔍 Role: Security Analyst")
        print("   Access: READ + ANALYZE")
        print("   - View security logs")
        print("   - Run threat analysis")
        print("   - Generate reports")
        # Analysts cannot modify settings
        print("   ⚠️  Cannot modify system settings")

    elif role == "auditor":
        print("📋 Role: Auditor")
        print("   Access: READ ONLY")
        print("   - View logs and reports")
        print("   - Export data for review")
        # Auditors have very limited access
        print("   ⚠️  Read-only access — no changes allowed")

    elif role == "guest":
        print("👤 Role: Guest")
        print("   Access: LIMITED")
        print("   - View public dashboard only")

    else:
        print("❓ Role: Unknown")
        print("   Access: DENIED — unrecognized role")
        print("   Contact IT support.")

else:
    # Login failed — don't show any access info
    print("⛔ Access denied. Please try again.")
    print("   If you forgot your password, contact IT support.")

# --- Final summary ---
print()
print("=" * 50)
print("   Session ended.")
print("=" * 50)
