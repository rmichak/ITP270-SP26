# ITP 270 — Module 6: List Methods
# append(), insert(), remove(), pop(), sort(), reverse(), len()
# =============================================================

# Start with a list of blocked IPs
blocked_ips = ["192.168.1.100"]
print("Starting list:", blocked_ips)


# --- append() — add to the END ---
print("\n--- append() ---")
blocked_ips.append("10.0.0.5")
print("After append('10.0.0.5'):", blocked_ips)

blocked_ips.append("172.16.0.99")
print("After append('172.16.0.99'):", blocked_ips)


# --- insert() — add at a SPECIFIC position ---
print("\n--- insert() ---")
blocked_ips.insert(0, "172.16.0.1")    # Insert at the beginning
print("After insert(0, '172.16.0.1'):", blocked_ips)

blocked_ips.insert(2, "10.10.10.10")   # Insert at index 2
print("After insert(2, '10.10.10.10'):", blocked_ips)


# --- remove() — remove by VALUE ---
print("\n--- remove() ---")
print("Before remove:", blocked_ips)
blocked_ips.remove("10.10.10.10")      # Removes first match
print("After remove('10.10.10.10'):", blocked_ips)


# --- pop() — remove by INDEX and return the item ---
print("\n--- pop() ---")
print("Before pop:", blocked_ips)
removed = blocked_ips.pop(0)           # Remove first item
print(f"Popped item: {removed}")
print("After pop(0):", blocked_ips)

last = blocked_ips.pop()               # No argument = remove last
print(f"Popped last: {last}")
print("After pop():", blocked_ips)


# --- sort() — arrange in order ---
print("\n--- sort() ---")
ports = [443, 22, 8080, 80, 3306]
print("Before sort:", ports)
ports.sort()
print("After sort:", ports)


# --- reverse() — flip the order ---
print("\n--- reverse() ---")
ports.reverse()
print("After reverse:", ports)


# --- len() — count items ---
print("\n--- len() ---")
print(f"Number of ports: {len(ports)}")
print(f"Number of blocked IPs: {len(blocked_ips)}")
