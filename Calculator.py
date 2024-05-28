Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Simple Calculator in Python
... 
... print("** CALCULAROR **")
... 
... try:
...     num1 = float(input("Enter first number: "))
...     num2 = float(input("Enter second number: "))
... except ValueError:
...     print("Invalid input Enter numeric values.")
...     exit()
... 
... print("Select operation:")
... print("1. Add")
... print("2. Subtract")
... print("3. Multiply")
... print("4. Divide")
... 
... choice = input("Enter choice (1/2/3/4): ")
... 
... if choice == '1':
...     result = num1 + num2
...     print(f"The result of {num1} + {num2} is: {result}")
... elif choice == '2':
...     result = num1 - num2
...     print(f"The result of {num1} - {num2} is: {result}")
... elif choice == '3':
...     result = num1 * num2
...     print(f"The result of {num1} * {num2} is: {result}")
... elif choice == '4':
...     if num2 != 0:
...         result = num1 / num2
...         print(f"The result of {num1} / {num2} is: {result}")
...     else:
...         print("Error! Division by zero.")
... else:
