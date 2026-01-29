# ============================================================
# function_basics.py — Introduction to Functions
# ITP 270 – Python Programming (Module 7)
# ============================================================
# A function is a reusable block of code that performs a task.
# Instead of writing the same code over and over, you put it
# in a function and call it whenever you need it.
#
# Why use functions?
#   1. Reusability — write once, use many times
#   2. Organization — break big problems into small pieces
#   3. Readability — give blocks of code meaningful names
#
# Syntax:
#   def function_name():
#       code inside the function
#
# To RUN the function, "call" it:
#   function_name()
# ============================================================

# --- Defining a simple function ---
# "def" means "define" — you are creating a function
# The code inside does NOT run until you call the function

def greet():
    """Display a simple greeting message."""
    print("Hello! Welcome to ITP 270.")
    print("Let's learn about functions!")

# Nothing has printed yet! We only DEFINED the function.
# Now let's CALL it:

print("--- Calling greet() ---")
greet()   # This runs the code inside the function

# --- You can call a function multiple times ---
print()
print("--- Calling greet() again ---")
greet()   # Same function, runs again

# --- Another function ---
def show_security_warning():
    """Display a security warning banner."""
    print("=" * 40)
    print("⚠️  SECURITY WARNING")
    print("   Unauthorized access is prohibited.")
    print("   All activity is monitored and logged.")
    print("=" * 40)

print()
show_security_warning()

# --- Functions help organize code ---
def print_separator():
    """Print a visual separator line."""
    print("-" * 40)

# Now we can use print_separator() anywhere!
print()
print("First section")
print_separator()
print("Second section")
print_separator()
print("Third section")

# --- Order matters: Define BEFORE you call ---
# This works:
def say_goodbye():
    """Display a goodbye message."""
    print("Goodbye! Keep practicing Python! 👋")

say_goodbye()   # Works because say_goodbye is defined above

# This would cause an error (uncomment to see):
# say_hello()   # ❌ Error! say_hello is not defined yet
#
# def say_hello():
#     print("Hello!")

print()
print("✅ Function basics complete!")
