# ============================================================
# ITP 270 — Module 4: if-elif-else Chains
# ============================================================
# elif = "else if" — check MULTIPLE conditions in order.
# Python checks from top to bottom.
# The FIRST True condition runs, then ALL others are skipped.
# ============================================================

# --- Example 1: Security Clearance ---
print("=== Example 1: Security Clearance ===")
clearance = int(input("Enter clearance level (1-5): "))

if clearance == 5:
    print("TOP SECRET — Full access granted.")
elif clearance == 4:
    print("SECRET — Restricted areas accessible.")
elif clearance == 3:
    print("CONFIDENTIAL — Limited access.")
elif clearance >= 1:
    print("BASIC — Public areas only.")
else:
    print("INVALID — Clearance not recognized.")

print("Clearance check complete.")
print()

# --- Example 2: Grade Calculator ---
print("=== Example 2: Grade Calculator ===")
score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

print()

# --- Example 3: Threat Level Assessment ---
print("=== Example 3: Threat Level ===")
threat_score = int(input("Enter threat score (0-100): "))

if threat_score >= 90:
    print("🔴 CRITICAL — Immediate action required!")
elif threat_score >= 70:
    print("🟠 HIGH — Investigate immediately.")
elif threat_score >= 50:
    print("🟡 MEDIUM — Monitor closely.")
elif threat_score >= 20:
    print("🟢 LOW — Routine monitoring.")
else:
    print("⚪ NONE — No threat detected.")

# --- KEY POINTS ---
# 1. Must START with if (exactly one)
# 2. Can have as many elif as you want
# 3. else is optional but must be LAST
# 4. Only ONE block runs (the first True one)
# 5. ORDER MATTERS — put specific conditions first!
