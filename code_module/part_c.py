### Write a function to check if a number is a prime or not ###
import math

def is_prime(num):
    if num < 2:
        return False
    sqrt_val = int(math.sqrt(num)) + 1
    for i in range(2, sqrt_val):
        if num % i == 0:
            return False
    
    return True

### Swap a list's head and tail. ###
def swap_head_tail(input_list):
    if len (input_list) < 2:
        return input_list
    c = input_list[0]
    input_list[0] = input_list[-1]
    input_list[-1] = c
    
    return input_list

### Get the median of a list. ###
def get_median(int_list):
    count = len(int_list)
    if count == 0:
        return None
    int_list.sort()
    mid = int(count / 2)
    median = int_list[mid]
    if (count % 2 == 0) :
        median = (median + int_list[mid-1])
        median = median / 2
    
    return median

### calculator ###
def calculator():
    while True:
        op = input("type in your operation (+, -, *, /, e for exit):")[0]
        if op.lower() == 'e':
            break
        if op not in "+-*/":
            continue
        operand1 = int(input("type in 1st operand: "))
        operand2 = int(input("type in 2nd operand: "))
        result = 0
        if op == '+':
            result = operand1 + operand2
        elif op == '-':
            result = operand1 - operand2
        elif op == '*':
            result = operand1 * operand2
        elif operand2 != 0:
            result = operand1 / operand2
        else:
            print("error: divid by 0.")
        
        print(f"result: {result}")
    