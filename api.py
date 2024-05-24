import requests
from data import category
            
class FetchApi:
    question_url = ""
    available_questions = 0
    question_content = dict()

    def question_url_builder(self, difficulty, question_size, question_type, question_id):
        # Builds the url needed to be used to fetch the question according to the user's preference.
        url = "https://opentdb.com/api.php?"
        if question_size:
            url += "amount={}".format(question_size)
        if question_id:
            url += "&category={}".format(question_id+8)
        if difficulty:
            url += "&difficulty={}".format(difficulty)
        if question_type:
            url += "&type={}".format(question_type)

        FetchApi.question_url = url
        print(f"The url of the fetched site is {url}")
    
    def compare_with_available_questions(self, question_size):
        return question_size > FetchApi.available_questions

    def fetch(self):
        # Calls question_url_builder to get the url
        url = FetchApi.question_url
        response = requests.get(url).json()
        FetchApi.question_content = response

    def available_question_counter(self):
        # Counts the number of questions that were fetched using the api.
        FetchApi.available_questions = len(FetchApi.question_content['results'])

    def method_caller(self, difficulty, question_size, question_type, question_id):
        self.question_url_builder(difficulty, question_size, question_type, question_id)
        self.fetch()
        self.available_question_counter()
    

