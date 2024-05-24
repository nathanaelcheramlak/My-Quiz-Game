from Quiz import Quizzer, MainHelper
from api import FetchApi

def oneSelected():
    print(MainHelper.question_id_parser()) # Prints a list of categories with their question_id

    category_id = int(input("Choose the Genre of your questions (1-24): "))
    while not MainHelper.validate_input(category_id, "category_id"): # Validates the user input.
        category_id = int(input("Incorrect Input! Choose only from (1-24): "))

    fetcher.method_caller(quiz1.difficulty, quiz1.question_size, quiz1.question_type, category_id)
    print(f"Debug *** Difficulty {quiz1.difficulty}")
    # Creating a Quizzer Object with the newly initialized values
    quiz1.question_list = fetcher.question_content['results']
    print("Length of the data: {}".format(len(fetcher.question_content['results'])))
    print("Couldn't find the required number of questions.")

    while quiz1.still_has_questions():
        quiz1.next_question()
    print("======================")
    print(f"You got a total score of {quiz1.score}/{quiz1.question_number}")
    print("======================")

def twoSelected():
    print("Options")
    print("Current Settings:")
    print(f"""
* Difficulty: {quiz1.difficulty}
* Number of Questions: {quiz1.question_size}
* Question Type: {quiz1.question_type}""")
    change_option = input("Do you want to modify settings? (Y/N) ")
    if change_option.lower() == "y":
        # If the user wants to change the option
        new_difficulty = input("Enter Difficulty(easy, medium, hard): ")
        while not MainHelper.validate_input(new_difficulty, "difficulty"):
            new_difficulty = input("Incorrect choice! Choose only from (easy, medium, hard): ")

        new_question_size = int(input("How many questions do you want? (1 - 15) "))
        while not MainHelper.validate_input(new_question_size, "question_size"):
            new_question_size = int(input("Incorrect choice! Choose only from (1 -15): "))

        new_question_type = int(input("1-True/False\n"
                                        "2-Multiple Choice\n"
                                        "Enter your choice: "))
        while not MainHelper.validate_input(new_question_type, "question_type"):
            new_question_type = int(input("Incorrect Choice! Choose only '1' or '2': "))
        
        print("New difficulty is set to ", new_difficulty)
        quiz1.difficulty = new_difficulty
        quiz1.question_size = new_question_size
        question_type = ['boolean', 'multiple']
        quiz1.question_type = question_type[new_question_type-1]
        print(f"Question type set to {quiz1.question_type}")


# Creating a Quizzer Object
quiz1 = Quizzer()

while True:
    # Createing a FetchApi object
    fetcher = FetchApi()

    print("""
******** Welcome to Quizzers ******** 
    1. Start Game
    2. Options
    3. About
    4. Quit
""")
    prompt = input(":> ")
    if prompt == "1":
        oneSelected()
        
    elif prompt == "2":
        twoSelected()

    elif prompt == "3":
        print("About")
    elif prompt == "4":
        print("Thanks for trying out Quizzer.")
        break
    else:
        print("Incorrect Input! Try Again.")

