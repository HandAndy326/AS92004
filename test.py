import random

history = []

while True:
    instruction = input("Do you know how to do a maths quiz? ")
    if not instruction:
        instruction = input("Please enter yes or no: ")
    instructions = instruction[0]
    instructions = instructions.lower()
    
    if instructions == "n":
        print('''You are going to select a difficulty out of primary and intermediate.
        Then you are going to get a question that is randomly generated which you have to answer
            ''')
        break
    elif instructions == "y":
        print("Let's start")
        break
    else:
        print("Please enter either yes or no")

number_of_questions = int(input("How many questions do you want? "))
if not number_of_questions:
    number_of_questions = int(input("Please enter a number: "))
difficulty = input("Do you want the primary school questions or the intermediate school questions? ").lower()
difficulty2 = difficulty[0]
for i in range(number_of_questions):
    operator = ''
    num1 = 0
    num2 = 0
    if difficulty2 == ("p"):
        num1 = random.randint(1, 10)
        num2 = random.randint(num1, 10)
        operator = random.choice(['+', '-',])
    elif difficulty2 == ("i"):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operator = random.choice(['+', '-',])
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    user_answer = int(input(f"What is {num2} {operator} {num1} = "))
    history.append((f"{num2} {operator} {num1}", user_answer))
    if user_answer == answer:
        print("correct!")
    elif user_answer != answer:
        print("wrong")
    else:
        print("PLease enter a number as your answer")
request = input("Do you want to see your questions and answers? ").lower()
request2 = request[0]
if request2 == "y":
    for question, user_ans in history:
        print(f"Question: {question}, Your answer: {user_ans}")
elif request2 == "n":
    print("Ok")


    

