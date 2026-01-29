# ============================================================
# parameters.py — Function Parameters (Arguments)
# ITP 270 – Python Programming (Module 7)
# ============================================================
# Parameters let you pass DATA into a function.
# This makes functions flexible — they can work with
# different values each time you call them.
#
# Vocabulary:
#   Parameter = the variable name in the function definition
#   Argument  = the actual value you pass when calling
#
# Example:
#   def greet(name):     ← "name" is the PARAMETER
#   greet("Alice")       ← "Alice" is the ARGUMENT
# ============================================================

# --- One parameter ---
def greet(name):
    """Greet a user by name."""
    print(f"Hello, {name}! Welcome to the system.")

# Call with different arguments each time
print("--- Single Parameter ---")
greet("Alice")        # name = "Alice"
greet("Bob")          # name = "Bob"
greet("Analyst01")    # name = "Analyst01"

# --- Two parameters ---
print()
print("--- Two Parameters ---")

def check_access(username, role):
    """Display a user's role and access information."""
    print(f"User: {username}")
    print(f"Role: {role}")
    print()

# Arguments match parameters in ORDER (positional arguments)
check_access("alice", "admin")       # username="alice", role="admin"
check_access("bob", "analyst")       # username="bob", role="analyst"

# --- Three parameters ---
print("--- Three Parameters ---")

def log_event(timestamp, event_type, message):
    """Display a formatted log entry."""
    print(f"[{timestamp}] {event_type}: {message}")

log_event("2026-01-15 09:00", "INFO", "System started")
log_event("2026-01-15 09:05", "WARNING", "High CPU usage detected")
log_event("2026-01-15 09:10", "ERROR", "Failed login attempt")

# --- Parameters are like variables inside the function ---
print()
print("--- How Parameters Work ---")

def double(number):
    """Print a number doubled."""
    result = number * 2    # "number" holds whatever value was passed in
    print(f"{number} doubled is {result}")

double(5)     # number = 5, result = 10
double(12)    # number = 12, result = 24
double(100)   # number = 100, result = 200

# --- Practical: Password length checker ---
print()
print("--- Password Length Checker ---")

def check_password_length(password, min_length):
    """Check if a password meets the minimum length requirement."""
    actual_length = len(password)
    if actual_length >= min_length:
        print(f"✅ Password OK ({actual_length} chars, need {min_length})")
    else:
        print(f"❌ Too short ({actual_length} chars, need {min_length})")

check_password_length("abc", 8)           # Too short
check_password_length("MyPassword1", 8)   # OK
check_password_length("Hi", 4)            # Too short

print()
print("✅ Parameters complete!")
