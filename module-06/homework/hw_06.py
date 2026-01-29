# ITP 270 — Module 6: Homework
# Simple Credential Storage System
# ===================================
# Name: ________________________
# Date: ________________________

# ============================================================
# PROBLEM 1 — Create the User Database (15 points)
# Create a nested dictionary with 3 users
# ============================================================

# TODO: Create a dictionary called 'users' with these entries:
#   "admin"   → password: "Str0ng!Pass",  role: "administrator"
#   "jsmith"  → password: "SecurePass!",  role: "analyst"
#   "guest"   → password: "Guest123",     role: "viewer"
#
# Structure: users = { "username": {"password": "...", "role": "..."}, ... }


# TODO: Print how many users are in the database
# Expected: "User database created with 3 users."



# ============================================================
# PROBLEM 2 — Add a New User (15 points)
# Ask for input, check for duplicates, add to dictionary
# ============================================================

# TODO: Ask for a new username with input()

# TODO: Check if the username already exists using 'in'
#   If exists: print "❌ Username '[name]' already exists!"
#   If new: ask for password and role, add to users dict
#   Print: "✅ User '[name]' added successfully!"



# ============================================================
# PROBLEM 3 — Look Up a User (20 points)
# Use .get() for safe access, mask the password
# ============================================================

# TODO: Ask for a username to look up

# TODO: Use .get() to safely retrieve the user's info

# TODO: If found, display:
#   Username, Role, and Masked Password
#   Mask = first character + asterisks for the rest
#   Example: "Str0ng!Pass" → "S**********"
#   Hint: password[0] + "*" * (len(password) - 1)

# TODO: If not found, print "User '[name]' not found."



# ============================================================
# PROBLEM 4 — List All Users (20 points)
# Loop through dictionary with .items()
# ============================================================

# TODO: Print a header "========== USER DIRECTORY =========="

# TODO: Loop through users.items()
#   For each user, print: "Username: admin       | Role: administrator"

# TODO: Print a footer line and the total number of users



# ============================================================
# PROBLEM 5 — Count Users by Role (15 points)
# Use the counting pattern with .get()
# ============================================================

# TODO: Create an empty dictionary called role_counts

# TODO: Loop through all users and count each role
#   Hint: role_counts[role] = role_counts.get(role, 0) + 1

# TODO: Print each role and its count
#   Example: "administrator: 1"



# ============================================================
# PROBLEM 6 — Delete a User (15 points)
# Safety check: don't allow deleting admin
# ============================================================

# TODO: Ask for a username to delete

# TODO: Check if the username is "admin"
#   If yes: print "🚫 Cannot delete the admin account!"
#   Do NOT delete it.

# TODO: Check if the username exists
#   If yes: delete with 'del' and print confirmation
#   If no: print "User '[name]' not found."

# TODO: Print how many users remain


print("\n🔐 Credential Storage System — Complete!")
