"""
ITP 270 — Module 5: Port Scanner Simulator
============================================
A complete port scanner simulation that uses:
  - for loop with range()
  - Counters and accumulators
  - break and continue
  - Conditional logic

⚠️ EDUCATIONAL ONLY — This does NOT connect to any network.
It simulates the scanning process to demonstrate loop concepts.
"""

# === Configuration ===
# In a real scanner, these would come from actual network probes.
# Here, we just pretend certain ports are open.
open_ports = [21, 22, 53, 80, 443, 3306, 3389, 8080]
blocked_ports = [25, 110, 143]  # Blocked by firewall
critical_ports = [23, 3389, 445]  # Telnet, RDP, SMB — dangerous if open

# Known service names (for display)
service_names = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt"
}

# === Counters and accumulators ===
found_count = 0       # How many open ports we found
blocked_count = 0     # How many we skipped
total_risk = 0        # Accumulated risk score
critical_alert = False

# === Get scan range from user ===
print("=" * 45)
print("   🔍 Port Scanner Simulator v1.0")
print("   ITP 270 — Educational Use Only")
print("=" * 45)
print()

start = int(input("Start port (e.g., 1): "))
end = int(input("End port (e.g., 1024): "))
print()

# Validate input
if start < 1 or end > 65535 or start > end:
    print("❌ Invalid port range. Ports must be 1-65535.")
    print("   Start must be less than or equal to end.")
    exit()

print(f"Scanning ports {start} to {end}...")
print("-" * 45)

# === Main scan loop ===
for port in range(start, end + 1):

    # Skip blocked ports
    if port in blocked_ports:
        blocked_count += 1
        continue  # Move to next port — don't scan this one

    # Check if port is "open"
    if port in open_ports:
        found_count += 1

        # Get service name (or "Unknown")
        service = service_names.get(port, "Unknown")

        # Assess risk level
        if port in critical_ports:
            risk = 10
            label = "🔴 CRITICAL"
        elif port in [21, 22, 3306, 8080]:
            risk = 5
            label = "🟡 MEDIUM"
        else:
            risk = 2
            label = "🟢 LOW"

        total_risk += risk  # Accumulate risk

        # Display result
        print(f"  Port {port:>5}  ({service:<10})  {label}  Risk: {risk} pts")

        # Stop on critical vulnerability
        if port in critical_ports:
            print()
            print("  🚨 CRITICAL VULNERABILITY DETECTED!")
            print("  Stopping scan — immediate remediation required.")
            critical_alert = True
            break

# === Results ===
print("-" * 45)
print()
print("📊 SCAN RESULTS")
print(f"  Ports scanned:    {start} — {end}")
print(f"  Open ports found: {found_count}")
print(f"  Blocked (skipped):{blocked_count}")
print(f"  Total risk score: {total_risk}")
print()

if critical_alert:
    print("⚠️  STATUS: CRITICAL — Scan was halted!")
    print("   Action: Close critical port immediately.")
elif total_risk > 20:
    print("⚠️  STATUS: HIGH RISK — Review open ports.")
elif total_risk > 10:
    print("🟡 STATUS: MODERATE — Some ports need attention.")
else:
    print("✅ STATUS: LOW RISK — Network looks good.")

print()
print("=" * 45)
print("   Scan complete.")
print("=" * 45)
