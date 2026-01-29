# default_params.py — Module 7 Example: Default Parameters
# ITP 270 — Programming for Cybersecurity
# ============================================================

# --- What are default parameters? ---
# A default parameter has a pre-set value. If the caller doesn't
# provide an argument for it, the default is used. If they do
# provide one, their value overrides the default.

# ============================================================
# EXAMPLE 1: One default parameter
# ============================================================

def log_event(message, level="INFO"):
    """Log a security event with an optional severity level."""
    print(f"[{level}] {message}")

# Using the default (level will be "INFO")
log_event("System started")
# Output: [INFO] System started

# Overriding the default
log_event("Brute force detected", "CRITICAL")
# Output: [CRITICAL] Brute force detected

log_event("User logged in")
# Output: [INFO] User logged in

print()

# ============================================================
# EXAMPLE 2: Multiple default parameters
# ============================================================

def scan_port(ip_address, port=80, timeout=5):
    """Simulate scanning a port on a target."""
    print(f"Scanning {ip_address}:{port} (timeout: {timeout}s)")

# All three ways work:
scan_port("192.168.1.1")                # Uses both defaults
scan_port("192.168.1.1", 443)           # Overrides port only
scan_port("192.168.1.1", 443, 10)       # Overrides both

print()

# ============================================================
# EXAMPLE 3: Rule — defaults must come LAST
# ============================================================

# ✅ This is correct:
def create_alert(message, priority="medium", send_email=False):
    """Create a security alert."""
    print(f"Alert ({priority}): {message}")
    if send_email:
        print("  → Email notification sent")

create_alert("Suspicious login")
create_alert("Port scan detected", "high")
create_alert("Server down", "critical", True)

print()

# ❌ This would cause an error (uncomment to see):
# def bad_function(priority="medium", message):
#     print(message)
# SyntaxError: non-default argument follows default argument

# ============================================================
# EXAMPLE 4: Using keyword arguments
# ============================================================

# You can also name arguments explicitly:
def generate_report(title, author="Security Team", format="text"):
    """Generate a security report header."""
    print(f"Report: {title}")
    print(f"Author: {author}")
    print(f"Format: {format}")
    print()

# Using keyword arguments — you can skip middle defaults:
generate_report("Incident Report")
generate_report("Weekly Scan", format="pdf")    # Skip author, change format
generate_report("Audit", author="Alice", format="html")
