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


# Unit Level Test(ULT) for is_palindrome()
def test_is_palindrome():
    """
    Create testing strings
    """
    test_strs = [("ABCDCBA", True),
                 ("level", True),
                 ("12321", True),
                 ("Level", True),
                 ("NotPalindrome", False)]
    test_pass = True
    for str, result in test_strs:
        if result != is_palindrome(str):
            print(f"Faied for {str}, expected {result}!!")
            test_pass = False
    
    print(f"Final Test Result: {test_pass}!")
    return test_pass

# Function: sqaure_even_item()
# Description:
#   Square the even elements in a given list.
#   In place operation(without creating extra arrays)
def square_even_item(data_list):
    for i in range(len(data_list)):
        if data_list[i] & 1 == 0:
            c = data_list[i]
            data_list[i] = c * c
    
    return data_list

def test_square_even_item():
    test_lists = [
        ([1,2,3,4,5], [1, 4, 3, 16, 5]),
        ([11, 13, 15, 17], [11, 13, 15,17]),
        ([10], [100]), ([5], [5]),
        ([], []),
    ]
    test_pass = True
    for x, y in test_lists:
        result = square_even_item(x)
        if result != y:
            test_pass = False
            print(f"failed {result}, expecting: {y}")
    
    print(f"Test result: {test_pass}")
    return test_pass

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

def test_find_2nd_largest():
    test_pass = True
    
    test_data =  [
        ([1,3,2,5], 3),
        ([100,3000], 100),
        ([234], None),
        ([], None),
    ]
    for x, y in test_data:
        result = find_2nd_largest(x)
        if y != result:
            test_pass = False
            print(f"failed test {x}, returns {result}, expecting {y}")
    
    print(f"Test result: {test_pass}")
    return test_pass

if __name__ == "__main__":
    # This block runs only if the script is executed directly,
    # not when imported as a module.
    test_find_2nd_largest()
