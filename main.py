import random
import logging
from typing import List


logging.basicConfig(level=logging.INFO)


class GameQuestion:
    def __init__(self, prompt: str, answers: dict, correct_answer: str):
        self.prompt = prompt
        self.answers = answers
        self.correct_answer = correct_answer

    def check_answer(self, answer: str) -> bool:
        return answer == self.correct_answer


class Game:
    def __init__(self, questions: List[dict]):
        self.questions = []
        for q in questions:
            self.questions.append(GameQuestion(q['prompt'], q['answers'], q['correct_answer']))
        self.score = 0
        self.total_questions = len(self.questions)

    def start(self):
        logging.info("Welcome to Question Challenge!")
        logging.info(f"You will be asked a series of {self.total_questions} various questions.")
        logging.info("Answer each question by entering the letter (A, B, or C) corresponding to the correct answer.")
        input("Press enter to begin...")

        random.shuffle(self.questions)
        for i, question in enumerate(self.questions, start=1):
            logging.info(f"\nQuestion {i}: {question.prompt}")
            for option, answer in question.answers.items():
                logging.info(f"{option}. {answer}")

            user_answer = input("Your answer: ").upper()
            while user_answer not in ["A", "B", "C"]:
                logging.info(f"'{user_answer}' is not a valid option! Try again")
                user_answer = input("Your answer: ").upper()

            if question.check_answer(user_answer):
                logging.info("Correct answer!")
                self.score += 1
            else:
                logging.info(f"Sorry, the correct answer was {question.correct_answer}.")

        logging.info(f"\nGame over! You scored {self.score} out of {self.total_questions}.")

    def reset(self):
        self.score = 0


def main():
    questions = [
        {
            "prompt": "What is the current capital of Japan?",
            "answers": {"A": "Tokyo", "B": "Asuka", "C": "Kuni-kyo"},
            "correct_answer": "A"
        },
        {
            "prompt": "In 1945, the Atomic bomb was dropped on Hiroshima, what was the name of the bomb?",
            "answers": {"A": "Big Boy", "B": "Little Boy", "C": "Untitled"},
            "correct_answer": "B"
        },
        {
            "prompt": "Which company created Santa Claus in 1931, St. Nicholas' interpretations in the modern world.?",
            "answers": {"A": "Pepsi", "B": "Corona", "C": "Coca-Colas"},
            "correct_answer": "C"
        }
    ]
    game = Game(questions)

    while True:
        game.start()

        play_again_answer = input("Do you want to play again? (y/n)").lower()
        while play_again_answer not in ["y", "n"]:
            play_again_answer = input("Do you want to play again? (y/n)").lower()

        if play_again_answer == "n":
            print("Goodbye, see you next time!")
            break


if __name__ == '__main__':
    main()
