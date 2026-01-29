"""
ITP 270 — Module 5: Counters and Accumulators
===============================================
Counter: Counts HOW MANY times something happens (adds 1 each time).
Accumulator: Adds up a TOTAL (adds varying amounts each time).

Both follow the same 3-step pattern:
  1. INITIALIZE before the loop (set to 0)
  2. UPDATE inside the loop
  3. USE after the loop
"""

# --- Example 1: Counter — Count uppercase letters ---
print("=== Example 1: Counter ===")
password = "MyP@ssW0rd!"
upper_count = 0  # Step 1: Initialize BEFORE the loop

for char in password:
    if char.isupper():
        upper_count += 1  # Step 2: Update INSIDE the loop

# Step 3: Use AFTER the loop
print(f"Password: {password}")
print(f"Uppercase letters: {upper_count}")
print()

# --- Example 2: Accumulator — Add up file sizes ---
print("=== Example 2: Accumulator ===")
file_sizes_mb = [2.5, 10.0, 0.3, 45.2, 8.1, 1.9]
total = 0  # Step 1: Initialize

for size in file_sizes_mb:
    total += size  # Step 2: Add each size to the total

# Step 3: Use the total
print(f"File sizes: {file_sizes_mb}")
print(f"Total: {total} MB")
print(f"Average: {total / len(file_sizes_mb):.1f} MB")
print()

# --- Example 3: Counter + Accumulator together ---
print("=== Example 3: Both Together ===")
login_attempts = [
    {"user": "admin", "result": "FAIL"},
    {"user": "admin", "result": "FAIL"},
    {"user": "jsmith", "result": "SUCCESS"},
    {"user": "admin", "result": "FAIL"},
    {"user": "root", "result": "FAIL"},
    {"user": "jsmith", "result": "SUCCESS"},
]

fail_count = 0     # Counter
success_count = 0  # Counter

for attempt in login_attempts:
    if attempt["result"] == "FAIL":
        fail_count += 1
    else:
        success_count += 1

total = fail_count + success_count
print(f"Total attempts: {total}")
print(f"Successful: {success_count}")
print(f"Failed: {fail_count}")
print(f"Failure rate: {fail_count / total * 100:.0f}%")
print()

# --- Example 4: Common mistake — initializing INSIDE the loop ---
print("=== Example 4: Common Bug ===")
print("WRONG way (counter resets every loop):")
numbers = [10, 20, 30]
for n in numbers:
    total_wrong = 0  # BUG: resets to 0 every time!
    total_wrong += n
    print(f"  Adding {n}, total = {total_wrong}")
print(f"  Final total: {total_wrong} (should be 60, but got {total_wrong})")

print()
print("RIGHT way (counter before the loop):")
total_right = 0  # CORRECT: initialize BEFORE
for n in numbers:
    total_right += n
    print(f"  Adding {n}, total = {total_right}")
print(f"  Final total: {total_right} ✅")
