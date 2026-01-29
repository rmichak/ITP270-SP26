# ============================================================
# ITP 270 — Module 3: Homework
# Log Entry Formatter & String Operations
# ============================================================
# Name:
# Date:
# ============================================================
# Complete all 6 problems. Test each one before moving on.
# Your output must match the expected output exactly.
# ============================================================


# ============================================================
# Problem 1 — Security Badge Creator (15 pts)
# ============================================================
# Given variables (do not change):
first_name = "Alex"
last_name = "Chen"
department = "security operations"
badge_id = "SOC-2847"

# 1. Create full_name by concatenating first_name + " " + last_name
# 2. Create dept_display by converting department to title case
# 3. Create a border of 40 equal signs using *
# 4. Print the badge (see instructions for format)


# YOUR CODE HERE:




# ============================================================
# Problem 2 — Password Analyzer (20 pts)
# ============================================================
# Given variable (do not change):
password = "S3cur!ty2025"

# Print:
# 1. Total length of password
# 2. First character
# 3. Last character
# 4. First 4 characters (slicing)
# 5. Password in all uppercase
# 6. Position of "2025" (use find())


# YOUR CODE HERE:




# ============================================================
# Problem 3 — Log Entry Parser (20 pts)
# ============================================================
# Given variable (do not change):
raw_log = "2025-03-10 22:15:33 CRITICAL unauthorized_access admin 172.16.0.42"

# 1. Split the log into parts
# 2. Store each part: date, time, severity, event, user, ip
# 3. Clean event: replace underscores with spaces, title case
# 4. Print in the format shown in instructions


# YOUR CODE HERE:




# ============================================================
# Problem 4 — Log Entry Formatter (25 pts)
# ============================================================
# Given variables (do not change):
log1 = "2025-03-10 08:15:22 WARNING failed_login jsmith 10.0.0.15"
log2 = "2025-03-10 08:15:45 WARNING failed_login jsmith 10.0.0.15"
log3 = "2025-03-10 08:16:01 ERROR account_locked jsmith 10.0.0.15"

# 1. Parse each log entry
# 2. Build formatted report (see instructions)
# 3. Include header with date from first log
# 4. Show time, severity, event for each entry
# 5. Show affected user and source IP at bottom


# YOUR CODE HERE:




# ============================================================
# Problem 5 — IP Address Extractor (10 pts)
# ============================================================
# Given variable (do not change):
message = "Blocked connection from IP:203.0.113.42 on port 443"

# 1. Use find() to locate "IP:"
# 2. Calculate start position (after "IP:")
# 3. Find the space after the IP
# 4. Slice out the IP address
# 5. Print: "Extracted IP Address: ..."


# YOUR CODE HERE:




# ============================================================
# Problem 6 — Data Sanitizer (10 pts)
# ============================================================
# Given variables (do not change):
raw_name = "   jANe   DOE   "
raw_email = "  Jane.Doe@EXAMPLE.COM  "
raw_role = "security analyst level 2"

# 1. Clean raw_name: strip + title case
# 2. Clean raw_email: strip + lowercase
# 3. Clean raw_role: title case
# 4. Create summary using join(): "name | email | role"
# 5. Print each cleaned value and the summary


# YOUR CODE HERE:


