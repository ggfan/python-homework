### 15.Find the missing number ###
def find_the_missing_number(nums):
    n = len(nums)

    total = int((n+1) * (n+2) / 2)
    for val in nums:
        total -= val
    return total

def find_the_missing_number2(nums):
    n = len(nums) + 1
    xor_all = 0
    for val in range(n+1):
        xor_all = xor_all ^ val
    xor_nums = 0
    for val in nums:
        xor_nums = xor_nums ^ val

    return (xor_nums ^ xor_all)

### 16. is palindrome function ###
def is_palindrome_string(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    
    return True

### 17. Get frequency of list elements. ###
def get_element_frequency(list_data):
    distribution = {}
    for e in list_data:
        distribution[e] = distribution.get(e, 0) + 1
    return distribution

### 18. Simple search in a list. ###
def find_item(data, item):
    for idx, val in enumerate(data):
        if val == item:
            return idx
        
    return -1
