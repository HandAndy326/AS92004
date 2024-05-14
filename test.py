import random
instruction = input("Do you know how to do a maths quiz? ").lower()
instrustions = instruction[0]
if instrustions == ("n"):
    print('''You are going to select a difficulty out of primary and intermediate.
Then you are going to get a question that is randomly generated which you have to answer
''')
elif instrustions == ("y"):
    print("Let's start")
else:
    print("Please enter either yes or no")

difficulty = input("Do you want the primary school questions or the intermediate school questions? ")
if difficulty == ("primary"):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-',])
elif difficulty == ("intermediate"):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-',])
if operator == '+':
    answer = num1 + num2
elif operator == '-':
    answer = num1 - num2

user = int(input(f"What is {num1} {operator} {num2} = "))

if user == answer:
    print("correct!")
    
elif user != answer:
    print("wrong")
    print("try again")


    

