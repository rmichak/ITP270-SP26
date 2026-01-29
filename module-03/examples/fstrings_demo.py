# ============================================================
# ITP 270 — Module 3: F-Strings, Concatenation & Repetition
# ============================================================
# This file demonstrates how to combine strings using
# concatenation (+), repetition (*), and f-strings.
# ============================================================

# --- Concatenation with + ---
# Concatenation means joining strings together.
first_name = "Cyber"
last_name = "Analyst"

# Join them with a space in between
full_title = first_name + " " + last_name
print(full_title)  # Output: Cyber Analyst

# --- You CANNOT concatenate a string and a number ---
# age = 25
# message = "Age: " + age    # ❌ This causes a TypeError!
# Fix: convert the number to a string first
age = 25
message = "Age: " + str(age)  # ✅ This works!
print(message)  # Output: Age: 25

# --- Repetition with * ---
# Repeat a string multiple times.
separator = "=" * 40
print(separator)
# Output: ========================================

warning = "⚠ " * 5
print(warning)
# Output: ⚠ ⚠ ⚠ ⚠ ⚠

# --- F-Strings (The Best Way!) ---
# An f-string starts with the letter f before the quote.
# Put variables inside curly braces {} and Python fills them in.
username = "admin"
ip_address = "192.168.1.105"
attempts = 5

alert = f"User {username} from {ip_address} failed {attempts} login attempts"
print(alert)
# Output: User admin from 192.168.1.105 failed 5 login attempts

# --- F-Strings handle numbers automatically ---
# No need for str() — f-strings convert for you!
count = 42
print(f"There are {count} alerts today")
# Output: There are 42 alerts today

# --- F-Strings can contain expressions ---
price = 49.99
print(f"Total with tax: ${price * 1.06:.2f}")
# Output: Total with tax: $52.99

# --- Multi-line F-String ---
# Combine f-strings with triple quotes for formatted output.
analyst = "Jordan"
level = "HIGH"
threats = 7

report = f"""
========================================
  Security Report for {analyst}
========================================
  Threat Level: {level}
  Active Threats: {threats}
  Status: {'CRITICAL' if threats > 5 else 'NORMAL'}
========================================"""

print(report)
