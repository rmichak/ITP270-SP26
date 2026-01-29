# ============================================================
# if_elif_else.py — The if-elif-else Statement
# ITP 270 – Python Programming (Module 4)
# ============================================================
# When you have MORE than two possible outcomes, use elif.
# "elif" is short for "else if".
#
# Syntax:
#   if condition1:
#       code for condition1
#   elif condition2:
#       code for condition2
#   elif condition3:
#       code for condition3
#   else:
#       code if NONE of the above are True
#
# Python checks conditions from TOP to BOTTOM.
# It runs the FIRST one that is True, then skips the rest.
# ============================================================

# --- Threat Level Assessment ---
print("--- Threat Level Assessment ---")

threat_score = 75  # Scale of 0-100

if threat_score >= 90:
    print("🔴 CRITICAL — Immediate action required!")
    print("   Isolate affected systems NOW.")
elif threat_score >= 70:
    print("🟠 HIGH — Serious threat detected.")         # This runs (75 >= 70)
    print("   Investigate within 1 hour.")
elif threat_score >= 40:
    print("🟡 MEDIUM — Potential threat found.")
    print("   Schedule investigation within 24 hours.")
elif threat_score >= 10:
    print("🟢 LOW — Minor concern.")
    print("   Log for weekly review.")
else:
    print("⚪ NONE — No threat detected.")
    print("   System is operating normally.")

# --- Grade Checker ---
print()
print("--- Grade Checker ---")

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"    # This runs because 85 >= 80
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}")
print(f"Grade: {grade}")

# --- HTTP Status Code Checker ---
print()
print("--- HTTP Status Code Checker ---")

status_code = 404

if status_code == 200:
    print("200 — OK: Request successful")
elif status_code == 301:
    print("301 — Redirect: Page has moved")
elif status_code == 403:
    print("403 — Forbidden: Access denied")
elif status_code == 404:
    print("404 — Not Found: Page does not exist")   # This runs
elif status_code == 500:
    print("500 — Server Error: Something went wrong")
else:
    print(f"{status_code} — Unknown status code")

# --- User Role Assignment ---
print()
print("--- User Role Assignment ---")

access_level = 2

if access_level == 0:
    role = "Guest"
elif access_level == 1:
    role = "User"
elif access_level == 2:
    role = "Moderator"   # This runs because access_level is 2
elif access_level == 3:
    role = "Admin"
else:
    role = "Unknown"

print(f"Access Level: {access_level}")
print(f"Assigned Role: {role}")

# --- IMPORTANT NOTE ---
# Only the FIRST matching condition runs!
print()
print("--- Order Matters! ---")

value = 95

# This works correctly:
if value >= 90:
    print("A (90+)")     # This runs first — stops here!
elif value >= 80:
    print("B (80+)")     # Skipped even though 95 >= 80
elif value >= 70:
    print("C (70+)")     # Skipped

print()
print("✅ if-elif-else examples complete!")
