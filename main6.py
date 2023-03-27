#1

def process_list(my_list):
    new_list = []
    for i, s in enumerate(my_list):
        if i % 2 == 0:
            new_list.append(s)
        else:
            new_list.append(s[::-1])
    return new_list
my_list = ["hello", "world", "how", "are", "you"]
new_list = process_list(my_list)
print(new_list)

#2

def filter_strings_starting_with_a(my_list):
    result_list = []
    for string in my_list:
        if string.startswith("a"):
            result_list.append(string)
    return result_list
my_list = ["apple", "banana", "avocado", "orange"]
result_list = filter_strings_starting_with_a(my_list)
print(result_list)

#3

def filter_strings_with_a(my_list):
    result_list = []
    for string in my_list:
        if "a" in string:
            result_list.append(string)
    return result_list
my_list = ["apple", "banana", "avocado", "orange", "pear"]
result_list = filter_strings_with_a(my_list)
print(result_list)

#4

def filter_strings(my_list):
    result_list = []
    for element in my_list:
        if isinstance(element, str):
            result_list.append(element)
    return result_list
my_list = ["apple", 1, "banana", 2, "orange"]
result_list = filter_strings(my_list)
print(result_list)

#5

def get_unique_characters(my_str):
    unique_chars = []
    for char in my_str:
        if my_str.count(char) == 1:
            unique_chars.append(char)
    return unique_chars
my_str = "hello world"
result_list = get_unique_characters(my_str)
print(result_list)

#6

def common_chars(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    common_set = set1.intersection(set2)
    return list(common_set)
s1 = "hello"
s2 = "world"
common = common_chars(s1, s2)
print(common)

#7

def common_chars(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    common = list(set1 & set2)
    return sorted(common)
str1 = "hello"
str2 = "world"
result = common_chars(str1, str2)
print(result)

#8

import random

def create_email(domains, names):
    first_name = random.choice(names)
    last_name = random.choice(names)
    domain = random.choice(domains)
    rand_str = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 7)))
    rand_num = random.randint(100, 999)
    email = f"{first_name}.{rand_num}@{rand_str}.{domain}"
    return email
names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print(e_mail)
