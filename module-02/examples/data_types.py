# ============================================
# ITP 270 — Module 2: Data Types
# ============================================
# Python has four basic data types:
#   int   — whole numbers (no decimal)
#   float — numbers with a decimal point
#   str   — text (in quotes)
#   bool  — True or False
# ============================================

# --- Integer (int) ---
# Whole numbers: positive, negative, or zero.
# No decimal point.

port_number = 443
login_attempts = 5
temperature = -10
zero_value = 0

print("=== Integers ===")
print("Port number:", port_number)           # Output: 443
print("Login attempts:", login_attempts)     # Output: 5
print("Temperature:", temperature)           # Output: -10
print("Zero:", zero_value)                   # Output: 0

# --- Float (floating-point number) ---
# Numbers WITH a decimal point.
# Even 5.0 is a float — the decimal makes it different.

threat_score = 7.5
cpu_usage = 92.3
file_size_mb = 2.75
five_as_float = 5.0       # This is a float, not an int!

print("\n=== Floats ===")
print("Threat score:", threat_score)         # Output: 7.5
print("CPU usage:", cpu_usage)               # Output: 92.3
print("File size:", file_size_mb, "MB")      # Output: 2.75 MB
print("Five as float:", five_as_float)       # Output: 5.0

# --- String (str) ---
# Text — any characters inside quotation marks.
# Single quotes or double quotes both work.

ip_address = "192.168.1.1"
server_name = 'web-server-01'
greeting = "Welcome to the network!"
port_as_text = "443"       # This is a STRING, not a number!

print("\n=== Strings ===")
print("IP address:", ip_address)             # Output: 192.168.1.1
print("Server:", server_name)                # Output: web-server-01
print("Greeting:", greeting)                 # Output: Welcome to the network!
print("Port (text):", port_as_text)          # Output: 443 (but it's text!)

# --- Boolean (bool) ---
# Only two values: True or False
# Must be capitalized!

firewall_enabled = True
is_admin = False
connection_secure = True

print("\n=== Booleans ===")
print("Firewall enabled:", firewall_enabled)   # Output: True
print("Is admin:", is_admin)                   # Output: False
print("Connection secure:", connection_secure) # Output: True

# --- Important: Numbers in Quotes ---
# 443   → integer (you can do math)
# "443" → string (just text, no math!)

number_port = 443
text_port = "443"

print("\n=== Numbers vs. Strings ===")
print("Number port:", number_port, "| Type:", type(number_port))
print("Text port:", text_port, "| Type:", type(text_port))
# They LOOK the same when printed, but they are different types!
