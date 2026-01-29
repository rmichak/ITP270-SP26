# ============================================================
# ITP 270 — Module 3: Common String Methods
# ============================================================
# This file demonstrates the most important string methods:
# upper(), lower(), strip(), find(), replace(), split(),
# join(), and the len() function.
# ============================================================

# --- Changing Case ---
status = "Warning: Firewall Breach"

print(status.upper())     # WARNING: FIREWALL BREACH
print(status.lower())     # warning: firewall breach
print(status.title())     # Warning: Firewall Breach

# --- strip() — Remove Whitespace ---
# Whitespace = spaces, tabs, newlines
raw_input = "   admin   "
cleaned = raw_input.strip()
print(f"Before: [{raw_input}]")   # Before: [   admin   ]
print(f"After:  [{cleaned}]")     # After:  [admin]

# lstrip() removes only from the left
# rstrip() removes only from the right
print(f"lstrip: [{raw_input.lstrip()}]")  # [admin   ]
print(f"rstrip: [{raw_input.rstrip()}]")  # [   admin]

# --- find() — Search for Text ---
log = "ERROR: Connection refused from 10.0.0.5"

# Returns the index position where the text starts
position = log.find("refused")
print(f"'refused' found at position: {position}")   # 19

# Returns -1 if not found
not_found = log.find("timeout")
print(f"'timeout' found at position: {not_found}")  # -1

# --- replace() — Swap Text ---
fixed = log.replace("ERROR", "WARNING")
print(fixed)   # WARNING: Connection refused from 10.0.0.5

# Replace multiple occurrences
text = "error error error"
print(text.replace("error", "fixed"))  # fixed fixed fixed

# --- split() — Break into a List ---
log_line = "2025-01-15 08:32:01 ERROR login_failed admin"

# Default: split on whitespace
parts = log_line.split()
print(parts)
# ['2025-01-15', '08:32:01', 'ERROR', 'login_failed', 'admin']

# Split on a specific character
date = "2025-01-15"
date_parts = date.split("-")
print(date_parts)    # ['2025', '01', '15']

# Access individual pieces
print(f"Year: {date_parts[0]}")   # Year: 2025
print(f"Month: {date_parts[1]}")  # Month: 01
print(f"Day: {date_parts[2]}")    # Day: 15

# --- join() — Combine a List into a String ---
words = ["ALERT", "firewall", "breach"]

# Join with a space
message = " ".join(words)
print(message)    # ALERT firewall breach

# Join with a comma
csv_line = ",".join(words)
print(csv_line)   # ALERT,firewall,breach

# Join with " | "
formatted = " | ".join(words)
print(formatted)  # ALERT | firewall | breach

# --- len() — Count Characters ---
password = "SecureP@ss123"
length = len(password)
print(f"Password '{password}' has {length} characters")  # 13

# Common use: check password length
if len(password) < 8:
    print("❌ Password too short!")
else:
    print("✅ Password meets minimum length")

# --- Strings are IMMUTABLE ---
# Methods return NEW strings. The original doesn't change!
original = "hello"
result = original.upper()
print(f"Original: {original}")   # hello  (unchanged!)
print(f"Result:   {result}")     # HELLO  (new string)
