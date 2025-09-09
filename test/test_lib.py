# test/test_lib.py
import inspect
from code_module import \
    is_palindrome,find_2nd_largest, find_highest_marks, merge_lists_to_dict, \
    string_to_dict, filter_with_len, find_uniques,reverse_words_in_sentence, calculate_sum, \
    is_prime, swap_head_tail, get_median, calculator

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

############### Part_b ##################
def test_string_to_dict():
    tests = ["abcde", "aabddc", "", "yyyyyy"]
    expected = [
        {'a': 1, 'b' : 1, 'c':1, 'd' : 1, 'e':1},
        {'a':2, 'b': 1, 'c': 1, 'd':2},
        {},
        {'y': 6}
    ]
    test_pass = True
    for idx in range(len(tests)):
        result = string_to_dict(tests[idx])
        if result != expected[idx]:
            test_pass = False
            print(f"Failed {tests[idx]}, expected {expected[idx]}, got {result}")

    print_test_result(test_pass)
    return test_pass

def test_filter_with_len():
    len_req = 5
    tests = [
        ["a", "b", "c", "d", "e", "excellent"],
        ["123", "345"],
        ["LongWords", "SuperLongWords", "pneumonoultramicroscopicsilicovolcanoconiosis"],
        []
    ]
    expected = [
         ["a", "b", "c", "d", "e"],
         ["123", "345"],
         [],
         []
    ]

    test_pass = True
    for idx in range(len(tests)):
        result = filter_with_len(tests[idx], len_req)
        result.sort()
        expected[idx].sort()
        if expected[idx] != result:
            test_pass = False
            print(f"Failed {tests[idx]}, expected {expected[idx]}, got {result}")
    
    print_test_result(test_pass)
    return test_pass

def test_find_uniques():
    tests = [
        [1, 2, 3, 4, 5, 8, 100, 3],
        ["this", "is", "a", "unique", "sentence"],
        ["dup", "dup", "dup"],
        []
    ]
    expected = [
        [1, 2, 3, 4, 5, 8, 100],
        ["this", "is", "a", "unique", "sentence"],
        ["dup"],
        []
    ]
    test_pass = True
    for idx in range(len(tests)):
        result = find_uniques(tests[idx])
        if expected[idx] != result:
            test_pass = False
            print(f"Failed {tests[idx]}, expected {expected[idx]}, got {result}")
    
    print_test_result(test_pass)
    return test_pass

def test_reverse_words_in_sentence():
    tests = [
        "This is the 1st Sentence.",
        "Good boy!",
        "aha",
        "."
        ""
    ]
    expected = [
        "sihT si eht ts1 ecnetneS.",
        "dooG yob!",
        "aha",
        ".",
        ""
    ]
    test_pass = True
    for idx in range(len(tests)):
        result = reverse_words_in_sentence(tests[idx])
        if expected[idx] != result:
            test_pass = False
            print(f"Failed {tests[idx]}, expected {expected[idx]}, got {result}")
    
    print_test_result(test_pass)
    return test_pass

def test_calculate_sum():
    tests = [
        "1234b5g67",
        "abc1d9",
        "100",
        ""
    ]
    expected = [28, 10, 1, 0]
    test_pass = True
    for idx in range(len(tests)):
        result = calculate_sum(tests[idx])
        if expected[idx] != result:
            test_pass = False
            print(f"Failed {tests[idx]}, expected {expected[idx]}, got {result}")
    
    print_test_result(test_pass)
    return test_pass


############### Part_b ##################
def test_is_prime():
    tests =    [0, 1, 2, 3, 7, 9, 99]
    expected = [False, False, True, True, True, False, False]
    test_pass = True

    for idx in range(len(tests)):
        result = is_prime(tests[idx])
        if result != expected[idx]:
            test_pass = False
            print(f"Failed {tests[idx]}, expected {expected[idx]}, got {result}")
    
    print_test_result(test_pass)
    return test_pass

def test_swap_head_tail():
    tests = [
        [0, 1, 2, 3, 7, 9, 99],
        ['a', 'b', 'c', 'd', 'e', 'f'],
        [] ]
    expected = [
        [99, 1, 2, 3, 7, 9, 0],
        ['f', 'b', 'c', 'd', 'e', 'a'],
        []]
    test_pass = True

    for idx in range(len(tests)):
        result = swap_head_tail(tests[idx])
        if result != expected[idx]:
            test_pass = False
            print(f"Failed {tests[idx]}, expected {expected[idx]}, got {result}")
    
    print_test_result(test_pass)
    return test_pass

def test_get_media():
    tests = [
        [0, 1, 2, 3, 7, 9, 99],
        [20, 40, 80, 100, 120, 60],
        [],
        [5]
        ]
    expected = [3, 70, None, 5]
    test_pass = True

    for idx in range(len(tests)):
        result = get_median(tests[idx])
        if result != expected[idx]:
            test_pass = False
            print(f"Failed {tests[idx]}, expected {expected[idx]}, got {result}")
    
    print_test_result(test_pass)
    return test_pass

def test_calculator():
    calculator()
    return True

# main test entry.
def run_test():
    return test_calculator()

