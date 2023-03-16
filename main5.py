#1

my_list = ["hello", "world", "python", "programming"]

new_list = []

for i in range(len(my_list)):
    if i % 2 == 0:
        new_list.append(my_list[i])
    else:
        new_list.append(my_list[i][::-1])

print(new_list)

#2

my_list = ["apple", "banana", "orange", "avocado"]

new_list = []

for string in my_list:
    if string[0] == "a":
        new_list.append(string)

print(new_list)

#3

my_list = ["apple", "banana", "orange", "avocado"]

new_list = [string for string in my_list if "a" in string]

print(new_list)

#4

#а

people = [{"name": "John", "age": 15}, {"name": "Alice", "age": 12}, {"name": "Bob", "age": 15}, {"name": "Jack", "age": 45}]

youngest_age = min(person["age"] for person in people)
youngest_names = [person["name"] for person in people if person["age"] == youngest_age]

print(youngest_names)

#б

people = [{"name": "John", "age": 15}, {"name": "Alice", "age": 12}, {"name": "Bob", "age": 15}, {"name": "Jack", "age": 45}]

longest_length = max(len(person["name"]) for person in people)
longest_names = [person["name"] for person in people if len(person["name"]) == longest_length]

print(longest_names)

#в

people = [{"name": "John", "age": 15}, {"name": "Alice", "age": 12}, {"name": "Bob", "age": 15}, {"name": "Jack", "age": 45}]

average_age = sum(person["age"] for person in people) / len(people)

print(average_age)

#5

#а

my_dict_1 = {"a": 1, "b": 2, "c": 3}
my_dict_2 = {"b": 4, "c": 5, "d": 6}

common_keys = [key for key in my_dict_1.keys() if key in my_dict_2]

print(common_keys)

#б

my_dict_1 = {"a": 1, "b": 2, "c": 3}
my_dict_2 = {"b": 4, "c": 5, "d": 6}

unique_keys = [key for key in my_dict_1.keys() if key not in my_dict_2]

print(unique_keys)

#в

my_dict_1 = {"a": 1, "b": 2, "c": 3}
my_dict_2 = {"b": 4, "c": 5, "d": 6}

new_dict = {key: my_dict_1[key] for key in my_dict_1.keys() if key not in my_dict_2}

print(new_dict)

#г

my_dict_1 = {1: 1, 2: 2, 11: 11}
my_dict_2 = {2: 22, 11: 11}

new_dict = {}

for key in set(list(my_dict_1.keys()) + list(my_dict_2.keys())):
    if key in my_dict_1 and key in my_dict_2:
        new_dict[key] = [my_dict_1[key], my_dict_2[key]]
    elif key in my_dict_1:
        new_dict[key] = my_dict_1[key]
    else:
        new_dict[key] = my_dict_2[key]

print(new_dict)
