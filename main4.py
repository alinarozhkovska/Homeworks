#1

number = int(input("Введіть ціле число: "))
count = 0

while number > 0:
    if number % 10 == 0:
        count += 1
    number //= 10

print("Кількість нулів у числі:", count)

#2

number = int(input("Введіть ціле число: "))
count = 0

while number % 10 == 0 and number != 0:
    count += 1
    number //= 10

print("Кількість нулів наприкінці числа:", count)

#3

my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [6, 7, 8, 9, 10]
my_result = []

for i in range(len(my_list_1)):
    if i % 2 == 0:
        my_result.append(my_list_1[i])

for i in range(len(my_list_2)):
    if i % 2 == 0:
        my_result.append(my_list_2[i])

print(my_result)

#4

my_list = [1, 2, 3, 4]
new_list = my_list[1:] + [my_list[0]]

print(new_list)

#5

my_list = [1, 2, 3, 4]
my_list.append(my_list.pop(0))

print(my_list)

#6

s = "100 більше ніж 10 , але менше ніж 200"
total_sum = 0
for word in s.split():
    if word.isdigit():
        total_sum += int(word)
print(total_sum)

#7

my_list = [2,4,1,5,3,9,0,7]

count = 0
for i in range(1, len(my_list)-1):
    if my_list[i] > my_list[i-1] + my_list[i+1]:
        count += 1

print(count)

#8

my_list = [1, 2, 3, "11", "22", 33]

new_list = []
for item in my_list:
    if type(item) == str:
        new_list.append(item)

print(new_list)

#9

my_str = "abbcddeffggh"

my_list = []
for char in my_str:
    if my_str.count(char) == 1:
        my_list.append(char)

print(my_list)

#10

str1 = "hello world"
str2 = "goodbye world"
common_chars = []

# перетворити рядки у множини символів
set1 = set(str1)
set2 = set(str2)

# перебрати унікальні символи у першій множині
for char in set1:
    # перевірити, чи символ зустрічається у другій множині
    if char in set2:
        common_chars.append(char)

print(common_chars)

#11

str1 = "aaaasdf1"
str2 = "asdfff2"

# знаходимо множини символів, які зустрічаються тільки один раз у кожному з рядків
set1 = set([ch for ch in str1 if str1.count(ch) == 1])
set2 = set([ch for ch in str2 if str2.count(ch) == 1])

# знаходимо перетин множин і перетворюємо його у список
result = list(set1 & set2)
print(result) # ['d', 's']
