from data import difficulty
from data import category
class Quizzer:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.difficulty = "easy"
        self.question_type = "True/False"
        self.question_size = 5

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q {self.question_number}: {current_question.question} (True/False): ")
        if self.check_answer(user_answer, current_question.answer):
            print("You got it right!")
        else:
            print("That was not correct.")
        print(f"The correct answer was: {current_question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number} \n")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True

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
        


