# test/test_lib.py
import inspect
from code_module import is_palindrome,find_2nd_largest, find_highest_marks, merge_lists_to_dict

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

def test_find_highest_marks():
    classes = [{"john":95, "Kathy":99, "David":50, "Darling Hao": 100, "Back Rear":0},
               {"Only One": 100},
               {"john" : 95, "Kathy":99, "David":50, "Darling Hao": 100, "Back Rear":0, "Mr. Perfect":100},
               {}
               ]
    expected = [
        ["Darling Hao"],
        ["Only One"],
        ["Darling Hao", "Mr. Perfect"],
        []
    ]
    test_pass =  True
    for idx in range(len(classes)):
        great_students = find_highest_marks(classes[idx])
        great_students.sort()
        expected[idx].sort()

        if great_students != expected[idx]:
            test_pass = False
            print(f"failed test {classes[idx]}, expected {expected[idx]}, got {great_students}")
    
    print_test_result(test_pass)
    return test_pass

def test_merge_lists_to_dict():
    lists = [
        (["a", "b", "c", "d"], [90, 80, 70, 90]),
        ([], [1, 3, 5, 190]),
        (["henry", "jack", "terry", "gausse"], ["A", "B", "C"])
    ]
    dicts = [
        {"a":90, "b":80, "c":70, "d":90},
        {},
        {"henry":"A", "jack":"B", "terry":"C"}
    ]

    test_pass = True
    idx = 0
    for (a, b) in lists:
        result = merge_lists_to_dict(a, b)
        if result != dicts[idx]:
            test_pass = False
            print(f"Failed for {a}: {b}: got {result}, expecting {dicts[idx]}")
        idx += 1

    print_test_result(test_pass)
    return test_pass

# main test entry.
def run_test():
    return test_merge_lists_to_dict()
