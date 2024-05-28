Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... choices = ['rock', 'paper', 'scissors']
... 
... user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
... if user_choice not in choices:
...     print("Invalid choice. Please choose rock, paper, or scissors.")
...     exit()
... 
... computer_choice = random.choice(choices)
... print(f"Computer chose: {computer_choice}")
... 
... if user_choice == computer_choice:
...     print("It's a tie!")
... elif (user_choice == 'rock' and computer_choice == 'scissors') or \
...      (user_choice == 'paper' and computer_choice == 'rock') or \
...      (user_choice == 'scissors' and computer_choice == 'paper'):
...     print("You win!")
... else:
