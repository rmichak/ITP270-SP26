# ============================================
# ITP 270 — Module 2: Type Conversion
# ============================================
# Converting between data types using:
#   int()   — convert to integer
#   float() — convert to float
#   str()   — convert to string
#   type()  — check the current type
# ============================================

# --- Checking Types with type() ---
# type() tells you what data type a value is.

port = 443
threat_level = 7.5
server = "web-01"
is_active = True

print("=== Checking Types ===")
print("port:", type(port))              # <class 'int'>
print("threat_level:", type(threat_level))  # <class 'float'>
print("server:", type(server))          # <class 'str'>
print("is_active:", type(is_active))    # <class 'bool'>

# --- String to Integer ---
# Use int() to convert text to a whole number.
# The text must LOOK like a whole number.

port_text = "443"                       # This is a string
port_number = int(port_text)            # Now it's an integer

print("\n=== String to Integer ===")
print("Before:", port_text, "| Type:", type(port_text))
print("After:", port_number, "| Type:", type(port_number))

# --- String to Float ---
# Use float() to convert text to a decimal number.

score_text = "7.5"                      # This is a string
score_number = float(score_text)        # Now it's a float

print("\n=== String to Float ===")
print("Before:", score_text, "| Type:", type(score_text))
print("After:", score_number, "| Type:", type(score_number))

# --- Integer to Float ---
# Use float() to add a decimal point to a whole number.

ssh_port = 22                           # This is an integer
ssh_float = float(ssh_port)             # Now it's 22.0

print("\n=== Integer to Float ===")
print("Before:", ssh_port, "| Type:", type(ssh_port))
print("After:", ssh_float, "| Type:", type(ssh_float))

# --- Float to Integer ---
# Use int() to drop the decimal part (does NOT round).

risk_score = 9.8                        # This is a float
risk_int = int(risk_score)              # Now it's 9 (NOT 10!)

print("\n=== Float to Integer ===")
print("Before:", risk_score, "| Type:", type(risk_score))
print("After:", risk_int, "| Type:", type(risk_int))
print("Notice: 9.8 became 9, not 10 — Python drops the decimal!")

# --- Number to String ---
# Use str() to convert a number to text.

http_port = 80                          # This is an integer
http_text = str(http_port)              # Now it's "80"

print("\n=== Number to String ===")
print("Before:", http_port, "| Type:", type(http_port))
print("After:", http_text, "| Type:", type(http_text))

# --- What DOESN'T Work ---
# You can only convert text that looks like a number.

print("\n=== What Doesn't Work ===")
print("int('443') works — '443' looks like a number")
print("int('hello') would CRASH — 'hello' is not a number")
print("int('3.14') would CRASH — use float('3.14') instead")
