# ============================================================
# security_functions.py — Cybersecurity Utility Functions
# ITP 270 – Python Programming (Module 7)
# ============================================================
# Real-world example: Functions a security analyst might use.
# Combines everything from Module 7:
#   - Functions with parameters and return values
#   - Default parameters
#   - Error handling with try-except
# ============================================================


# --- Function 1: Password Validator ---
def validate_password(password, min_length=8):
    """
    Check if a password meets security requirements.

    Requirements:
        - At least min_length characters (default 8)
        - At least one uppercase letter
        - At least one digit

    Parameters:
        password (str): The password to check
        min_length (int): Minimum required length (default 8)

    Returns:
        bool: True if password is valid, False otherwise
    """
    # Check if password is a string
    if not isinstance(password, str):
        print("  ❌ Error: Password must be a string.")
        return False

    # Check length
    if len(password) < min_length:
        print(f"  ❌ Too short: {len(password)} chars (need {min_length})")
        return False

    # Check for uppercase letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break               # Found one — no need to keep checking

    if not has_upper:
        print("  ❌ Missing uppercase letter.")
        return False

    # Check for digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break

    if not has_digit:
        print("  ❌ Missing digit.")
        return False

    # All checks passed!
    print("  ✅ Password meets all requirements.")
    return True


# --- Function 2: IP Address Format Checker ---
def check_ip_format(ip_address):
    """
    Check if a string looks like a valid IPv4 address.

    A valid IPv4 address has:
        - Exactly 4 parts separated by dots
        - Each part is a number between 0 and 255

    Parameters:
        ip_address (str): The IP address string to check

    Returns:
        bool: True if format is valid, False otherwise
    """
    try:
        # Split the IP address by dots
        parts = ip_address.split(".")

        # Must have exactly 4 parts
        if len(parts) != 4:
            print(f"  ❌ Invalid: Expected 4 octets, got {len(parts)}")
            return False

        # Each part must be a number between 0 and 255
        for part in parts:
            number = int(part)        # Convert to number (may raise ValueError)
            if number < 0 or number > 255:
                print(f"  ❌ Invalid: {number} is not between 0-255")
                return False

        print(f"  ✅ '{ip_address}' is a valid IPv4 format.")
        return True

    except ValueError:
        # int() failed — a part was not a number
        print(f"  ❌ Invalid: '{ip_address}' contains non-numeric parts.")
        return False


# --- Function 3: Security Report Generator ---
def generate_report(title, findings, severity="MEDIUM"):
    """
    Generate a simple security report.

    Parameters:
        title (str): Report title
        findings (list): List of finding strings
        severity (str): Overall severity (default "MEDIUM")

    Returns:
        str: The formatted report as a string
    """
    try:
        # Build the report string
        report = ""
        report += "=" * 50 + "\n"
        report += f"  SECURITY REPORT: {title}\n"
        report += f"  Severity: {severity}\n"
        report += "=" * 50 + "\n"

        if len(findings) == 0:
            report += "  No findings to report.\n"
        else:
            report += f"\n  Findings ({len(findings)} total):\n"
            report += "-" * 50 + "\n"

            for i, finding in enumerate(findings, start=1):
                report += f"  {i}. {finding}\n"

        report += "\n" + "=" * 50
        return report

    except Exception as e:
        return f"❌ Error generating report: {e}"


# ============================================================
# DEMO: Let's test all three functions!
# ============================================================

print("=" * 50)
print("  🔐 SECURITY FUNCTIONS DEMO")
print("=" * 50)

# --- Test validate_password ---
print()
print("--- Password Validation ---")

passwords = ["abc", "longpassword", "LongPassword", "Secure123"]
for pwd in passwords:
    print(f'\nChecking: "{pwd}"')
    result = validate_password(pwd)
    print(f"  Result: {'PASS' if result else 'FAIL'}")

# --- Test check_ip_format ---
print()
print("--- IP Address Validation ---")

ips = ["192.168.1.1", "10.0.0.256", "abc.def.ghi.jkl", "172.16.0.1"]
for ip in ips:
    print(f'\nChecking: "{ip}"')
    result = check_ip_format(ip)

# --- Test generate_report ---
print()
print("--- Security Report ---")

findings_list = [
    "Open port 22 (SSH) detected on server",
    "Outdated SSL certificate on web server",
    "3 failed login attempts from IP 10.0.0.5"
]

report = generate_report("Weekly Scan", findings_list, severity="HIGH")
print(report)

# --- Empty report ---
print()
empty_report = generate_report("Monthly Audit", [])
print(empty_report)

print()
print("✅ Security functions demo complete!")
