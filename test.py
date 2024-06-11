import random
history = []
def getting_instructions():
    while True:
        #Asking the user if they know how to do a maths quiz
        instruction = input("Do you know how to do a maths quiz? ")
        #If the user doesn't enter yes or no, the program asks for either yes or no
        if not instruction:
            instruction = print("Please enter yes or no: ")
            continue
        instructions = instruction[0]
        instructions = instructions.lower()
        #If the user entered no, this bit of code will begin which gives them the instructions
        if instructions == "n":
            print('''You are going to select a difficulty out of primary and intermediate.
    Then you are going to get a question that is randomly generated which you have to answer''')
            break
        #If the user entered yes, the program continues
        elif instructions == "y":
            print("Let's start")
            break
def getting_number_of_questions():
    while True:
        try:
            #Asking the user how many questions they want, if they enter a integer the program will continue
            number_of_questions = int(input("How many questions do you want? "))
            break
        except ValueError:
            #If the user doesn't enter a integer and therfore causing a error, they will get redirected here
            number_of_questions =int(input("Please enter a valid integer. "))
            break

    return number_of_questions

#This asks the user if they want the primary level questions or the intermediate level questions
def getting_difficulty():
    difficulty = input("Do you want the primary school questions or the intermediate school questions? ").lower()
    #If the user did not enter any of the options below, the program asks the user again of they want primary of intermediate questions
    while difficulty not in ('p', 'i', 'pri', 'int', 'primary', 'intermediate'):
        print("Please enter either primary or intermediate")
        difficulty = input("Do you want the primary school questions or the intermediate school questions? ")
    difficulty2 = difficulty[0]
    return difficulty2

#This is the question generator, it generates however many questions you said you would like
#The question generator has two difficulties, the primary and the intermediate. You can choose out of.
def question_generator():
    for i in range(num_of_user_questions):
        operator = ''
        num1 = 0
        num2 = 0
        #If you chose primary as your difficulty, you will get two numbers generated from 1 to 10 and a operator that is either plus or minus
        if difficulty2 == ("p"):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operator = random.choice(['+', '-',])
        #If you chose intermediate as your difficulty, you will get two numbers generated from 1 to 100 and a operator that is either plus or minus
        elif difficulty2 == ("i"):
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            operator = random.choice(['+', '-',])
        #if the randomly chosen operator is a plus it will add the two numbers together
        if operator == '+':
            answer = num1 + num2
        #If the randomly chosen operator is a minus it will subtract the second number from the first number
        elif operator == '-':
            answer = num1 - num2
        #This is the user entering the answer to the randomly generated question. It stores their answer in a variable called user_answer
        user_answer = int(input(f"What is {num1} {operator} {num2} = "))
        #This saves the question and what the user put in as the answer
        history.append((f"{num1} {operator} {num2}", user_answer))
        #If what the user enetered was equal to the actual answer, the program prints correct and it continues to the next question
        if user_answer == answer:
            print("correct!")
        #If what the user enetered was not equal to the actual answer, the program prints wrong and gives them the right answer and continues
        elif user_answer != answer:
            print("wrong")
            print(f"The correct answer is {answer}")
        return num_of_questions_correct

def getting_history():
    while True:
        #Asks the user if they want their quiz history or not
        request = input("Do you want to see your questions and answers? ").lower()
        #If they enter something that is not yes or no, the program asks them to enter either yes or no and the user gets asked again if they want their history
        if not request:
            print("Please enter either yes or no")
            continue
        request2 = request[0]
        #If the user said yes to getting their history, it gets printed out
        if request2 == "y":
            for question, user_ans in history:
                print(f"Question: {question}, Your answer: {user_ans}")
            break
        #If they say no, the game end and it thanks the user for playing
        elif request2 == "n":
            print("Thanks for playing")
            break



getting_instructions()

num_of_user_questions = getting_number_of_questions()

difficulty2 = getting_difficulty()

question_generator()

getting_history()
