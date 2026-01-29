# ============================================================
# ITP 270 — Module 3: String Indexing & Slicing
# ============================================================
# This file demonstrates how to access individual characters
# (indexing) and portions of a string (slicing).
# ============================================================

# --- Indexing ---
# Every character has a position number (index).
# Python starts counting at 0!

protocol = "HTTPS"

# Positive indexing (left to right, starting at 0)
print(protocol[0])    # H  — first character
print(protocol[1])    # T  — second character
print(protocol[2])    # T  — third character
print(protocol[3])    # P  — fourth character
print(protocol[4])    # S  — fifth character (last)

# Negative indexing (right to left, starting at -1)
print(protocol[-1])   # S  — last character
print(protocol[-2])   # P  — second from last
print(protocol[-5])   # H  — first character (same as [0])

# --- Index positions visualized ---
#   H   T   T   P   S
#   0   1   2   3   4     ← positive index
#  -5  -4  -3  -2  -1     ← negative index

# --- Slicing ---
# Extract a portion of a string: string[start:stop]
# The stop index is NOT included!

log_entry = "ERROR:login_failed:admin"

# Get characters from index 0 up to (not including) 5
status = log_entry[0:5]
print(status)    # ERROR

# Shortcut: leave out the 0 to start from the beginning
status = log_entry[:5]
print(status)    # ERROR

# From index 6 to the end (leave out the stop)
details = log_entry[6:]
print(details)   # login_failed:admin

# From index 6 to index 18
action = log_entry[6:18]
print(action)    # login_failed

# --- Negative slicing ---
# Get the last 5 characters
ending = log_entry[-5:]
print(ending)    # admin

# --- Copy the entire string ---
full_copy = log_entry[:]
print(full_copy)  # ERROR:login_failed:admin

# --- Practical Example ---
# Extract parts of a timestamp
timestamp = "2025-01-15 08:32:01"
date = timestamp[:10]       # "2025-01-15"
time = timestamp[11:]       # "08:32:01"
year = timestamp[:4]        # "2025"
month = timestamp[5:7]      # "01"
day = timestamp[8:10]       # "15"

print(f"Date: {date}")
print(f"Time: {time}")
print(f"Year: {year}, Month: {month}, Day: {day}")
