# ============================================
# ITP 270 — Module 2: Cybersecurity Variables
# ============================================
# Real-world examples of using variables and
# data types in cybersecurity scenarios.
# ============================================

# ============================================
# SCENARIO 1: Network Device Inventory
# ============================================
print("=== Network Device Inventory ===")

# Device information using all four data types
device_name = "Cisco-ASA-5505"          # str  — device name is text
device_ip = "10.0.0.1"                  # str  — IP addresses are text
num_interfaces = 8                      # int  — count of interfaces
firmware_version = 9.16                 # float — version number
is_managed = True                       # bool — management status

print("Device:", device_name)
print("IP:", device_ip)
print("Interfaces:", num_interfaces)
print("Firmware:", firmware_version)
print("Managed:", is_managed)

# ============================================
# SCENARIO 2: Login Monitoring
# ============================================
print("\n=== Login Monitoring ===")

username = "jsmith"
max_login_attempts = 5
failed_attempts = 3
remaining_attempts = max_login_attempts - failed_attempts
account_locked = False

print("User:", username)
print("Failed attempts:", failed_attempts, "of", max_login_attempts)
print("Remaining:", remaining_attempts)
print("Account locked:", account_locked)

# ============================================
# SCENARIO 3: Password Strength Analysis
# ============================================
print("\n=== Password Strength Analysis ===")

# Calculate password strength based on character set
lowercase_chars = 26       # a-z
uppercase_chars = 26       # A-Z
digit_chars = 10           # 0-9
special_chars = 33         # !@#$%^&*... etc.

# Simple password: just lowercase, 6 characters
simple_length = 6
simple_charset = lowercase_chars
simple_combinations = simple_charset ** simple_length
print("Simple password (6 lowercase):", simple_combinations, "combinations")

# Strong password: all character types, 12 characters
strong_length = 12
strong_charset = lowercase_chars + uppercase_chars + digit_chars + special_chars
strong_combinations = strong_charset ** strong_length
print("Strong password (12 mixed):", strong_combinations, "combinations")

print("Strong passwords are MUCH harder to crack!")

# ============================================
# SCENARIO 4: Network Port Categories
# ============================================
print("\n=== Network Port Categories ===")

total_ports = 2 ** 16                   # 65536 total ports
well_known = 1024                       # Ports 0-1023
registered = 49152 - 1024              # Ports 1024-49151
dynamic = total_ports - 49152          # Ports 49152-65535

print("Total ports:", total_ports)
print("Well-known ports (0-1023):", well_known)
print("Registered ports (1024-49151):", registered)
print("Dynamic/Private ports (49152-65535):", dynamic)

# Common ports every cybersecurity pro should know
http_port = 80
https_port = 443
ssh_port = 22
dns_port = 53
ftp_port = 21

print("\nCommon Ports:")
print("HTTP:", http_port)
print("HTTPS:", https_port)
print("SSH:", ssh_port)
print("DNS:", dns_port)
print("FTP:", ftp_port)

# ============================================
# SCENARIO 5: Incident Response Data
# ============================================
print("\n=== Incident Response Report ===")

incident_id = "INC-2026-0042"           # str  — incident identifier
source_ip = "203.0.113.50"              # str  — attacker IP
target_ip = "192.168.1.100"             # str  — victim IP
attack_port = 22                         # int  — targeted port
severity_score = 8.5                     # float — CVSS-like score
incident_resolved = False                # bool — resolution status

print("Incident ID:", incident_id)
print("Source IP:", source_ip)
print("Target IP:", target_ip)
print("Attack Port:", attack_port)
print("Severity:", severity_score, "/ 10")
print("Resolved:", incident_resolved)
