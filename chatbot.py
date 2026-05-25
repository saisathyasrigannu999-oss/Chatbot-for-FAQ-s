import pandas as pd

data = pd.read_csv("faqs.csv")

questions = data["Question"].tolist()
answers = data["Answer"].tolist()

def get_response(user_question):

    user_question = user_question.lower()

    for i in range(len(questions)):

        if questions[i].lower() in user_question:

            return answers[i]

    return "Sorry, I don't understand."
