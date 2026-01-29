# ============================================================
# ITP 270 — Module 3: Log Parser Example (Cybersecurity)
# ============================================================
# This program demonstrates how to parse and format
# security log entries using string methods.
# This is what real security analysts do every day!
# ============================================================

# --- Raw log entry (a single line from a server log) ---
log = "2025-01-15 08:32:01 ERROR login_failed admin 192.168.1.50"

# --- Step 1: Split the log into parts ---
# .split() breaks the string at every space
parts = log.split()
# parts = ['2025-01-15', '08:32:01', 'ERROR', 'login_failed', 'admin', '192.168.1.50']

# --- Step 2: Extract each piece using indexing ---
date     = parts[0]    # '2025-01-15'
time     = parts[1]    # '08:32:01'
severity = parts[2]    # 'ERROR'
event    = parts[3]    # 'login_failed'
user     = parts[4]    # 'admin'
ip       = parts[5]    # '192.168.1.50'

# --- Step 3: Clean up the event ---
# Replace underscores with spaces, then capitalize each word
clean_event = event.replace("_", " ").title()
# 'login_failed' → 'login failed' → 'Login Failed'

# --- Step 4: Build a formatted alert ---
border = "=" * 50
divider = "-" * 50

alert = f"""
{border}
  ⚠  SECURITY ALERT: {severity}
{border}
  Date:    {date}
  Time:    {time}
  Event:   {clean_event}
  User:    {user}
  Source:  {ip}
{divider}
  Recommended Action: Investigate immediately
{border}
"""

print(alert)

# --- Bonus: Extracting IP from a message ---
print("--- BONUS: IP Extraction ---")
message = "Failed login from IP:192.168.1.105 at port 22"

# Find where "IP:" starts
start = message.find("IP:") + 3    # +3 to skip past "IP:"

# Find the next space after the IP
end = message.find(" ", start)

# Slice out just the IP address
ip_address = message[start:end]
print(f"Extracted IP: {ip_address}")  # 192.168.1.105

# --- Bonus: Password strength check ---
print("\n--- BONUS: Password Check ---")
password = "MyP@ssw0rd"
print(f"Password: {password}")
print(f"Length: {len(password)}")
print(f"Has uppercase: {password != password.lower()}")
print(f"Has lowercase: {password != password.upper()}")
