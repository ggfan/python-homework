# is_palindrome
def is_palindrome(s):

    return True


###Unit Level Test(ULT) for is_palindrome()
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

if __name__ == "__main__":
    # This block runs only if the script is executed directly,
    # not when imported as a module.
    test_is_palindrome()
