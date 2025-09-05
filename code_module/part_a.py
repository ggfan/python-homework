# lib/part_a.py

# A global variable exported
greeting = "Hello from part_a!"

# Function: is_palindrome
# Description:
#   check a string is palindrome
# Notes:
#   there is a simpler implentation such as this: 
#   s = s.lower()
#   return s = s[::-1]
# but it creates 2 temp arrays, not memory efficient.
# This version checks string in place, more memroy efficient.
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        c1 = s[left]
        c2 = s[right]

        # Normalize both characters to lowercase if they're uppercase
        if 'A' <= c1 <= 'Z':
            c1 = chr(ord(c1) + 32)
        if 'A' <= c2 <= 'Z':
            c2 = chr(ord(c2) + 32)

        if c1 != c2:
            return False

        left += 1
        right -= 1

    return True

### Find the 2nd largest item in an list ####
def find_2nd_largest(data_list):
    list_len = len(data_list)
    x = None
    y = None
    if list_len < 2:
        return y
    if data_list[0] < data_list[1]:
        x = data_list[1]
        y = data_list[0]
    else:
        x = data_list[0]
        y = data_list[1]
    
    for i in range(2, list_len):
        if data_list[i] > x:
            y = x
            x = data_list[i]
        elif data_list[i] > y:
            y = data_list[i]
    
    return y
