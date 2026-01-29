# scope_demo.py — Module 7 Example: Variable Scope
# ITP 270 — Programming for Cybersecurity
# ============================================================

# --- What is scope? ---
# Scope means "where a variable exists and can be used."
# LOCAL = inside a function (only visible there)
# GLOBAL = outside all functions (visible everywhere)

# ============================================================
# EXAMPLE 1: Local variables
# ============================================================

def analyze_log():
    """Analyze a log file (demonstrates local variable)."""
    threat_count = 5    # LOCAL variable — only exists in this function
    print(f"Threats found: {threat_count}")

analyze_log()

# Uncomment this line to see the error:
# print(threat_count)
# NameError: name 'threat_count' is not defined
# threat_count doesn't exist outside the function!

print()

# ============================================================
# EXAMPLE 2: Global variables
# ============================================================

alert_level = "GREEN"       # GLOBAL variable — exists outside all functions

def show_status():
    """Display the current alert level."""
    # Functions CAN READ global variables
    print(f"Current alert level: {alert_level}")

show_status()       # Output: Current alert level: GREEN
print(f"Main program: {alert_level}")   # Also works here

print()

# ============================================================
# EXAMPLE 3: Local and global with the same name
# ============================================================

status = "SAFE"             # Global variable

def check_system():
    """Check system status (has a local 'status' variable)."""
    status = "COMPROMISED"  # This is a NEW LOCAL variable, not the global one!
    print(f"Inside function: {status}")     # COMPROMISED

check_system()
print(f"Outside function: {status}")        # SAFE — global is unchanged!

print()

# ============================================================
# EXAMPLE 4: Best practice — use parameters instead of globals
# ============================================================

# ❌ Not great — relies on a global variable
total_scans = 0

def bad_scan():
    """This function tries to use a global — can cause confusion."""
    # Can't modify global without 'global' keyword
    # total_scans += 1  # This would cause an error!
    print(f"Total scans: {total_scans}")

# ✅ Better — pass data as parameters, return results
def good_scan(scan_count):
    """Takes data in, sends data out — clean and predictable."""
    scan_count += 1
    print(f"Scan #{scan_count} complete")
    return scan_count

count = 0
count = good_scan(count)    # Scan #1 complete
count = good_scan(count)    # Scan #2 complete
count = good_scan(count)    # Scan #3 complete
print(f"Total scans: {count}")  # 3

print()
print("--- Scope Demo Complete ---")
print("Remember: Pass data as parameters, not global variables!")
