import random

class TriviaGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def play_round(self):
        question = random.choice(self.questions)
        print(question.text)

        option_num = 1
        for option in question.options:
            print(f"{option_num}. {option}")
            option_num += 1

        while True:
            try:
                user_answer = int(input("Your answer (1-4): "))
                if 1 <= user_answer <= 4:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if question.options[user_answer - 1] == question.answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect. The answer is {question.answer}.")