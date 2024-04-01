import requests
from data import category

url = "https://opentdb.com/api_count.php?category="
question_list = []
for i in range(9, 33):
    new_url = url + str(i)
    response = requests.get(new_url).json()
    question_list.append(response['category_question_count'])


for question in question_list:
    for num in question.values():
        if num < 10:
            print("False")
        else:
            print("True")
            print(question)

class FetchApi:
    def __init__(self):
        available_questions = 0

    def question_url_builder(self, difficulty, question_size, question_type, question_id):
        url = "https://opentdb.com/api.php?"
        if question_size:
            url += "amount={}".format(question_size)
        if question_id:
            url += "&category={}".format(question_id)
        if difficulty:
            url += "&difficulty={}".format(difficulty)
        if question_type:
            url += "&type={}".format(question_type)
        # "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=multiple"
        return url
    
    def compare_with_available_questions(self, question_size):
        return question_size > FetchApi.available_question

    def fetch(self, difficulty, question_size, question_type, question_id):
        # Calls question_url_builder to get the url
        url = self.question_url_builder(self, difficulty, question_size, question_type, question_id)
        response = requests.get(url).json()
        return response
    
    def available_question_counter(self, response):
        
    