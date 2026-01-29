"""
Program:  Comments Demo — All Types of Comments in Python
Course:   ITP 270 — Programming for Cybersecurity
Author:   [Your Name]
Date:     [Today's Date]

Purpose:  This program demonstrates every type of comment in Python.
          Comments are notes for humans — Python ignores them completely.
"""

# =============================================
# TYPE 1: Single-Line Comments (using #)
# =============================================

# This is a full-line comment. Python skips this entire line.
# You can write anything here — Python does not care!

# Use single-line comments to explain WHAT your code does:
print("This line runs normally")  # This is an inline comment

# =============================================
# TYPE 2: Multi-Line Comments (using ''' or """)
# =============================================

'''
This is a multi-line comment using single triple quotes.
You can write as many lines as you want here.
Python will ignore all of it.

Multi-line comments are useful for:
- Describing what a program does (file headers)
- Explaining complex logic
- Temporarily disabling code (commenting out)
'''

"""
This is a multi-line comment using double triple quotes.
Both ''' and triple double-quotes work exactly the same way.
Most programmers pick one style and stick with it.
"""

# =============================================
# TYPE 3: Using Comments in Practice
# =============================================

# Good comment: explains WHY something is done
# Check if the password meets the 12-character minimum policy
print("Password check: PASSED")

# Bad comment: states the obvious (don't do this!)
# Print hello
print("Hello")

# TODO comment: reminds you of unfinished work
# TODO: Add error handling for invalid passwords

# Section divider comment: organizes your code
# --- End of Program ---
print("Demo complete!")
