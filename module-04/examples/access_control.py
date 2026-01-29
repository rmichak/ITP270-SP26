# ============================================================
# ITP 270 — Module 4: Access Control System
# ============================================================
# This program demonstrates a complete access control system
# combining if/else, elif, and/or, and nested if statements.
# This is the kind of logic used in real cybersecurity systems!
# ============================================================

print("╔══════════════════════════════════╗")
print("║   Secure Access Control System   ║")
print("╚══════════════════════════════════╝")
print()

# --- Step 1: Get user credentials ---
username = input("Username: ")
password = input("Password: ")
role = input("Role: ").lower()

print()
print("Verifying credentials...")
print()

# --- Step 2: Validate credentials ---
# Both username AND password must be correct
if username == "admin" and password == "CyberSec2025!":
    print("✓ Credentials verified.")
    print()

    # --- Step 3: Check role (nested if-elif-else) ---
    if role == "admin":
        print("Access Level: ADMINISTRATOR")
        print("Permissions:")
        print("  - Manage users")
        print("  - Change system settings")
        print("  - View all security logs")
        print("  - Run security scans")
        print("  - Full database access")
    elif role == "analyst":
        print("Access Level: SECURITY ANALYST")
        print("Permissions:")
        print("  - View security logs")
        print("  - Run security scans")
        print("  - Generate reports")
    elif role == "user":
        print("Access Level: STANDARD USER")
        print("Permissions:")
        print("  - View own files")
        print("  - Change own password")
    else:
        print("✗ Role '" + role + "' not recognized.")
        print("Contact IT support to get assigned a valid role.")

elif username == "guest":
    # Guest users don't need a password but have limited access
    print("✓ Guest access granted.")
    print("Access Level: GUEST")
    print("Permissions:")
    print("  - View public information only")
    print("  - No file access")

else:
    print("✗ ACCESS DENIED")
    print("Invalid username or password.")
    print()
    print("If you forgot your credentials:")
    print("  - Contact IT Support at x4567")
    print("  - Visit Room 210 with your employee ID")

print()
print("═══ End of Security Check ═══")
