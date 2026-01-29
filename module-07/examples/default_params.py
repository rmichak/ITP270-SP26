# ============================================================
# default_params.py — Default (Optional) Parameters
# ITP 270 – Python Programming (Module 7)
# ============================================================
# You can give parameters a DEFAULT value.
# If the caller doesn't provide that argument, the default
# is used automatically.
#
# Syntax:
#   def function(param1, param2="default_value"):
#
# Rules:
#   - Parameters WITH defaults must come AFTER those without
#   - The caller can override the default by passing a value
# ============================================================

# --- Basic default parameter ---
def greet(name, greeting="Hello"):
    """Greet a user. Greeting defaults to 'Hello' if not provided."""
    print(f"{greeting}, {name}!")

print("--- Default Parameters ---")
greet("Alice")                  # Uses default: "Hello, Alice!"
greet("Bob", "Welcome")        # Overrides default: "Welcome, Bob!"
greet("Charlie", "Good morning")  # "Good morning, Charlie!"

# --- Security log with defaults ---
print()
print("--- Security Logger ---")

def log_event(message, level="INFO", source="SYSTEM"):
    """Log a security event with optional level and source."""
    print(f"[{level}] ({source}) {message}")

# Call with just the message (uses both defaults)
log_event("System started")
# Output: [INFO] (SYSTEM) System started

# Override just the level
log_event("Failed login attempt", "WARNING")
# Output: [WARNING] (SYSTEM) Failed login attempt

# Override both optional parameters
log_event("Brute force detected", "CRITICAL", "FIREWALL")
# Output: [CRITICAL] (FIREWALL) Brute force detected

# --- Password validator with configurable rules ---
print()
print("--- Password Validator with Defaults ---")

def check_password(password, min_length=8, require_upper=True):
    """
    Check password strength.
    min_length defaults to 8.
    require_upper defaults to True.
    """
    # Check length
    if len(password) < min_length:
        print(f"❌ Too short ({len(password)} chars, need {min_length})")
        return False

    # Check uppercase (only if required)
    if require_upper:
        has_upper = False
        for char in password:
            if char.isupper():
                has_upper = True
        if not has_upper:
            print("❌ Missing uppercase letter")
            return False

    print(f"✅ Password OK")
    return True

# Use all defaults (min 8, require uppercase)
check_password("SecurePass")       # ✅ OK

# Use custom minimum length
check_password("Hi", min_length=4)  # ❌ Too short (2 chars, need 4)

# Disable uppercase requirement
check_password("simple123", require_upper=False)  # ✅ OK

# --- Using keyword arguments ---
# You can specify arguments BY NAME (in any order)
print()
print("--- Keyword Arguments ---")

def create_user(username, role="user", active=True):
    """Create a user account with optional role and status."""
    status = "Active" if active else "Inactive"
    print(f"Created: {username} | Role: {role} | Status: {status}")

# Positional (in order)
create_user("alice", "admin", True)

# Keyword (by name — order doesn't matter)
create_user("bob", active=False, role="analyst")

# Mix of positional and keyword
create_user("charlie", role="auditor")

print()
print("✅ Default parameters complete!")
