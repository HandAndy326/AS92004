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
number_of_questions = 0
number_of_questions = int(input("How many questions do you want? "))

difficulty = input("Do you want the primary school questions or the intermediate school questions? ").lower()
difficulty2 = difficulty[0]
for i in range(number_of_questions):
    operator = ''
    num1 = 0
    num2 = 0
    if difficulty2 == ("p"):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-',])
    elif difficulty2 == ("i"):
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


    

