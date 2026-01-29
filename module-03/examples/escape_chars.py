# ============================================================
# ITP 270 — Module 3: Escape Characters
# ============================================================
# Escape characters let you insert special characters into
# strings that you can't normally type.
# They start with a backslash (\).
# ============================================================

# --- \n — New Line ---
# Creates a line break (like pressing Enter)
print("Line 1\nLine 2\nLine 3")
# Output:
# Line 1
# Line 2
# Line 3

# --- \t — Tab ---
# Creates a tab indent (good for aligning text)
print("User:\tAdmin")
print("Status:\tActive")
print("Role:\tAnalyst")
# Output:
# User:   Admin
# Status: Active
# Role:   Analyst

# --- \\ — Backslash ---
# A single \ starts an escape sequence.
# To print an actual backslash, use two: \\
print("C:\\Users\\admin\\Documents")
# Output: C:\Users\admin\Documents

print("Network path: \\\\server\\share")
# Output: Network path: \\server\share

# --- \" and \' — Quotes Inside Strings ---
# Use \" to put double quotes inside a double-quoted string
print("The server said \"Access Denied\"")
# Output: The server said "Access Denied"

# Use \' to put a single quote inside a single-quoted string
print('It\'s a security alert!')
# Output: It's a security alert!

# --- Practical Example: Formatted Log Entry ---
# Using escape characters to build a structured output
log_entry = "Date:\t2025-01-15\nTime:\t08:32:01\nStatus:\tERROR\nEvent:\tLogin Failed"
print("--- LOG ENTRY ---")
print(log_entry)
print("-" * 20)
# Output:
# --- LOG ENTRY ---
# Date:   2025-01-15
# Time:   08:32:01
# Status: ERROR
# Event:  Login Failed
# --------------------

# --- Tip: Triple quotes vs Escape Characters ---
# For multi-line strings, triple quotes are often easier:
same_output = """Date:\t2025-01-15
Time:\t08:32:01
Status:\tERROR"""
print(same_output)
