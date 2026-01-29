"""
ITP 270 — Module 5: while Loop Examples
=========================================
A while loop keeps running AS LONG AS a condition is True.
Use it when you DON'T KNOW how many times to repeat.
"""

# --- Example 1: Simple countdown ---
# We start at 5 and count down to 1
# The loop stops when count reaches 0 (condition becomes False)
print("=== Example 1: Countdown ===")
count = 5                       # Start at 5

while count > 0:                # Keep going while count is positive
    print(f"  {count}...")
    count = count - 1           # IMPORTANT: decrease count each time!

print("  Liftoff! 🚀")
print()

# --- Example 2: Password check ---
# Keep asking until the user types the correct password
# We don't know how many tries it will take!
print("=== Example 2: Password Check ===")
correct_password = "secure123"
user_input = ""                 # Start empty so condition is True

while user_input != correct_password:
    user_input = input("Enter password: ")
    if user_input != correct_password:
        print("  Wrong! Try again.\n")

print("  ✅ Access granted!\n")

# --- Example 3: Menu system ---
# A while loop is perfect for menus — keep showing options
# until the user chooses to quit
print("=== Example 3: Security Menu ===")
choice = ""

while choice != "4":
    print("1. Scan ports")
    print("2. Check passwords")
    print("3. View logs")
    print("4. Exit")
    choice = input("Choose (1-4): ")

    if choice == "1":
        print("  → Scanning ports...\n")
    elif choice == "2":
        print("  → Checking passwords...\n")
    elif choice == "3":
        print("  → Viewing logs...\n")
    elif choice == "4":
        print("  → Goodbye!\n")
    else:
        print("  ❌ Invalid choice. Try again.\n")

# --- Example 4: The WRONG way (infinite loop) ---
# DO NOT RUN THIS without a way to stop it!
# Uncomment to see what happens (press Ctrl+C to escape)
#
# print("=== INFINITE LOOP (DON'T RUN!) ===")
# x = 1
# while x <= 5:
#     print(x)
#     # OOPS! We forgot to change x!
#     # x stays at 1 forever → infinite loop
