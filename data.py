question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

category = [
    {'id': 1, 'name': 'General Knowledge'}, 
    {'id': 2, 'name': 'Entertainment: Books'},
    {'id': 3, 'name': 'Entertainment: Film'},
    {'id': 4, 'name': 'Entertainment: Music'},
    {'id': 5, 'name': 'Entertainment: Musicals & Theatres'},
    {'id': 6, 'name': 'Entertainment: Television'},
    {'id': 7, 'name': 'Entertainment: Video Games'},
    {'id': 8, 'name': 'Entertainment: Board Games'}, 
    {'id': 9, 'name': 'Science & Nature'},
    {'id': 10, 'name': 'Science: Computers'},
    {'id': 11, 'name': 'Science: Mathematics'},
    {'id': 12, 'name': 'Mythology'},
    {'id': 13, 'name': 'Sports'},
    {'id': 14, 'name': 'Geography'},
    {'id': 15, 'name': 'History'},
    {'id': 16, 'name': 'Politics'},
    {'id': 17, 'name': 'Art'},
    {'id': 18, 'name': 'Celebrities'},
    {'id': 19, 'name': 'Animals'},
    {'id': 20, 'name': 'Vehicles'},
    {'id': 21, 'name': 'Entertainment: Comics'},
    {'id': 22, 'name': 'Science: Gadgets'},
    {'id': 23, 'name': 'Entertainment: Japanese Anime & Manga'},
    {'id': 24, 'name': 'Entertainment: Cartoon & Animations'}
]

difficulty = ['easy', 'medium', 'hard']

# question_type = ['True/False', 'Multiple Choice']
question_type = ['boolean', 'multiple']

new_data = {"response_code":0,"results":[{"type":"multiple","difficulty":"medium","category":"General Knowledge","question":"Whose greyscale face is on the kappa emoticon on Twitch?","correct_answer":"Josh DeSeno","incorrect_answers":["Justin DeSeno","John DeSeno","Jimmy DeSeno"]},
                                         {"type":"multiple","difficulty":"medium","category":"General Knowledge","question":"Where does water from Poland Spring water bottles come from?","correct_answer":"Maine, United States","incorrect_answers":["Hesse, Germany","Masovia, Poland","Bavaria, Poland"]}]}

tf_data = {"response_code":0,"results":[{"type":"boolean","difficulty":"medium","category":"Mythology","question":"The Japanese god Izanagi successfully returned his wife Izanami from the Underworld.","correct_answer":"False","incorrect_answers":["True"]}]}