# ============================================================
# if_else.py — The if-else Statement
# ITP 270 – Python Programming (Module 4)
# ============================================================
# if-else gives your program TWO paths:
#   - If the condition is True  → run the if block
#   - If the condition is False → run the else block
#
# Syntax:
#   if condition:
#       code when True
#   else:
#       code when False
#
# ONE of these blocks will ALWAYS run — never both, never neither.
# ============================================================

# --- Basic if-else ---
age = 20

if age >= 18:
    print("You are an adult.")     # This runs because 20 >= 18
else:
    print("You are a minor.")      # This is skipped

# --- Cybersecurity: Access Granted / Denied ---
print()
print("--- Access Control Example ---")

# Simulate a user entering a password
entered_password = "Secure123"
correct_password = "Secure123"

# Check if the password matches
if entered_password == correct_password:
    print("✅ ACCESS GRANTED")
    print("Welcome to the system!")
else:
    print("❌ ACCESS DENIED")
    print("Incorrect password. Please try again.")

# --- Login Attempts Check ---
print()
print("--- Login Attempts Example ---")

max_attempts = 5
current_attempts = 6

if current_attempts <= max_attempts:
    print("Login allowed. Please enter your credentials.")
else:
    print("🔒 Account locked!")
    print(f"You exceeded the maximum of {max_attempts} attempts.")

# --- Network Port Check ---
print()
print("--- Port Check Example ---")

port = 443

if port == 443:
    print("Port 443: HTTPS (secure web traffic)")
else:
    print(f"Port {port}: Not the standard HTTPS port")

# --- Even or Odd ---
print()
print("--- Even / Odd Check ---")

number = 7

# The % operator gives the remainder of division
# If a number divided by 2 has remainder 0, it's even
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")    # This prints because 7 % 2 = 1

# --- Firewall Rule ---
print()
print("--- Firewall Rule Example ---")

ip_address = "192.168.1.100"
allowed_network = "192.168.1."

# Check if the IP starts with the allowed network prefix
if ip_address.startswith(allowed_network):
    print(f"✅ {ip_address} — ALLOWED (internal network)")
else:
    print(f"❌ {ip_address} — BLOCKED (external network)")

print()
print("✅ if-else examples complete!")
