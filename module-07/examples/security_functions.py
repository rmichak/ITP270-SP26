# security_functions.py — Module 7 Example: Building Modular Security Tools
# ITP 270 — Programming for Cybersecurity
# ============================================================

# This file puts EVERYTHING together:
# - Functions with parameters and return values
# - Default parameters
# - Try-except error handling
# - Functions calling other functions

from datetime import datetime


# ============================================================
# FUNCTION 1: Validate an IPv4 address
# ============================================================

def validate_ip(ip_string):
    """Check if a string is a valid IPv4 address.
    
    Args:
        ip_string: A string like "192.168.1.1"
    
    Returns:
        True if valid IPv4, False otherwise
    """
    parts = ip_string.split(".")
    
    # Must have exactly 4 parts
    if len(parts) != 4:
        return False
    
    # Each part must be a number 0-255
    for part in parts:
        try:
            num = int(part)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
    
    return True


# ============================================================
# FUNCTION 2: Score a password's strength
# ============================================================

def score_password(password):
    """Score a password from 0 to 5 based on security criteria.
    
    Scoring:
        +1 for length >= 8
        +1 for length >= 12
        +1 for uppercase letter
        +1 for lowercase letter
        +1 for digit
    
    Returns:
        Integer score 0-5
    """
    score = 0
    
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    
    # Check for uppercase
    for char in password:
        if char.isupper():
            score += 1
            break
    
    # Check for lowercase
    for char in password:
        if char.islower():
            score += 1
            break
    
    # Check for digit
    for char in password:
        if char.isdigit():
            score += 1
            break
    
    return score


# ============================================================
# FUNCTION 3: Classify a port number
# ============================================================

def classify_port(port_string):
    """Classify a port number into its category.
    
    Args:
        port_string: A string that should contain a port number
    
    Returns:
        String: "well-known", "registered", "dynamic", or "invalid"
    """
    try:
        port = int(port_string)
    except ValueError:
        return "invalid"
    
    if 1 <= port <= 1023:
        return "well-known"
    elif 1024 <= port <= 49151:
        return "registered"
    elif 49152 <= port <= 65535:
        return "dynamic"
    else:
        return "invalid"


# ============================================================
# FUNCTION 4: Log security events (with defaults)
# ============================================================

def log_event(message, level="INFO"):
    """Log a security event with timestamp and severity level.
    
    Args:
        message: Description of the event
        level: Severity level (default: "INFO")
    """
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{level}] {timestamp} — {message}")


# ============================================================
# FUNCTION 5: Generate a security report
# ============================================================

def generate_report(target_ip, password, port):
    """Generate a security assessment report.
    
    Uses validate_ip(), score_password(), classify_port(),
    and log_event() to build a complete assessment.
    
    Args:
        target_ip: IP address string to validate
        password: Password string to score
        port: Port number string to classify
    """
    # Validate IP
    ip_valid = validate_ip(target_ip)
    ip_status = "✅ Valid" if ip_valid else "❌ Invalid"
    
    # Score password
    pw_score = score_password(password)
    strength_labels = {
        0: "Very Weak ❌",
        1: "Weak ❌",
        2: "Fair ⚠️",
        3: "Moderate 👍",
        4: "Strong ✅",
        5: "Very Strong ✅"
    }
    pw_label = strength_labels.get(pw_score, "Unknown")
    
    # Classify port
    port_category = classify_port(port)
    
    # Display report
    print()
    print("=" * 44)
    print("     SECURITY ASSESSMENT REPORT")
    print("=" * 44)
    print(f"  Target IP:     {target_ip} — {ip_status}")
    print(f"  Password:      {'*' * len(password)}")
    print(f"  PW Strength:   {pw_score}/5 — {pw_label}")
    print(f"  Port:          {port} — {port_category}")
    print("=" * 44)
    print()


# ============================================================
# MAIN PROGRAM: Interactive security tool
# ============================================================

def main():
    """Run the interactive security assessment tool."""
    print("=" * 44)
    print("     SECURITY ANALYSIS TOOLKIT v1.0")
    print("     ITP 270 — Cybersecurity Tools")
    print("=" * 44)
    print()
    
    try:
        # Get user inputs
        target = input("Enter target IP address: ")
        password = input("Enter password to evaluate: ")
        port = input("Enter port number to check: ")
        
        # Generate the report (calls our other functions!)
        generate_report(target, password, port)
        
        # Log the event
        log_event("Security assessment completed successfully")
        
    except KeyboardInterrupt:
        print("\n")
        log_event("Assessment cancelled by user", "WARNING")
    except Exception as e:
        log_event(f"Assessment failed: {e}", "ERROR")


# Only run if this file is executed directly (not imported)
if __name__ == "__main__":
    main()
