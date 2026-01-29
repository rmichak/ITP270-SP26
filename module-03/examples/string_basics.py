# ============================================================
# ITP 270 — Module 3: String Basics
# ============================================================
# This file demonstrates how to create strings in Python
# using single quotes, double quotes, and triple quotes.
# ============================================================

# --- Single Quotes ---
# Wrap text in single quotes to create a string.
greeting = 'Hello, analyst!'
print(greeting)  # Output: Hello, analyst!

# --- Double Quotes ---
# Double quotes work exactly the same way.
greeting = "Hello, analyst!"
print(greeting)  # Output: Hello, analyst!

# --- When to use which? ---
# Use double quotes when your text has an apostrophe
message = "It's a security alert!"
print(message)  # Output: It's a security alert!

# Use single quotes when your text has double quotes
command = 'The user typed "exit" to log out'
print(command)  # Output: The user typed "exit" to log out

# --- Triple Quotes (Multi-Line Strings) ---
# Triple quotes let you write strings on multiple lines.
# Everything between the triple quotes is part of the string.
alert = """SECURITY ALERT
Location: Server Room B
Status: Unauthorized access detected
Time: 14:32 UTC"""

print(alert)
# Output:
# SECURITY ALERT
# Location: Server Room B
# Status: Unauthorized access detected
# Time: 14:32 UTC

# --- Checking the Type ---
# You can verify that something is a string using type()
name = "Cyber Analyst"
print(type(name))  # Output: <class 'str'>

# --- Empty String ---
# A string with nothing in it is called an empty string.
empty = ""
print(len(empty))  # Output: 0
