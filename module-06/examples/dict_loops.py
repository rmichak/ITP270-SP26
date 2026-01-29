# ITP 270 — Module 6: Looping Through Dictionaries
# Loop through keys, values, and key-value pairs
# ================================================

credentials = {
    "admin": "P@ssw0rd123",
    "jsmith": "SecurePass!",
    "analyst": "Cyber2024#"
}


# --- Loop through KEYS (default behavior) ---
print("--- Loop: Keys Only ---")
for username in credentials:
    print(f"  Username: {username}")


# --- Loop through VALUES only ---
print("\n--- Loop: Values Only ---")
for password in credentials.values():
    print(f"  Password: {password}")


# --- Loop through BOTH keys and values ---
print("\n--- Loop: Keys AND Values ---")
for username, password in credentials.items():
    print(f"  {username} → {password}")


# --- Practical: Formatted user report ---
print("\n" + "=" * 40)
print("        USER DIRECTORY")
print("=" * 40)
for username, password in credentials.items():
    masked = password[0] + "*" * (len(password) - 1)
    print(f"  User: {username:12s} | Password: {masked}")
print("=" * 40)
print(f"  Total users: {len(credentials)}")


# --- Counting pattern: Login attempt tracker ---
print("\n--- Login Attempt Counter ---")
login_attempts = {}

# Simulate login attempts
users_trying = ["admin", "jsmith", "admin", "admin", "analyst", "jsmith"]

for user in users_trying:
    # If user already in dict, add 1. If not, start at 0 + 1
    login_attempts[user] = login_attempts.get(user, 0) + 1

print("Attempt counts:", login_attempts)

# Flag suspicious activity
print("\n--- Security Alerts ---")
for user, count in login_attempts.items():
    if count >= 3:
        print(f"  ⚠️  ALERT: '{user}' has {count} login attempts!")
    else:
        print(f"  ✅ '{user}': {count} attempt(s) — normal")
