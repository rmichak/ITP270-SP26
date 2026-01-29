# ============================================================
# in_class_04.py — In-Class Practice: Decision Control
# ITP 270 – Python Programming (Module 4)
# ============================================================
# Complete each exercise by replacing the TODO comments
# with your own code. Run the file after each exercise
# to test your work!
# ============================================================


# ============================================================
# EXERCISE 1: Simple if Check
# ============================================================
# A server's CPU usage is stored in the variable below.
# If the CPU usage is above 80%, print a warning message.
# ============================================================

cpu_usage = 85  # percentage

# TODO: Write an if statement that prints "WARNING: High CPU usage!"
# if cpu_usage is greater than 80.


print()  # Blank line for readability


# ============================================================
# EXERCISE 2: if-else Access Check
# ============================================================
# A user is trying to log in. Check if the entered password
# matches the correct password.
# Print "Access Granted" if they match.
# Print "Access Denied" if they don't match.
# ============================================================

correct_password = "Python2026"
entered_password = "python2026"  # Notice: different capitalization!

# TODO: Write an if-else that checks if entered_password equals
# correct_password. Print the appropriate message.


print()


# ============================================================
# EXERCISE 3: if-elif-else Grade Checker
# ============================================================
# Given a student's exam score, determine their letter grade:
#   90 and above → "A"
#   80-89        → "B"
#   70-79        → "C"
#   60-69        → "D"
#   Below 60     → "F"
# Print the score and the grade.
# ============================================================

exam_score = 73

# TODO: Write an if-elif-else chain to determine the grade.
# Print something like: "Score: 73 → Grade: C"


print()


# ============================================================
# EXERCISE 4: Logical Operators Practice
# ============================================================
# A system has two security checks: firewall and antivirus.
# Determine the security status:
#   - If BOTH are enabled → print "Fully Protected"
#   - If only ONE is enabled → print "Partially Protected"
#   - If NEITHER is enabled → print "UNPROTECTED!"
#
# Hint: Think about what combinations give each result.
# ============================================================

firewall_enabled = True
antivirus_enabled = False

# TODO: Write if-elif-else using 'and' / 'or' / 'not' to check
# the security status. Print the appropriate message.


print()


# ============================================================
# EXERCISE 5: Simple Access Control System
# ============================================================
# Check if a user should be allowed into the system.
# Requirements:
#   - Username must be "admin" or "analyst"
#   - Password must be "SecurePass1"
#   - Account must NOT be locked
#
# If all requirements are met, print "Welcome, [username]!"
# Otherwise, print "Access Denied" with a reason.
# ============================================================

username = "analyst"
password = "SecurePass1"
is_locked = False

# TODO: Write the access control logic.
# Hint: Use 'and', 'or', and 'not' operators.
# Hint: To check username, use: username == "admin" or username == "analyst"


print()


# ============================================================
# EXERCISE 6: Nested if for Role-Based Decisions
# ============================================================
# FIRST check if the user is logged in.
# IF they are logged in, THEN check their role:
#   - "admin"   → print "Full access: You can modify settings."
#   - "viewer"  → print "Read-only access: You can view reports."
#   - anything else → print "Limited access."
# IF they are NOT logged in:
#   - Print "Please log in first."
#
# This requires an if INSIDE another if (nested).
# ============================================================

is_logged_in = True
user_role = "viewer"

# TODO: Write nested if statements.
# Outer if: check is_logged_in
#   Inner if-elif-else: check user_role
# Outer else: not logged in


print()
print("=" * 40)
print("✅ In-class exercises complete!")
print("=" * 40)
