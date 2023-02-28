value = int(input("Enter a value: "))
new_value = value / 2 if value < 100 else -value
print(new_value)

########################################################

value = int(input("Enter a value: "))
new_value = 1 if value < 100 else 0
print(new_value)

########################################################

new_value = int(input("Enter a value: "))
new_value = True if new_value < 100 else False
print(new_value)

########################################################

my_str = input("Enter a word: ")
my_str = my_str + my_str if len(my_str) < 5 else my_str
print(my_str)

########################################################

my_str = input("Enter a word: ")

if len(my_str) < 5:
    my_str += my_str[::-1]

print(my_str)

########################################################

def calculator():
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
    except ValueError:
        print("Введені значення некоректні.")
        return

    operation = input("Виберіть операцію (+, -, *, /): ")

    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Ділення на нуль!")
            result = num1 / num2
        else:
            raise ValueError("Некоректна операція!")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Помилка: {e}")
        return

    print(f"Результат: {result}")

    repeat = input("Чи потрібен ще калькулятор? (так або ні): ")
    if repeat.lower() == "так":
        calculator()

calculator()
