# ============================================================
# ITP 270 — Module 3: In-Class Exercises
# Strings
# ============================================================
# Complete each exercise with your instructor.
# Test your code after each one!
# ============================================================


# ============================================================
# Exercise 1 — Creating Strings
# ============================================================
# 1. Create event_type using double quotes: "Unauthorized Access"
# 2. Create location using single quotes: 'Building B - Room 4'
# 3. Create full_report using triple quotes (3 lines — see instructions)
# 4. Print all three variables


# YOUR CODE HERE:




# ============================================================
# Exercise 2 — Concatenation and F-Strings
# ============================================================
analyst_name = "Jordan"
alert_level = "HIGH"
threat_count = 3

# 1. Using concatenation (+), create greeting: "Hello, Jordan!"
# 2. Using f-string, create alert_msg: "ALERT: Jordan detected 3 HIGH-level threats"
# 3. Using repetition (*), create border: 50 dashes
# 4. Print: border, greeting, alert_msg, border


# YOUR CODE HERE:




# ============================================================
# Exercise 3 — Indexing and Slicing
# ============================================================
protocol = "HTTPS_SECURE_CONNECTION"

# 1. Print the first character (positive indexing)
# 2. Print the last character (negative indexing)
# 3. Slice and print "HTTPS" (first 5 characters)
# 4. Slice and print "SECURE" (index 6 through 11)
# 5. Slice and print "CONNECTION" (index 13 to end)


# YOUR CODE HERE:




# ============================================================
# Exercise 4 — String Methods
# ============================================================
raw_username = "   Admin_User   "
raw_command  = "SHUTDOWN server-01"

# 1. Strip raw_username → store in clean_user, print it
# 2. Convert clean_user to lowercase, print it
# 3. Replace underscore with space in clean_user, print it
# 4. Find position of "server" in raw_command, print it
# 5. Split raw_command into parts, print the list
# 6. Print the length of clean_user


# YOUR CODE HERE:




# ============================================================
# Exercise 5 — Escape Characters
# ============================================================
# 1. Print "--- LOG ENTRY ---", "Date: 2025-01-15", "Status: ERROR"
#    using \n in ONE print statement
#
# 2. Print "User:	admin", "Role:	analyst", "Level:	3"
#    using \t for alignment
#
# 3. Print: C:\Security\Logs\2025\January
#    using \\ for each backslash


# YOUR CODE HERE:




# ============================================================
# Exercise 6 — Putting It All Together: Parse a Log Entry
# ============================================================
log = "2025-01-15 14:22:08 WARNING brute_force_attempt root 10.0.0.99"

# 1. Split the log into parts
# 2. Store each part: date, time, severity, event, user, ip
# 3. Replace underscores in event with spaces
# 4. Convert cleaned event to uppercase
# 5. Print the formatted alert (see instructions for format)


# YOUR CODE HERE:


