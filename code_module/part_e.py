### 19. calculate factorial of a number ###
def calculate_factorial(num):
    fact = 1
    idx = 1
    while idx <= num:
        fact = fact * idx
        idx += 1
    
    return fact
### 20. counting vowels in a string. ###
def count_vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiou":
            count += 1
    return count

### 21. Get sum and average for a list. ###
def get_sum_and_ave(data):
    if len(data) == 0:
        return (0, 0)
    total = 0
    for v in data:
        total += v
    return (total, total/len(data))
### 22. Is in a list function. ###
def is_in(data, item):
    for val in data:
        if val == item:
            return True
    return False

### 23. Generate the fibonacci. ###
def get_fibonacci(n):
    result = []
    result.append(0)
    if n == 0: 
        return result
    result.append(1)
    if n == 1:
        return result
    
    idx = 2
    while idx <= n:
        next = result[-1] + result[-2]
        result.append(next)
        idx += 1
    
    return result

### 24. divid 2 numbers and handle ZeroDivisionError & ValueError ###
def divid_numbers(n1, n2):
    try:
        result = n1 / n2
    except ZeroDivisionError:
        result = None
    
    return result

### 25. bubble sort ###
def bubble_sort(data):
    cur_pos = 0
    idx = len(data) - 1
    while cur_pos < idx:
        while cur_pos < idx:
            if data[idx-1] > data[idx]:
                data[idx-1], data[idx] = data[idx], data[idx-1]
            idx -= 1
        
        idx = len(data) - 1
        cur_pos += 1
    return data

def bubble_sort2(data):
    n = len(data)
    for i in range(n-1):
        swapped = False
        for j in range(n-1, i, -1):
            if data[j-1] > data[j]:
                data[j-1], data[j] = data[j], data[j-1]
                swapped = True
        if not swapped:
            break

    return data
