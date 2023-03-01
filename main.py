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
