from data import question_data

class Question:
    def __init__(self, q_text, q_answer):
        self.question = q_text
        self.answer = q_answer

question_bank = []
for question in question_data:
    question_text = question["text"]
    answer_text = question["answer"]

    new_question = Question(question_text, answer_text)
    question_bank.append(new_question)
