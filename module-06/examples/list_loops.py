# ITP 270 — Module 6: Looping Through Lists
# for loops, the 'in' keyword, and enumerate()
# =============================================

blocked_ips = ["192.168.1.100", "10.0.0.5", "172.16.0.99"]


# --- Basic for loop ---
print("--- All Blocked IPs ---")
for ip in blocked_ips:
    print(f"  Blocked: {ip}")


# --- Using 'in' to check membership ---
print("\n--- Membership Check ---")
suspect = "10.0.0.5"

if suspect in blocked_ips:
    print(f"⚠️  {suspect} is BLOCKED!")
else:
    print(f"✅ {suspect} is not blocked.")

# Check a safe IP
safe_ip = "8.8.8.8"
if safe_ip in blocked_ips:
    print(f"⚠️  {safe_ip} is BLOCKED!")
else:
    print(f"✅ {safe_ip} is not blocked.")


# --- Searching with a loop and break ---
print("\n--- Search with Loop ---")
search_for = "172.16.0.99"
found = False

for ip in blocked_ips:
    if ip == search_for:
        print(f"Found {search_for} in the blocklist!")
        found = True
        break    # Stop searching once found

if not found:
    print(f"{search_for} was not found.")


# --- enumerate() — loop with index numbers ---
print("\n--- Enumerate ---")
ports = [22, 80, 443, 8080]

for index, port in enumerate(ports):
    print(f"  Port #{index}: {port}")


# --- Building a new list from a loop ---
print("\n--- Filter: Only High Ports ---")
all_ports = [22, 80, 443, 8080, 3306, 25, 8443]
high_ports = []    # Start with empty list

for port in all_ports:
    if port > 1000:
        high_ports.append(port)

print(f"All ports: {all_ports}")
print(f"High ports (>1000): {high_ports}")
