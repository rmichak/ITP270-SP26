# ITP 270 — Module 6: List Basics
# Creating, accessing, modifying, and slicing lists
# =================================================

# --- Creating lists ---

# A list of blocked IP addresses (strings)
blocked_ips = ["192.168.1.100", "10.0.0.5", "172.16.0.99"]
print("Blocked IPs:", blocked_ips)

# A list of open port numbers (integers)
open_ports = [22, 80, 443, 8080]
print("Open ports:", open_ports)

# An empty list — we'll add items later
alerts = []
print("Alerts:", alerts)


# --- Accessing items by index ---
# Remember: indexing starts at 0!

print("\n--- Accessing by Index ---")
print("First blocked IP:", blocked_ips[0])    # Index 0 = first item
print("Second blocked IP:", blocked_ips[1])   # Index 1 = second item
print("Third blocked IP:", blocked_ips[2])    # Index 2 = third item

# Negative indexing — count from the end
print("\nLast blocked IP:", blocked_ips[-1])   # -1 = last item
print("Second from last:", blocked_ips[-2])   # -2 = second from last


# --- Modifying items ---
print("\n--- Modifying Items ---")
print("Before:", blocked_ips)
blocked_ips[1] = "10.0.0.50"    # Change the second item
print("After:", blocked_ips)


# --- Slicing ---
# Syntax: list[start:stop]  (includes start, EXCLUDES stop)
ports = [22, 80, 443, 8080, 3306]
print("\n--- Slicing ---")
print("All ports:", ports)
print("ports[1:3]:", ports[1:3])    # Items at index 1 and 2
print("ports[:2]:", ports[:2])       # First two items
print("ports[2:]:", ports[2:])       # From index 2 to end
print("ports[:]:", ports[:])         # Copy of entire list
