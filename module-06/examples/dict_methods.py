# ITP 270 — Module 6: Dictionary Methods
# get(), keys(), values(), items()
# =================================

credentials = {
    "admin": "P@ssw0rd123",
    "jsmith": "SecurePass!",
    "analyst": "Cyber2024#"
}


# --- get() — safe access (no crash if key is missing) ---
print("--- get() Method ---")

# When the key EXISTS:
result = credentials.get("admin")
print(f"get('admin'): {result}")          # P@ssw0rd123

# When the key DOES NOT exist:
result = credentials.get("hacker")
print(f"get('hacker'): {result}")         # None (no crash!)

# get() with a default value:
result = credentials.get("hacker", "User not found")
print(f"get('hacker', default): {result}")  # User not found

# Compare: regular access CRASHES on missing key
# print(credentials["hacker"])  # ❌ KeyError!


# --- keys() — get all keys ---
print("\n--- keys() Method ---")
print("All usernames:", credentials.keys())

# Convert to a regular list if needed
username_list = list(credentials.keys())
print("As a list:", username_list)


# --- values() — get all values ---
print("\n--- values() Method ---")
print("All passwords:", credentials.values())


# --- items() — get all key-value pairs ---
print("\n--- items() Method ---")
print("All items:", credentials.items())

# Each item is a tuple: (key, value)
for item in credentials.items():
    print(f"  Pair: {item}")
    print(f"    Key: {item[0]}, Value: {item[1]}")


# --- Practical example: safe user lookup ---
print("\n--- Practical: Safe User Lookup ---")
username_to_find = "jsmith"

user_password = credentials.get(username_to_find)
if user_password is not None:
    print(f"Found user '{username_to_find}'")
    # Mask the password for display
    masked = user_password[0] + "*" * (len(user_password) - 1)
    print(f"Password: {masked}")
else:
    print(f"User '{username_to_find}' not found.")
