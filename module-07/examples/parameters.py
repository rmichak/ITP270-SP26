# parameters.py — Module 7 Example: Parameters and Arguments
# ITP 270 — Programming for Cybersecurity
# ============================================================

# --- Parameters vs. Arguments ---
# Parameter = variable name in the function DEFINITION (placeholder)
# Argument  = actual value you pass when CALLING the function

# ============================================================
# EXAMPLE 1: One parameter
# ============================================================

def greet_user(username):       # 'username' is the PARAMETER
    """Greet a user by name."""
    print(f"Welcome back, {username}!")

greet_user("admin")             # "admin" is the ARGUMENT
greet_user("analyst_jones")     # "analyst_jones" is the ARGUMENT

print()

# ============================================================
# EXAMPLE 2: Two parameters (positional arguments)
# ============================================================

def log_event(event_type, description):
    """Log a security event."""
    print(f"[{event_type}] {description}")

# Order matters! First argument → first parameter
log_event("WARNING", "Failed login attempt detected")
log_event("INFO", "User admin logged in successfully")
log_event("CRITICAL", "Unauthorized access to database")

print()

# ============================================================
# EXAMPLE 3: Three parameters
# ============================================================

def create_user(username, role, department):
    """Display info about a new user account."""
    print(f"Creating user: {username}")
    print(f"  Role: {role}")
    print(f"  Department: {department}")
    print()

create_user("alice", "Analyst", "Security Operations")
create_user("bob", "Admin", "IT Infrastructure")

# ============================================================
# EXAMPLE 4: What happens with wrong number of arguments?
# ============================================================

# Uncomment these to see the errors:
# log_event("WARNING")               # TypeError: missing 1 required argument
# log_event("WARNING", "msg", "x")   # TypeError: takes 2 positional arguments but 3 were given

print("--- Parameter Demo Complete ---")
