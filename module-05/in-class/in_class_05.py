"""
ITP 270 — Module 5: In-Class Exercises
========================================
Port Range Scanner Simulator

Fill in the code where you see # TODO comments.
Follow the instructions for each exercise.

Name: ___________________
Date: ___________________
"""

# ==============================================================
# Exercise 1 — Your First Loop
# Print the numbers 1 through 10 using a for loop.
# ==============================================================
print("=== Exercise 1: Numbers 1-10 ===")

# TODO: Write a for loop that prints numbers 1 through 10
# Hint: range(1, 11) gives you 1, 2, 3, ... 10


print()


# ==============================================================
# Exercise 2 — Scanning a Port Range
# Print "Scanning port X..." for each port from 1 to 20.
# ==============================================================
print("=== Exercise 2: Port Scanner ===")
print("Scanning ports 1-20...\n")

# TODO: Write a for loop that scans ports 1 through 20
# For each port, print: Scanning port X...
# After the loop, print: Scan complete.


print()


# ==============================================================
# Exercise 3 — Detecting Open Ports (Counter)
# Scan ports 1-100. Count how many "open" ports you find.
# ==============================================================
print("=== Exercise 3: Open Port Counter ===")
open_ports = [21, 22, 80, 443]  # Pretend these are open

# TODO: Create a counter variable, set it to 0

# TODO: Write a for loop that goes through ports 1 to 100
# Inside the loop:
#   - Check if the port is in the open_ports list
#   - If yes: print the port number and add 1 to your counter

# TODO: After the loop, print how many open ports were found


print()


# ==============================================================
# Exercise 4 — Risk Scoring (Accumulator)
# Assign risk points to each open port. Add up the total.
# ==============================================================
print("=== Exercise 4: Risk Assessment ===")
open_ports = [21, 22, 80, 443, 3389]
high_risk = [21, 3389]     # FTP, Remote Desktop
medium_risk = [22, 80]     # SSH, HTTP
low_risk = [443]           # HTTPS (encrypted)

# TODO: Create two variables: found (counter) and total_risk (accumulator)
#       Set both to 0

# TODO: Write a for loop through ports 1 to 100
# Inside the loop:
#   - Check if the port is in open_ports
#   - If yes: determine risk level (high=10, medium=5, low=2)
#   - Add the risk score to total_risk
#   - Add 1 to found
#   - Print the port, risk level, and points

# TODO: After the loop, print total ports found and total risk score


print()


# ==============================================================
# Exercise 5 — Skip Blocked Ports (continue)
# Skip ports on the blocklist. Only scan non-blocked ports.
# ==============================================================
print("=== Exercise 5: Blocklist Filter ===")
open_ports = [21, 22, 25, 80, 443, 8080]
blocked_ports = [25, 8080]
found = 0

# TODO: Write a for loop through ports 1 to 100
# Inside the loop:
#   - FIRST: Check if port is in blocked_ports
#     - If yes: use 'continue' to skip it
#   - THEN: Check if port is in open_ports
#     - If yes: print the port and add 1 to found

# TODO: After the loop, print how many ports were found


print()


# ==============================================================
# Exercise 6 — Stop on Critical (break)
# Stop scanning immediately if a critical port is found.
# ==============================================================
print("=== Exercise 6: Critical Alert ===")
open_ports = [22, 80, 443, 3389, 8443]
critical_ports = [3389, 23, 445]
found = 0
critical_found = False

# TODO: Write a for loop through ports 1 to 100
# Inside the loop:
#   - Check if port is in open_ports
#   - If yes:
#     - Add 1 to found
#     - Print the port
#     - Check if port is ALSO in critical_ports
#       - If yes: print an alert, set critical_found = True, and BREAK

# TODO: After the loop:
#   - If critical_found: print a warning message
#   - Else: print "all clear"


print()


# ==============================================================
# Exercise 7 — Full Scanner (Putting It All Together)
# Combine everything into one complete program.
# ==============================================================
print("=== Exercise 7: Complete Port Scanner ===")

# TODO: Create these variables:
#   open_ports = [21, 22, 53, 80, 443, 3306, 3389, 8080]
#   blocked_ports = [25, 110]
#   critical_ports = [3389, 445, 23]
#   found = 0
#   total_risk = 0
#   critical_found = False

# TODO: Ask the user for start_port and end_port using input()
#       Convert to integers with int()

# TODO: Print a header showing the scan range

# TODO: Write the main scan loop (for port in range(...))
#   - Skip blocked ports (continue)
#   - Check if port is open
#   - If open:
#     - Count it
#     - Determine risk (critical=10, medium=5, low=2)
#     - Add risk to total_risk
#     - Print port with risk level
#     - If critical: alert and break

# TODO: Print results: ports found, risk score, status

print("\n🎉 Congratulations! You built a Port Scanner Simulator!")
