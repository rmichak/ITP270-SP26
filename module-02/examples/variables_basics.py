# ============================================
# ITP 270 — Module 2: Variables Basics
# ============================================
# This file demonstrates how to create and
# use variables in Python.
# ============================================

# --- Creating Variables ---
# A variable stores a piece of information.
# Use the = sign to assign a value to a variable.

username = "admin"          # Store text in a variable
print(username)             # Output: admin

# --- Variables Can Hold Different Things ---
server_name = "web-server-01"
port_number = 443
login_attempts = 0

print(server_name)          # Output: web-server-01
print(port_number)          # Output: 443
print(login_attempts)       # Output: 0

# --- Variables Can Change ---
# You can replace the value in a variable at any time.

password_attempts = 0
print(password_attempts)    # Output: 0

password_attempts = 3       # Replace old value with new value
print(password_attempts)    # Output: 3

password_attempts = 5       # Replace again
print(password_attempts)    # Output: 5

# --- Using Variables Together ---
# You can print text and variables together.

device = "Firewall"
location = "Building A"
print("Device:", device)            # Output: Device: Firewall
print("Location:", location)        # Output: Location: Building A

# --- Variable Naming Examples ---
# GOOD variable names (descriptive, follow the rules):
ip_address = "192.168.1.1"
max_attempts = 5
is_active = True

# BAD variable names (avoid these!):
# x = "192.168.1.1"       # What is x? Nobody knows!
# a1 = 5                  # Meaningless name
# 1st_try = True          # ERROR: can't start with a number
# my server = "web-01"    # ERROR: no spaces allowed

print("\n--- Summary ---")
print("IP Address:", ip_address)
print("Max Attempts:", max_attempts)
print("Is Active:", is_active)
