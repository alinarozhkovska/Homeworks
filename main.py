print("Choose an operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter the operation number (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", (num1+num2))

elif choice == '2':
    print(num1, "-", num2, "=", (num1-num2))

elif choice == '3':
    print(num1, "*", num2, "=", (num1*num2))

elif choice == '4':
    print(num1, "/", num2, "=", (num1//num2))

else:
    print("Incorrect choice of operation")
