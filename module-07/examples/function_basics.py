# function_basics.py — Module 7 Example: Defining and Calling Functions
# ITP 270 — Programming for Cybersecurity
# ============================================================

# --- What is a function? ---
# A function is a named block of code that performs a specific task.
# You write it once, then call (use) it whenever you need it.

# ============================================================
# EXAMPLE 1: The simplest function (no parameters)
# ============================================================

def greet_analyst():
    """Display a welcome message for a security analyst."""
    print("Welcome, Security Analyst!")
    print("System check complete.")

# Defining a function does NOT run it.
# You must CALL it:
greet_analyst()

print()  # Blank line for spacing

# ============================================================
# EXAMPLE 2: Understanding program flow
# ============================================================

def scan_network():
    """Simulate a network scan."""
    print("  Scanning network...")
    print("  Scan complete!")

print("--- Program Flow Demo ---")
print("Step 1: Before function call")
scan_network()                          # Python jumps into the function
print("Step 2: After function call")    # Then comes back here

print()

# ============================================================
# EXAMPLE 3: Calling a function multiple times
# ============================================================

def alert():
    """Print a security alert."""
    print("⚠️  ALERT: Suspicious activity detected!")

print("--- Calling Three Times ---")
alert()    # First call
alert()    # Second call
alert()    # Third call — no copy-pasting needed!

print()

# ============================================================
# EXAMPLE 4: Functions help organize code
# ============================================================

def show_banner():
    """Display the tool banner."""
    print("=" * 40)
    print("   SECURITY TOOLKIT v1.0")
    print("=" * 40)

def show_menu():
    """Display the menu options."""
    print("1. Scan network")
    print("2. Check logs")
    print("3. Exit")

# Using the functions makes the main program clean and readable:
show_banner()
show_menu()
