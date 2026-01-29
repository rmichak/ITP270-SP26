# ============================================================
# scope_demo.py — Variable Scope: Local vs Global
# ITP 270 – Python Programming (Module 7)
# ============================================================
# "Scope" means WHERE a variable can be used.
#
# Local variable  = created INSIDE a function
#                   → only works inside that function
#
# Global variable = created OUTSIDE all functions
#                   → can be read from anywhere
#
# Think of it like rooms in a building:
#   - Local variables are items in a specific room (private)
#   - Global variables are items in the lobby (shared)
# ============================================================

# --- Local variable example ---
print("--- Local Variables ---")

def my_function():
    """Demonstrate a local variable."""
    secret = "hidden"        # This is LOCAL to my_function
    print(f"Inside function: secret = {secret}")

my_function()

# Trying to access 'secret' outside the function would cause an error:
# print(secret)   # ❌ NameError: name 'secret' is not defined
print("Outside function: 'secret' does not exist here!")

# --- Global variable example ---
print()
print("--- Global Variables ---")

company = "CyberSafe Inc."    # This is GLOBAL — defined outside any function

def show_company():
    """Read the global variable."""
    # We can READ global variables inside a function
    print(f"Company: {company}")

show_company()            # Output: Company: CyberSafe Inc.
print(f"Also here: {company}")  # Works outside the function too

# --- Local and global with same name ---
print()
print("--- Same Name, Different Scope ---")

message = "I am global"    # Global variable

def demo():
    """Show that local variables don't affect global ones."""
    message = "I am local"   # This creates a NEW local variable
    print(f"Inside function: {message}")   # Uses the LOCAL one

demo()                                     # Output: I am local
print(f"Outside function: {message}")      # Output: I am global
# The global variable was NOT changed!

# --- Each function has its own scope ---
print()
print("--- Separate Scopes ---")

def function_a():
    """Function A has its own local variable."""
    x = 10
    print(f"function_a: x = {x}")

def function_b():
    """Function B has its own local variable."""
    x = 99
    print(f"function_b: x = {x}")

function_a()   # Output: function_a: x = 10
function_b()   # Output: function_b: x = 99
# These are DIFFERENT variables — they just have the same name!

# --- Best practice ---
print()
print("--- Best Practice ---")
print("✅ Pass values through parameters instead of relying on globals.")
print("   This makes functions independent and easier to test.")

# GOOD: Pass data as a parameter
def greet_user(name):
    """Greet using a parameter (good practice)."""
    print(f"Hello, {name}!")

greet_user("Alice")   # Clear where the data comes from

# AVOID: Relying on global variables
user_name = "Bob"
def greet_global():
    """Greet using a global (works but less clear)."""
    print(f"Hello, {user_name}!")

greet_global()   # Works, but harder to track where data comes from

print()
print("✅ Scope demo complete!")
