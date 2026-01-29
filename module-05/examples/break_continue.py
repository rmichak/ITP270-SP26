"""
ITP 270 — Module 5: break and continue
========================================
break — Stops the ENTIRE loop immediately.
continue — Skips the rest of THIS iteration, moves to the next.
"""

# --- Example 1: break — Find and stop ---
# Search for a specific item and stop when found
print("=== Example 1: break — Find Suspicious IP ===")
ip_list = ["10.0.0.1", "10.0.0.2", "192.168.1.100", "10.0.0.3", "10.0.0.4"]
target = "192.168.1.100"

for ip in ip_list:
    print(f"  Checking {ip}...")
    if ip == target:
        print(f"  🚨 FOUND suspicious IP: {ip}")
        break  # Stop — no need to check the rest

print("  Search ended.\n")

# --- Example 2: continue — Skip unwanted items ---
# Print only non-"INFO" log entries
print("=== Example 2: continue — Skip INFO Entries ===")
logs = ["INFO", "WARNING", "INFO", "ERROR", "INFO", "WARNING"]

for entry in logs:
    if entry == "INFO":
        continue  # Skip this one — go to the next entry
    print(f"  ⚠️ {entry}")  # Only prints WARNING and ERROR

print()

# --- Example 3: break with while loop ---
# Keep asking for input until user types "quit"
print("=== Example 3: break with while ===")
print("Type commands (type 'quit' to stop):")

while True:  # Runs forever UNLESS we break
    command = input("  > ")
    if command == "quit":
        print("  Exiting...")
        break  # This is the ONLY way out of the loop
    print(f"  Running: {command}")

print()

# --- Example 4: continue with numbers ---
# Print only odd numbers from 1 to 10
print("=== Example 4: continue — Odd Numbers Only ===")
for num in range(1, 11):
    if num % 2 == 0:  # If the number is even...
        continue      # ...skip it
    print(f"  {num}", end="  ")
print()
# Output: 1  3  5  7  9

print()

# --- Example 5: Combining break and continue ---
# Scan ports, skip blocked ones, stop on critical
print("=== Example 5: Combined break + continue ===")
ports = [20, 21, 22, 23, 25, 80, 110, 443]
blocked = [25, 110]
critical = [23]  # Telnet — very insecure

for port in ports:
    if port in blocked:
        print(f"  Port {port} — BLOCKED (skipping)")
        continue
    if port in critical:
        print(f"  Port {port} — 🚨 CRITICAL! Stopping scan.")
        break
    print(f"  Port {port} — Scanning...")
