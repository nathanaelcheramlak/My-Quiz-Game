from data import difficulty
from data import category
class Quizzer:

    def __init__(self):
        self.question_number = 0
        self.question_list = ''
        self.score = 0
        self.difficulty = "easy"
        self.question_type = "multiple"
        self.question_size = 5

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        multiple_question_letters = dict()
        # For True/False Questions
        if self.question_type == 'boolean': 
            user_answer = input(f"Q {self.question_number}: {current_question['question']} ({self.question_type}): ")
        
        # For multiple choice questions
        elif self.question_type == 'multiple':

            from random import shuffle
            choices = current_question['incorrect_answers'] + [current_question['correct_answer']]
            shuffle(choices) # Shuffles the choices so the answer is random

            print(f'Q {self.question_number}: {current_question['question']}') # Display the question

            multiple_question_letters = dict(enumerate(choices))
            for key, value in multiple_question_letters.items():
                print(f"{chr(key+65)}. {value}")

            user_answer = input("Answer: ")

        if self.check_answer(user_answer, current_question['correct_answer'], multiple_question_letters):
            print("You got it right!")
        else:
            print("That was not correct.")
        print(f"The correct answer was: {current_question['correct_answer']}")
        print(f"Your current score is: {self.score}/{self.question_number} \n")

    def check_answer(self, user_answer, correct_answer, choices_list=None):
        if self.question_type == 'multiple':
            ascii_value = ord(user_answer) - 65
            if ascii_value in choices_list and choices_list[ascii_value].lower() == correct_answer.lower():
                self.score += 1
                return True
        else:
            if user_answer.lower() == correct_answer.lower() or user_answer[0].lower() == correct_answer[0].lower(): # So that it works for just 'T' instead of 'True'
                self.score += 1
                return True
        return False

class MainHelper:
    @staticmethod
    def validate_input(user_input, input_type):
        if input_type == "difficulty":
            return user_input in difficulty
        elif input_type == "question_size":
            return user_input > 0 and user_input <= 15
        elif input_type == "question_type":
            if user_input == 1 or user_input == 2:
                return True
            return False
        elif input_type == "category_id":
            return user_input >= 1 and user_input <= 24
        else:
            return True
    @staticmethod
    def question_id_parser():
        output_text = ""
        for type in category:
            for val in type.values():
                output_text += " {}".format(val)
            output_text += "\n"
        return output_text

        


