# ITP 270 — Module 6: IP Address Manager (Complete Example)
# Combines lists, dictionaries, loops, and methods
# =================================================

# --- Setup: Initial data ---
ip_list = ["192.168.1.10", "192.168.1.25", "10.0.0.1"]

ip_details = {
    "192.168.1.10": {"device": "Web Server", "status": "active"},
    "192.168.1.25": {"device": "File Server", "status": "active"},
    "10.0.0.1":     {"device": "Gateway",     "status": "active"}
}

blocklist = ["172.16.0.99", "10.10.10.10"]


# --- Function-like sections (we'll learn functions in Module 7) ---

# 1. Display all IPs
print("=" * 50)
print("         NETWORK IP MANAGER")
print("=" * 50)

print("\n📋 All Network IPs:")
for i, ip in enumerate(ip_list):
    info = ip_details.get(ip, {})
    device = info.get("device", "Unknown")
    status = info.get("status", "unknown")
    print(f"  [{i}] {ip:18s} | {device:15s} | {status}")

print(f"\nTotal IPs: {len(ip_list)}")
print(f"Blocked IPs: {len(blocklist)}")


# 2. Add a new IP
print("\n--- Adding New IP ---")
new_ip = "192.168.1.99"

if new_ip not in ip_list:
    ip_list.append(new_ip)
    ip_details[new_ip] = {"device": "New Workstation", "status": "active"}
    print(f"✅ Added {new_ip}")
else:
    print(f"⚠️  {new_ip} already exists")


# 3. Check if an IP is blocked
print("\n--- Blocklist Check ---")
incoming_ips = ["8.8.8.8", "172.16.0.99", "192.168.1.10"]

for ip in incoming_ips:
    if ip in blocklist:
        print(f"  🚫 {ip} — BLOCKED")
    else:
        print(f"  ✅ {ip} — Allowed")


# 4. Remove an IP
print("\n--- Removing IP ---")
remove_ip = "10.0.0.1"
if remove_ip in ip_list:
    ip_list.remove(remove_ip)
    del ip_details[remove_ip]
    print(f"🗑️  Removed {remove_ip}")
else:
    print(f"  {remove_ip} not found")


# 5. Sort and display final report
print("\n--- Final Network Report ---")
ip_list.sort()
print(f"{'IP Address':18s} | {'Device':15s} | {'Status'}")
print("-" * 50)
for ip in ip_list:
    info = ip_details.get(ip, {})
    device = info.get("device", "Unknown")
    status = info.get("status", "unknown")
    print(f"{ip:18s} | {device:15s} | {status}")

print("-" * 50)
print(f"Active: {sum(1 for ip in ip_details.values() if ip.get('status') == 'active')}")
print(f"Total:  {len(ip_list)}")


# 6. Search for an IP
print("\n--- IP Search ---")
search = "192.168.1.10"
result = ip_details.get(search)
if result:
    print(f"Found: {search}")
    print(f"  Device: {result['device']}")
    print(f"  Status: {result['status']}")
else:
    print(f"{search} not found in network.")
