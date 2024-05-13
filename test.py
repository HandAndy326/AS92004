import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
operator = random.choice(['+', '-', '*'])
if operator == '+':
    answer = num1 + num2
elif operator == '-':
    answer = num1 - num2
user = int(input(f"What is {num1} {operator} {num2} = "))
if user == answer:
    print("correct!")
if user != answer:
    print("wrong")
