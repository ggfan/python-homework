### Count the frequency of each character in a string and print it as a dictionary ###
def string_to_dict(s):
    dict = {}
    
    for c in s:
        dict[c] = dict.get(c, 0) + 1
    
    print(dict)
    return dict

### Filter out all words shorter than 5 characters ###
def filter_with_len(word_list, len_req):
    result_list = []
    for word in word_list:
        if len(word) < len_req:
            result_list.append(word)
    return result_list

### Find all unique elements in a list ####
def find_uniques(given_list):
    new_list = []
    for element in given_list:
        if element not in new_list:
            new_list.append(element)
    
    return new_list

### Reverse words in a sentence preserving word order ###
def reverse_words_in_sentence(sentence):
    words = sentence.split()
    reversed_words = []
    for w in words:
        if w[-1].isalpha():
            reversed_words.append(w[::-1])
        else:
            tmp = w[-2::-1]
            tmp += w[-1]     # Reattach the non-alpha character in the end.
            reversed_words.append(tmp)           
    
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

### Calculate the sum of all number digits in a mixed string. ###
def calculate_sum(mixed_string):
    total = 0

    for c in mixed_string:
        if c.isdigit():
            total += int(c)
    
    return total
