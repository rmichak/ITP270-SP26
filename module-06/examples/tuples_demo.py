# ITP 270 — Module 6: Tuples
# Immutable (unchangeable) ordered collections
# =============================================

# --- Creating tuples ---
# Tuples use parentheses ( ) instead of square brackets [ ]

server = ("192.168.1.1", 443)
print("Server tuple:", server)

# HTTP status codes — these never change
success_codes = (200, 201, 204)
print("Success codes:", success_codes)

# Single-item tuple needs a trailing comma!
single = ("only_item",)
print("Single tuple:", single)
print("Type:", type(single))

# Without the comma, it's just a string in parentheses
not_a_tuple = ("only_item")
print("Not a tuple:", not_a_tuple)
print("Type:", type(not_a_tuple))


# --- Accessing tuple items ---
print("\n--- Accessing Items ---")
print("IP address:", server[0])    # First item
print("Port:", server[1])          # Second item
print("Last item:", server[-1])    # Last item


# --- Tuple unpacking ---
print("\n--- Tuple Unpacking ---")
ip, port = server    # Assign each item to a variable
print(f"Connecting to {ip} on port {port}")

# Works with any size tuple
code1, code2, code3 = success_codes
print(f"Codes: {code1}, {code2}, {code3}")


# --- Tuples are IMMUTABLE (cannot be changed) ---
print("\n--- Immutability Demo ---")
print("Trying to change server[0]...")
try:
    server[0] = "10.0.0.1"    # This will cause an error!
except TypeError as e:
    print(f"❌ Error: {e}")
    print("Tuples cannot be modified!")


# --- Looping through a tuple ---
print("\n--- Looping Through a Tuple ---")
for code in success_codes:
    print(f"  HTTP {code} = Success")


# --- When to use tuples vs. lists ---
print("\n--- When to Use What ---")
print("Use a LIST  when data changes:  blocked IPs, user list")
print("Use a TUPLE when data is fixed: server address, config values")

# Cybersecurity example: approved protocols (should not change)
approved_protocols = ("HTTPS", "SSH", "SFTP")
print(f"\nApproved protocols: {approved_protocols}")

# Check if a protocol is approved
protocol = "HTTP"
if protocol in approved_protocols:
    print(f"✅ {protocol} is approved")
else:
    print(f"🚫 {protocol} is NOT approved — use HTTPS instead!")
