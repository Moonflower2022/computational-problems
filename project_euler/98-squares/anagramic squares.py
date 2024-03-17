import math
import itertools
import json
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'words.txt')

file = open(filename, "r")

text = file.read()

words = [word[:-1][1:] for word in text.split(",")]

def get_good_num_dicts(word):
    good_num_dicts = []

    letter_set = list(set(word))

    letters = list(word)
    
    num_dict = {}
    
    for i in range(10**len(word)):
        for j in range(len(word)):
            num_dict[letters[j]] = get_digit(i, j)
        if (math.sqrt(chars_to_nums(word, num_dict)).is_integer()):
            good_num_dicts.append(str(num_dict))
    return good_num_dicts

def get_digit(number, n):
    return number // 10**n % 10

def chars_to_nums(str, dictionary):
    ret = 0
    for i in range(len(str)):
        ret += dictionary[str[i]] * 10 ** (len(str) - i - 1)
    return ret

highest_value = 0

words_copy = list(words)

for upper_word in words:
    if len(upper_word) > 10:
        word = upper_word.lower()

        good_dict_strings = get_good_num_dicts(word)

        for perm in ["".join(perm) for perm in itertools.permutations(word)]:
            if (perm != word):
                for dict_string in good_dict_strings:
                    num_dict = json.loads(dict_string.replace("\'", "\""))
                    if (math.sqrt(chars_to_nums(perm, num_dict)).is_integer()):
                        if (chars_to_nums(perm, num_dict) > highest_value):
                            highest_value = chars_to_nums(perm, num_dict)
                        elif (chars_to_nums(word, num_dict) > highest_value):
                            highest_value = chars_to_nums(word, num_dict)

print(highest_value)

file.close()
