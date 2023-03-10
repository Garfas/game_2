How to play the game:
   we run the  `main.py` file. Information message with game instructions
   and the available user choices will be displayed in the terminal. If the user enters a choice
    which is not in the list of choices, he will be asked to enter a choice from
    suggested options, and the question will be returned for repetition. Point 1 is
    for each question answered. At the end of the game, points are scored based on
     about how many readings were answered correctly and how many questions were incorrect.

Tip:
   There are 3 questions in this game. In order to have more questions, it is necessary
   add to the questions.py file. existing function
def main()
    questions[
        {
            "prompt": "What is the current capital of Japan?",
            "answers": {"A": "Tokyo", "B": "Asuka", "C": "Kuni-kyo"},
            "correct_answer": "A"
        }
    ]


Creating a game without an importable module, explanation of functions/methods:

1. import random: This line imports the random module, which is used later in the code to shuffle the order of the questions.

2. import logging: This line imports the logging module, which is used to log messages at various levels of severity throughout the code.

3. from typing import List: This line imports the List type from the typing module, which is used to define the type of the questions parameter in the Game class constructor.

4. logging.basicConfig(level=logging.INFO): This line configures the logging module to log messages with a severity level of INFO or higher.

5. class GameQuestion:: This line defines a class called GameQuestion that represents a single question in the game. The class has three attributes: prompt, which is the text of the question; answers, which is a dictionary of possible answers (with letters A, B, and C as keys and the corresponding answer text as values); and correct_answer, which is the letter corresponding to the correct answer.

6. def __init__(self, prompt: str, answers: dict, correct_answer: str):: This line defines the constructor for the GameQuestion class. The constructor takes three arguments: prompt, answers, and correct_answer. These arguments are used to initialize the prompt, answers, and correct_answer attributes of the new GameQuestion object.

7. def check_answer(self, answer: str) -> bool:: This string defines a method called check_answer that checks whether the given answer is correct. The method takes one argument, response, which is a string representing the user's response. The method returns True if the user's answer is correct, otherwise False.

8. class Game:: This line defines a class named Game that represents the entire game. The class has two attributes: questions, which is a list of GameQuestion objects; and the score, which is the user's score, is initialized to 0.

9. def __init__(self, questions: List[dict]):: This line defines the constructor for the game class. The constructor takes one argument, questions, which is a list of vocabularies representing game questions. The constructor initializes the questions attribute by creating a new GameQuestion object for each dictionary in the list with a score of 0.

10. def start(self): This line defines a method called start that starts the game. The method begins by registering a welcome message and game instructions. It then shuffles the order of the questions using the random.shuffle function. For each question, the method registers the question prompt and possible answers, prompts the user for an answer, and checks that the answer is correct using the GameQuestion object's check_answer method. If the answer is correct, the user's score is increased by 1. After all questions are asked, the user's score is recorded.

11. def reset(self):: This line defines a method called reset that resets the user result to 0.

12. def main():: This line defines the main function, The function initializes the list of questions as a list of dictionaries, creates a new game object using this list, and then enters a loop that repeatedly runs `start