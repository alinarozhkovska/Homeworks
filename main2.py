string = input("Enter a word: ")

# a
print(string[2])

# b
print(string[-2])

# c
print(string[:5])

# d
print(string[:-2])

# e
print(string[::2])

# f
print(string[1::2])

# g
print(string[::-1])

# h
print(string[-1::-2])

# i
print(len(string))

########################################################

string = input("Введіть рядок: ")
word_count = string.count(' ') + 1
print("Кількість слів у рядку:", word_count)

########################################################

s = input("Введіть рядок: ")
ch = input("Введіть символ: ")

for i in range(len(s)):
    if s.find(ch, i, i+1) != -1:
        print("Символ", ch, "знайдено на позиції", i)

########################################################

string = input("Введіть рядок: ")

# знаходимо перше входження літери h
first_h = string.find('h')

# знаходимо останнє входження літери h
last_h = string.rfind('h')

# замінюємо літеру h на літеру H від першого + 1 до останнього
new_string = string[:first_h+1] + string[first_h+1:last_h].replace('h', 'H') + string[last_h:]

print("Результат:", new_string)
