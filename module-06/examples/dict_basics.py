# ITP 270 — Module 6: Dictionary Basics
# Creating, accessing, adding, updating, and deleting
# ====================================================

# --- Creating a dictionary ---
# Syntax: { key: value, key: value, ... }

credentials = {
    "admin": "P@ssw0rd123",
    "jsmith": "SecurePass!",
    "analyst": "Cyber2024#"
}
print("Credentials:", credentials)

# An empty dictionary
login_attempts = {}
print("Login attempts:", login_attempts)


# --- Accessing values by key ---
print("\n--- Accessing Values ---")
print("admin's password:", credentials["admin"])
print("analyst's password:", credentials["analyst"])

# CAUTION: accessing a key that doesn't exist causes a crash!
# print(credentials["hacker"])  # ❌ KeyError!


# --- Adding new key-value pairs ---
print("\n--- Adding Entries ---")
credentials["newuser"] = "Welcome1!"
print("After adding newuser:", credentials)

credentials["intern"] = "TempPass99"
print("After adding intern:", credentials)


# --- Updating existing values ---
print("\n--- Updating Values ---")
print("Before update — admin:", credentials["admin"])
credentials["admin"] = "NewStr0ng!Pass"
print("After update — admin:", credentials["admin"])


# --- Deleting key-value pairs ---
print("\n--- Deleting Entries ---")
print("Before delete:", credentials)
del credentials["intern"]
print("After deleting intern:", credentials)


# --- Checking if a key exists ---
print("\n--- Checking Keys ---")
username = "admin"
if username in credentials:
    print(f"✅ '{username}' exists in the system")
else:
    print(f"❌ '{username}' not found")

username = "hacker"
if username in credentials:
    print(f"✅ '{username}' exists in the system")
else:
    print(f"❌ '{username}' not found")


# --- Dictionary keys must be unique ---
print("\n--- Unique Keys Demo ---")
# If you use the same key twice, the second value wins
test = {"a": 1, "b": 2, "a": 99}
print("Duplicate key 'a':", test)   # {'a': 99, 'b': 2}
