# ITP 270 — Module 6: In-Class Activity
# IP Address Manager
# ===================================
# Name: ________________________
# Date: ________________________

# ============================================================
# EXERCISE 1 — Create Your IP List
# Create a list, print it, print first and last items
# ============================================================

# TODO: Create a list called ip_addresses with these IPs:
#   "192.168.1.10", "192.168.1.25", "192.168.1.50"


# TODO: Print the entire list


# TODO: Print the first IP (index 0)


# TODO: Print the last IP (negative indexing)



# ============================================================
# EXERCISE 2 — Add IPs to the List
# Use append() to add new IPs
# ============================================================

# TODO: Use append() to add "10.0.0.1"


# TODO: Use append() to add "172.16.0.5"


# TODO: Print the list and its length using len()



# ============================================================
# EXERCISE 3 — Remove an IP
# Use remove() and pop()
# ============================================================

# TODO: Use remove() to remove "192.168.1.25"


# TODO: Print the updated list and its length


# TODO: Use pop() to remove the last item. Save it in removed_ip.


# TODO: Print which IP was removed and the remaining list



# ============================================================
# EXERCISE 4 — Search the IP List
# Use input() and the 'in' keyword
# ============================================================

# TODO: Ask the user to enter an IP address
# search_ip = input("Enter an IP to search: ")

# TODO: Check if search_ip is in ip_addresses
# If found: print "✅ [IP] is on the network"
# If not found: print "❌ [IP] is NOT on the network"



# ============================================================
# EXERCISE 5 — Loop and Display All IPs
# Use enumerate() and sort()
# ============================================================

# TODO: Print a header "--- Network IP Addresses ---"

# TODO: Use enumerate() in a for loop to print each IP with its index
# Format: "[0] 192.168.1.10"

# TODO: Sort the list with .sort()

# TODO: Print "--- Sorted ---" and loop again to show sorted order



# ============================================================
# EXERCISE 6 — Store IP Metadata in a Dictionary
# Create a nested dictionary
# ============================================================

# TODO: Create ip_info dictionary (copy from the activity sheet)
# ip_info = {
#     "192.168.1.10": {"status": "active", "device": "Web Server"},
#     ...
# }

# TODO: Print the device name for "192.168.1.10"


# TODO: Add "172.16.0.5" with status "active" and device "Firewall"


# TODO: Update the status of "10.0.0.1" to "decommissioned"



# ============================================================
# EXERCISE 7 — Full Network Report
# Loop through dictionary with .items()
# ============================================================

# TODO: Print "========== NETWORK REPORT =========="

# TODO: Loop through ip_info.items() and print each entry
# Format: "IP: 192.168.1.10  | Device: Web Server  | Status: active"

# TODO: Count active devices vs. inactive/other

# TODO: Print the counts and total


# ============================================================
# 🌟 BONUS — Menu System (if you finish early)
# ============================================================
# Uncomment and complete the menu below:

# while True:
#     print("\n--- IP Manager Menu ---")
#     print("1. View all IPs")
#     print("2. Add an IP")
#     print("3. Remove an IP")
#     print("4. Search for an IP")
#     print("5. Network Report")
#     print("6. Quit")
#     
#     choice = input("Choose (1-6): ")
#     
#     if choice == "1":
#         pass   # Replace with your code
#     elif choice == "6":
#         print("Goodbye!")
#         break

print("\n🎉 Activity complete!")
