# test/test_lib.py
import inspect
from code_module import is_palindrome, greeting, \
                find_2nd_largest

# A helper function to get calling function name.
def print_test_result(result):
    print(inspect.currentframe().f_back.f_code.co_name,
          f"Test Result: {result}.")

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
    
    print_test_result(test_pass)
    return test_pass

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
    
    print_test_result(test_pass)
    return test_pass

# main test entry.
def run_test():
    return test_is_palindrome() and test_find_2nd_largest()
